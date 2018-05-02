import unittest

from bag.bag import Bag


class BagTest(unittest.TestCase):

    def test_no_element_in_bag(self):
        bag = Bag()
        self.assertTrue(bag.is_empty())

    def test_add_one_element_to_bag(self):
        bag = Bag()
        bag.add('python')
        self.assertEqual(1, bag.size())

    def test_add_five_elements_and_iterate_bag(self):
        bag = Bag()
        langs = ['python', 'java', 'ruby', 'php', 'go']
        for lang in langs:
            bag.add(lang)
        self.assertEqual(len(langs), bag.size())
        for element in bag:
            self.assertIn(element, langs)
