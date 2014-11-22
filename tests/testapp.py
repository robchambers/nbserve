import unittest


class NBServeTestCase(unittest.TestCase):

    def testImports(self):
        """ Can we import everything?
        """
        pass

    # To do:
    # Does the index list the right files?
    # Can we load each notebook?
    # Does each notebook have the right info in it?
    # Are input cells properly hidden, etc?
    # Does the CLI work right?

    # def testIndex(self):
    #     with app.test_client() as c:
    #         c.get('/')

    def setUp(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()