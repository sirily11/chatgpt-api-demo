import dataclasses

import numpy as np
from scipy.optimize import linear_sum_assignment

from service.model.base_model import BaseModel


@dataclasses.dataclass
class RunResult:
    total_profit: int
    assignments: any


class AuctionModel(BaseModel):
    description = "Generate best assignment of bidders to items to maximize profit"

    def run(self, num_bidders: int, num_of_items: int, bids: dict[int, dict[int, int]]) -> RunResult:
        """
        :param num_bidders:
        :param num_of_items:
        :param bids: [bidder][item] = bid
        :return:
        """
        # Create a cost matrix from the bids
        cost_matrix = np.zeros((num_bidders, num_of_items))
        for bidder, items in bids.items():
            for item, bid in items.items():
                cost_matrix[bidder][item] = -bid  # We negate the bids because linear_sum_assignment minimizes the cost

        # Solve the assignment problem
        row_ind, col_ind = linear_sum_assignment(cost_matrix)

        # Calculate the total profit
        total_profit = -cost_matrix[row_ind, col_ind].sum()  # We negate the profit because we negated the bids

        # Create the assignment list
        # the first one is the index of the bidder and the second one is the index of the item.
        assignments = list(zip(row_ind, col_ind))

        return RunResult(total_profit, assignments)
