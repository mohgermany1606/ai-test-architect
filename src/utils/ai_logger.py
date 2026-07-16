import logging
from pathlib import Path


Path("logs").mkdir(exist_ok=True)


logging.basicConfig(
    filename="logs/ai_execution.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


ai_logger = logging.getLogger("AI")