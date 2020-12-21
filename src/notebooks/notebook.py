from typing import List

import nbformat

from notebooks.cells import Cell, MarkdownCell, APLCell


class Notebook:
    def __init__(self, file_name):
        self.file_name = file_name
        self.cells = []

    def add(self, cell: Cell):
        self.cells.append(cell)

    def markdown_cells(self) -> List['MarkdownCell']:
        return list(cell for cell in self.cells if cell.cell_type() == 'markdown')

    def apl_cells(self) -> List['APLCell']:
        return list(cell for cell in self.cells if cell.cell_type() == 'code')

    def find_apl_assignments(self):
        assignments = {}
        for cell in self.apl_cells():
            for names in cell.assignments():
                for name in names:
                    assignments[name] = cell
        return assignments


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


if __name__ == '__main__':
    nb = read_apl_book_from('data/sample-notebook.ipynb')
    print(nb.find_apl_assignments())