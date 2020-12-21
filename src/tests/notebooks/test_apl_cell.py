import unittest
from typing import List

from notebooks.notebook import APLCell


class MockNotebookCell:
    def __init__(self, cell_type, source: List[str]):
        self.cell_type = type
        self.source = source


def apl_cell(*lines: str):
    return APLCell(MockNotebookCell('code',list(lines)))


class APLCellTestCase(unittest.TestCase):

    def test_can_remove_comment(self):
        a_cell = apl_cell('foo ⍝ bar')
        self.assertEqual(a_cell.bodies(), ['foo '])

    def test_can_remove_quoted_contents(self):
        a_cell = apl_cell("foo 'baz'")
        self.assertEqual(a_cell.remove_quotes(), ['foo '])

    def test_can_find_identifiers(self):
        a_cell = apl_cell("foo bar 'baz' ⍝ bing")
        self.assertEqual(list(a_cell.identifiers()), [['foo','bar']])

    def test_can_find_assignment(self):
        a_cell = apl_cell("foo ← bar 'baz' ⍝ bing", 'goop')
        self.assertEqual(list(a_cell.assignments()), [['foo'],[]])




if __name__ == '__main__':
    unittest.main()
