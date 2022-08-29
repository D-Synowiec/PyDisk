from dataclasses import dataclass, field
from pathlib import Path
import os
import pathlib
import hashlib

@dataclass
class FileClass:
    name: str = field(init=False)
    size: int = field(init=False) # In bytes
    extension: str = field(init=False)
    path: Path
    hash: str = field(init=False)
    
    def __post_init__(self):
        self.name = pathlib.Path(self.path).name
        self.size = os.path.getsize(self.path)
        self.extension = pathlib.Path(self.path).suffix
        self.hash = self.hash_file()
    
    def hash_file(self) -> str:
        h_sha256 = hashlib.sha256()
        
        with open(self.path,'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h_sha256.update(chunk)
                
        return h_sha256.hexdigest()
    