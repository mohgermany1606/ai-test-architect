from pydantic import BaseModel


class TestCase(BaseModel):

    test_id: str

    title: str

    steps: list[str]

    expected_result: str