BUG_ANALYSIS_PROMPT = """

You are an expert QA engineer.

Analyze this failed test.

Failure:

{failure}

Provide:

1. Root cause
2. Possible fix
3. Severity
4. Suggested action

"""