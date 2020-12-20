import unittest

from notebooks.notebook import APLCell


class MockNotebookCell:
    def __init__(self, type, source):
        self.type = type
        self.source = source


def apl_cell(source: str):
    return APLCell(MockNotebookCell('code',source))


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



if __name__ == '__main__':
    unittest.main()
