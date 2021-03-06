#----------------------------------------------------
class testStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'Hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        #check that s,split fails when the seperator is not a string

        with self.assertRaises(TypeError):
            s.split(2)

    if name == 'main':
        unittest.main()