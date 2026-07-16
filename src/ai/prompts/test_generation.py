GENERATE_TEST_CASES_PROMPT = """

You are a Senior QA Architect.

Analyze the requirement below.

Generate detailed test cases.

Requirement:

{requirement}

Return ONLY JSON.

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