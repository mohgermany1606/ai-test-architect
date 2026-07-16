from src.ai.test_generator import TestGenerator


requirement = """
User should be able to search Wikipedia
for Artificial Intelligence.
"""


tests = TestGenerator.generate(
    requirement
)


for test in tests:

    print("====================")

    print("Test ID:", test.test_id)

    print("Title:", test.title)

    print("Steps:")

    for step in test.steps:
        print("-", step)

    print(
        "Expected Result:",
        test.expected_result
    )