from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:

    test_id: str
    title: str
    steps: List[str]
    expected_result: str