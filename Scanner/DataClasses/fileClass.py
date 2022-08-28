from dataclasses import dataclass
from pathlib import Path


@dataclass
class FileClass:
    name: str
    size: int
    extension: str
    path: Path
    
    def hash_file(self) -> str:
        pass
        # To implement for file comparation