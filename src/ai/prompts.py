GENERATE_TEST_CASES = """
You are a Senior QA Architect.

Generate test cases for this requirement:

{requirement}

Return ONLY valid JSON.

Format:

[
 {{
  "test_id": "",
  "title": "",
  "steps": [],
  "expected_result": ""
 }}
]
"""