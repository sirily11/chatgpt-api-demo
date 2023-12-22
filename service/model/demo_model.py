from service.model.base_model import BaseModel, RunResult


class DemoModel(BaseModel):
    description = "Given a list of bids, return the total amount of the top n bids"

    def run(self, bids: dict[str, int], num_items: int) -> RunResult:
        """
        Run function with given arguments

        3 bids, num_items = 1 -> Highest bid wins
        3 bids, num_items = 2 -> 2 highest bids win
        :param bids:
        :param num_items:
        :return:
        """
        sorted_bids = sorted(bids.items(), key=lambda x: x[1], reverse=True)
        return RunResult(
            name="DemoModel",
            amount=sum([bid for _, bid in sorted_bids[:num_items]]),
        )
