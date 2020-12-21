import re
from abc import ABC
from typing import List

dequoter = re.compile(r"'[^']*'")
name = re.compile('([A-Za-z_∆⍙][A-Za-z_0-9]*|⎕io)')


def make_list(source):
    return source if isinstance(source, list) else [source]


class Cell(ABC):
    def __init__(self, cell):
        self.cell = cell

    def source(self):
        return make_list(self.cell.source)

    def cell_type(self):
        return self.cell.cell_type


class MarkdownCell(Cell):
    pass


def line_body(line: str) -> str:
    if '⍝' not in line:
        return line
    front, back = line.split('⍝') # assumes no comment symbol in quotes
    return front


def remove_quotes_for(line: str):
    return dequoter.sub('', line)


def identifiers_in(line):
    return name.findall(line)


def code_for(line):
    return remove_quotes_for(line_body(line))


def assignments_in(line):
    if '←' not in line:
        return []
    return identifiers_in(line.split('←')[0])


class APLCell(Cell):
    def apply(self, method):
        return [method(line) for line in self.source()]


    def bodies(self) -> List[str]:
        return self.apply(line_body)
        # return [line_body(line) for line in self.source()]

    def remove_quotes(self):
        return [remove_quotes_for(line) for line in self.source()]

    def identifiers(self):
        return (identifiers_in(code_for(line)) for line in self.source())

    def assignments(self):
        return (assignments_in(code_for(line)) for line in self.source())




