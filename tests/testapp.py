import unittest
import nbserve
import os

class NBServeTestCase(unittest.TestCase):

    def testImports(self):
        """ Can we import everything?
        """
        self.assertEqual(nbserve.__progname__,'nbserve')

    def testIndex(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('mocknb1.ipynb', response.data)

    def test_mocknb1(self):
        response = self.app.get('/mocknb1.ipynb/')
        self.assertEqual(response.status_code, 200)

    def test_mocknb1_has_input_code_cells(self):
        response = self.app.get('/mocknb1.ipynb/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('# This is a comment in the first input cell.', response.data)

    def test_mocknb1_has_output_cells(self):
        response = self.app.get('/mocknb1.ipynb/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('This is an output cell.', response.data)

    def test_mocknb1_has_printed_output(self):
        response = self.app.get('/mocknb1.ipynb/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('This is printed output.', response.data)

    def test_mocknb1_has_rendered_markdown(self):
        response = self.app.get('/mocknb1.ipynb/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<li>And, this is a markdown list item.</li>', response.data)


    # To do:

    # Does the CLI work right?

    def setUp(self):
        nbserve.set_working_directory(
            os.path.join(os.path.split(__file__)[0],'notebooks/'))
        self.app = nbserve.flask_app.test_client()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()