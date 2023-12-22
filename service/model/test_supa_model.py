import unittest

from service.model.supa_model import AuctionModel


class TestAuctionModel(unittest.TestCase):
    def setUp(self):
        self.model = AuctionModel()

    def test_run(self):
        num_bidders = 3
        num_of_items = 3
        bids = {
            0: {0: 10, 1: 15, 2: 5},
            1: {0: 15, 1: 10, 2: 20},
            2: {0: 5, 1: 20, 2: 15}
        }
        result = self.model.run(num_bidders, num_of_items, bids)
        self.assertEqual(result.total_profit, 50)
        self.assertEqual(sorted(result.assignments), [(0, 0), (1, 2), (2, 1)])


if __name__ == '__main__':
    unittest.main()
