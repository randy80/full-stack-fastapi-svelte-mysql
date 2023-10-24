import os

from pydantic_settings import SettingsConfigDict
from pydantic_settings_yaml import YamlBaseSettings


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Settings(YamlBaseSettings):
    model_config = SettingsConfigDict(yaml_file=f'{ROOT_DIR}/config/config.yaml', env_file_encoding='utf-8', secrets_dir=None)

    domain: str


settings = Settings()
