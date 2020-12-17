from abc import ABC, abstractmethod
from typing import List

import nbformat


def listify(source):
    return source if isinstance(source, list) else [source]


class Cell(ABC):
    def __init__(self, cell):
        self.cell = cell

    def source(self):
        return listify(self.cell.source())

    def cell_type(self):
        return self.cell.cell_type


class Notebook:
    def __init__(self, file_name):
        self.file_name = file_name
        self.cells = []

    def add(self, cell: Cell):
        self.cells.append(cell)

    def markdown_cells(self) -> List['MarkdownCell']:
        return list(cell for cell in self.cells if cell.cell_type() == 'markdown')

    def apl_cells(self) -> List['MarkdownCell']:
        return list(cell for cell in self.cells if cell.cell_type() == 'code')


class MarkdownCell(Cell):
    pass


class APLCell(Cell):
    pass


def read_apl_book_from(file_name):
    with open(file_name) as nb:
        raw_book = nbformat.read(nb, as_version=4)
    language = raw_book.metadata.kernelspec.language
    if language != 'apl':
        raise ValueError('notebook must be APL')
    result = Notebook(file_name)
    for cell in raw_book.cells:
        if cell.cell_type in ['markdown','code']:
            klass = MarkdownCell if cell.cell_type == 'markdown' else APLCell
            result.add(klass(cell))
    return result

