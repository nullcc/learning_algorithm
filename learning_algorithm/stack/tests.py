import unittest

from stack.stack import Stack


class StackTest(unittest.TestCase):

    def test_no_element_in_stack(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_add_one_element_to_stack(self):
        stack = Stack()
        stack.push('python')
        self.assertEqual(1, stack.size())

    def test_push_five_elements_to_stack_and_pop_two_elements(self):
        stack = Stack()
        langs = ['python', 'java', 'ruby', 'php', 'go']
        for lang in langs:
            stack.push(lang)
        self.assertEqual(len(langs), stack.size())
        element1 = stack.pop()
        element2 = stack.pop()
        self.assertEqual('go', element1)
        self.assertEqual('php', element2)
        self.assertEqual(3, stack.size())

    def test_push_five_elements_to_stack_and_pop_all_elements(self):
        stack = Stack()
        langs = ['python', 'java', 'ruby', 'php', 'go']
        for lang in langs:
            stack.push(lang)
        self.assertEqual(len(langs), stack.size())
        for i in range(len(langs)):
            element = stack.pop()
            self.assertEqual(element, langs[len(langs)-i-1])
        self.assertTrue(stack.is_empty())

    def test_push_five_elements_and_iterate_stack(self):
        stack = Stack()
        langs = ['python', 'java', 'ruby', 'php', 'go']
        for lang in langs:
            stack.push(lang)
        self.assertEqual(len(langs), stack.size())
        for index, element in enumerate(stack):
            self.assertEqual(element, langs[len(langs)-index-1])
