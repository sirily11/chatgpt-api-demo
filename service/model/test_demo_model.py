import unittest

from service.model.demo_model import DemoModel


class MyTestCase(unittest.TestCase):
    def test_simple_bid(self):
        model = DemoModel()
        bids = {
            "Alice": 100,
            "Bob": 200,
            "Charlie": 300,
        }
        num_items = 1
        result = model.run(bids=bids, num_items=num_items)
        self.assertEqual(result.amount, 300)

    def test_two_bids(self):
        model = DemoModel()
        bids = {
            "Alice": 100,
            "Bob": 200,
            "Charlie": 300,
        }
        num_items = 2
        result = model.run(bids=bids, num_items=num_items)
        self.assertEqual(result.amount, 500)

    def test_three_bids(self):
        model = DemoModel()
        bids = {

            "Alice": 100,
            "Bob": 200,
            "Charlie": 300,
        }
        num_items = 3
        result = model.run(bids=bids, num_items=num_items)
        self.assertEqual(result.amount, 600)


if __name__ == '__main__':
    unittest.main()
