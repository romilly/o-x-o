import unittest

from notebooks.notebook import read_apl_book_from


class NotebookCase(unittest.TestCase):
    def setUp(self) -> None:
        self.notebook = read_apl_book_from('data/sample-notebook.ipynb')

    def test_knows_apl_cells(self):
        self.assertEqual(len(self.notebook.apl_cells()), 12)

    def test_knows_markdown_cells(self):
        self.assertEqual(len(self.notebook.markdown_cells()), 6)


if __name__ == '__main__':
    unittest.main()
