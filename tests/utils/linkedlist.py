from dataclasses import dataclass
from typing import Self


@dataclass
class MergeSource:
    """
    Example:
    pre_tokens = " watered"
        MS(" ", "w") -> MS("w", "a") -> MS("a", "t") -> MS("t", "e") -> MS("e", "r") -> MS("r", "e") -> MS("e", "d")

    merge:
                        self
        MS("w", "a") -> MS("a", "t") -> MS("t", "e") -> MS("e", "r")
        MS("w", "at") -> MS("a", "t") -> MS("at", "e") -> MS("e", "r")
        MS("w", "at") -> MS("at", "e") -> MS("e", "r")


        corner case: three repetitive chars
                        self
        MS("3", "0") -> MS("0", "0") -> MS("0", "0") -> MS("0", ",")
        MS("3", "00") -> MS("0", "0") -> MS("00", "0") -> MS("0", ",")
        MS("3", "00") -> MS("00", "0") -> MS("0", ",")
                         ^
                         |
                        already changed, so don't merge
    """

    left_token: bytes
    right_token: bytes
    raw_token: bytes
    count: int = 0
    prev: Self = None
    next: Self = None

    def __repr__(self) -> str:
        return f"MergeSource({self.left_token!r}, {self.right_token!r}, raw_token={self.raw_token!r}, count={self.count!r})"
