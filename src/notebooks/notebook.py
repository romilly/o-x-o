from abc import ABC
from typing import List

import nbformat
import re

dequoter = re.compile(r"'[^']*'")

name = re.compile('([A-Za-z_∆⍙][A-Za-z_0-9]+)')

def listify(source):
    return source if isinstance(source, list) else [source]


class Cell(ABC):
    def __init__(self, cell):
        self.cell = cell

    def source(self):
        return listify(self.cell.source)

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


def line_body(line: str) -> str:
    front, back = line.split('⍝') # assumes no comment symbol in quotes
    return front


def remove_quotes_for(line: str):
    return dequoter.sub('', line)


def identifiers_in(line):
    return name.findall(line)


def code_for(line):
    return remove_quotes_for(line_body(line))


class APLCell(Cell):
    def bodies(self) -> List[str]:
        return [line_body(line) for line in self.source()]

    def remove_quotes(self):
        return [remove_quotes_for(line) for line in self.source()]

    def identifiers(self):
        return (identifiers_in(code_for(line)) for line in self.source())


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

