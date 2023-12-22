from service.functions import BaseFunction
from service.model.supa_model import AuctionModel


class Zoey(BaseFunction):
    name = "AuctionBot"
    description = "Get bid info"
    parameters = {
        "type": "object",
        "properties": {
            "num_items": {
                "type": "integer",
                "description": "The amount of info to get",
            }
        },
        "required": ["num_items"],
    }

    model = AuctionModel()

    def run(self, arguments: dict):
        print(f"arguments: {arguments}")
        num_items = arguments["num_items"]
        bids = {
            0: {0: 10, 1: 15, 2: 5},
            1: {0: 15, 1: 10, 2: 20},
            2: {0: 5, 1: 20, 2: 15}
        }
        result = self.model.run(bids=bids, num_of_items=3, num_bidders=3)
        prompt = f"The following is a bid game for {num_items} items. The bids are as follows:\n"
        prompt += f"Our model is doing the following calculation: {self.model.description}\n"
        prompt += f"And the result from our state of the art model is:\n"
        prompt += f"the assignments are {result.assignments}\n"
        prompt += "Give a simple explanation of the result above for the high school student.\nAnswer: "

        return self.api.get_chat_response(message=prompt)
