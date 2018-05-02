import unittest

from linked_list.linked_list import LinkedList


class LinkedListTest(unittest.TestCase):

    def test_no_element_in_linked_list(self):
        linked_list = LinkedList()
        self.assertEqual(0, linked_list.size())

    def test_add_one_element_to_end_of_linked_list(self):
        linked_list = LinkedList()
        linked_list.add_last('python')
        self.assertEqual('python', linked_list.get_first().item)
        self.assertEqual('python', linked_list.get_last().item)
        self.assertEqual(1, linked_list.size())

    def test_add_two_elements_to_end_of_linked_list(self):
        linked_list = LinkedList()
        linked_list.add_last('python')
        linked_list.add_last('ruby')
        self.assertEqual('python', linked_list.get_first().item)
        self.assertEqual('ruby', linked_list.get_last().item)
        self.assertEqual(2, linked_list.size())

    def test_add_one_element_to_beginning_of_linked_list(self):
        linked_list = LinkedList()
        linked_list.add_first('python')
        self.assertEqual('python', linked_list.get_first().item)
        self.assertEqual('python', linked_list.get_last().item)
        self.assertEqual(1, linked_list.size())

    def test_add_two_elements_to_beginning_of_linked_list(self):
        linked_list = LinkedList()
        linked_list.add_first('python')
        linked_list.add_first('ruby')
        self.assertEqual('python', linked_list.get_last().item)
        self.assertEqual('ruby', linked_list.get_first().item)
        self.assertEqual(2, linked_list.size())

    def test_add_five_elements_to_end_and_iterate_linked_list(self):
        linked_list = LinkedList()
        langs = ['python', 'java', 'ruby', 'php', 'go']
        for lang in langs:
            linked_list.add_last(lang)
        self.assertEqual(len(langs), linked_list.size())
        for node in linked_list:
            self.assertIn(node.item, langs)

    def test_get_index(self):
        linked_list = LinkedList()
        langs = ['python', 'java', 'ruby', 'php', 'go']
        for lang in langs:
            linked_list.add_last(lang)
        self.assertEqual(len(langs), linked_list.size())
        self.assertEqual(langs[3], linked_list.get_index(3).item)
