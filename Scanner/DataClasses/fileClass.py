from dataclasses import dataclass, field
from pathlib import Path
import os
import pathlib

@dataclass
class FileClass:
    name: str = field(init=False)
    size: int = field(init=False) # In bytes
    extension: str = field(init=False)
    path: Path
    
    def __post_init__(self):
        self.name = pathlib.Path(self.path).name
        self.size = os.path.getsize(self.path)
        self.extension = pathlib.Path(self.path).suffix
    
    def hash_file(self) -> str:
        pass
        # To implement for file comparation