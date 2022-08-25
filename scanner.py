from abc import abstractmethod
from pathlib import Path


class Scanner():
    
    @abstractmethod
    def scan_disk(self, path: Path):
        pass