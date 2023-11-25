from dataclasses import data
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    Source_URL:str
    local_data_file:Path
    unzip_dir:Path
    