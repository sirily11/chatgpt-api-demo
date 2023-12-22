import dataclasses


@dataclasses.dataclass
class RunResult:
    name: str
    amount: int


class BaseModel:
    description: str

    def run(self, num_bidders: int, num_of_items: int, bids: dict[int, dict[int, int]]) -> RunResult:
        raise NotImplementedError()
