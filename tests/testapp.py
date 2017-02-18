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
        nbserve.update_config({'template':'full'})
        response = self.app.get('/mocknb1.ipynb/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('# This is a comment in the first input cell.', response.data)
        self.assertIn('In&nbsp;[', response.data)
        self.assertIn('<div class="prompt input_prompt">', response.data)

    def test_mocknb1_has_no_input_code_cells(self):
        nbserve.update_config({'template':'strip-input'})
        response = self.app.get('/mocknb1.ipynb/')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('# This is a comment in the first input cell.', response.data)
        self.assertNotIn('<div class="prompt input_prompt">', response.data)

    def test_mocknb1_has_output_cells(self):
        response = self.app.get('/mocknb1.ipynb/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('This is an output cell.', response.data)

    def test_mocknb1_has_no_output_cells_if_not_run(self):
        nbserve.update_config({'run':False})
        response = self.app.get('/mocknb1.ipynb/')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('This is an output cell.', response.data)


    def test_mocknb1_has_printed_output(self):
        response = self.app.get('/mocknb1.ipynb/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('This is printed output.', response.data)

    def test_mocknb1_has_rendered_markdown(self):
        response = self.app.get('/mocknb1.ipynb/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<li>And, this is a markdown list item.</li>', response.data)

    def test_reset(self):
        """ Does %reset -f work as expected?
        """
        response = self.app.get('/testreset.ipynb/')
        self.assertIn("Before reset, had 1: &lt;module &apos;Jupyter&apos;", response.data)
        self.assertIn("Before reset, had 2: &lt;module &apos;runipy&apos;", response.data)
        self.assertIn("Before reset, had 3: old value", response.data)
        self.assertIn("Before reset, had 4: temp value", response.data)
        self.assertIn("name &apos;Jupyter&apos; is not defined", response.data)
        self.assertIn("name &apos;runipy&apos; is not defined", response.data)
        self.assertIn("name &apos;my_var&apos; is not defined", response.data)
        #self.assertIn("&apos;module&apos; object has no attribute &apos;tempvar&apos;", response.data)

    def test_reset2(self):
        """ Is the notebook reset between runs?
        """
        response = self.app.get('/testreset2.ipynb/')
        self.assertIn("Before reset, had 1: &lt;module &apos;Jupyter&apos;", response.data)
        self.assertIn("Before reset, had 2: &lt;module &apos;runipy&apos;", response.data)
        self.assertIn("Before reset, had 3: old value", response.data)
        self.assertIn("Before reset, had 4: temp value", response.data)
        self.assertIn("name &apos;Jupyter&apos; is not defined", response.data)
        self.assertIn("name &apos;runipy&apos; is not defined", response.data)
        self.assertIn("name &apos;my_var&apos; is not defined", response.data)
        response = self.app.get('/testreset2.ipynb/')
        self.assertIn("Before reset, had 1: &lt;module &apos;Jupyter&apos;", response.data)
        self.assertIn("Before reset, had 2: &lt;module &apos;runipy&apos;", response.data)
        self.assertIn("Before reset, had 3: old value", response.data)
        self.assertIn("Before reset, had 4: temp value", response.data)
        self.assertIn("name &apos;Jupyter&apos; is not defined", response.data)
        self.assertIn("name &apos;runipy&apos; is not defined", response.data)
        self.assertIn("name &apos;my_var&apos; is not defined", response.data)


    # To do:
    # 'run' option false
    # Does the CLI work right?

    def setUp(self):
        nbserve.set_config({
            'working_directory':os.path.join(os.path.split(__file__)[0],'notebooks/'),
            'run':True})
        self.app = nbserve.flask_app.test_client()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()