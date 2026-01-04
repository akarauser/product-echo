import json
from pathlib import Path
from typing import Any

from pydantic import BaseModel

from ._logger import logger


class ConfigValidation(BaseModel):
    data_path: str
    output_dir: str
    base_model: str
    max_length: int
    max_new_tokens: int
    repetition_penalty: float
    target_modules: list


def _read_json_file() -> Any | None:
    config_path = Path(f"{Path(__file__).parent}\\config.json")
    try:
        with config_path.open(encoding="utf-8") as file:
            config_values = json.load(file)
            return config_values
    except FileNotFoundError:
        logger.error("Config file not found.")


try:
    config_args = ConfigValidation.model_validate(_read_json_file())
except ValueError:
    logger.error("Validation failed.")
