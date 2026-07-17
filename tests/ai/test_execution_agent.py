from unittest.mock import patch

from src.agents.execution_agent import execution_agent



def test_execution_agent():


    state = {

        "requirement": "Search Wikipedia",

        "plan": [],

        "test_cases": [],

        "execution_status": "",

        "execution_result": "",

        "screenshots": []

    }


    with patch(
        "src.agents.execution_agent.Browser"
    ) as mock_browser:


        mock_page = mock_browser.return_value.__enter__.return_value


        result = execution_agent(state)


        assert (
            result["execution_status"]
            == "PASSED"
        )


        assert len(
            result["screenshots"]
        ) == 1