import unittest

from queue.queue import Queue


class QueueTest(unittest.TestCase):

    def test_no_element_in_queue(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())

    def test_enqueue_one_element_to_queue(self):
        queue = Queue()
        queue.enqueue('python')
        self.assertEqual(1, queue.size())

    def test_enqueue_five_elements_to_queue_and_dequeue_two_elements(self):
        queue = Queue()
        langs = ['python', 'java', 'ruby', 'php', 'go']
        for lang in langs:
            queue.enqueue(lang)
        self.assertEqual(len(langs), queue.size())
        element1 = queue.dequeue()
        element2 = queue.dequeue()
        self.assertEqual('python', element1)
        self.assertEqual('java', element2)
        self.assertEqual(3, queue.size())

    def test_enqueue_five_elements_to_queue_and_dequeue_all_elements(self):
        queue = Queue()
        langs = ['python', 'java', 'ruby', 'php', 'go']
        for lang in langs:
            queue.enqueue(lang)
        self.assertEqual(len(langs), queue.size())
        element1 = queue.dequeue()
        element2 = queue.dequeue()
        element3 = queue.dequeue()
        element4 = queue.dequeue()
        element5 = queue.dequeue()
        self.assertEqual('python', element1)
        self.assertEqual('java', element2)
        self.assertEqual('ruby', element3)
        self.assertEqual('php', element4)
        self.assertEqual('go', element5)
        self.assertTrue(queue.is_empty())

    def test_enqueue_five_elements_and_iterate_queue(self):
        queue = Queue()
        langs = ['python', 'java', 'ruby', 'php', 'go']
        for lang in langs:
            queue.enqueue(lang)
        self.assertEqual(len(langs), queue.size())
        for element in queue:
            self.assertIn(element, langs)
