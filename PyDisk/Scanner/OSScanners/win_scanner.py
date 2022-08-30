from pathlib import Path
from PyDisk.Scanner.Interfaces.scanner import Scanner
from PyDisk.DataClasses.fileClass import FileClass
import os

class WinScanner(Scanner):
    def scan_disk(self, path: Path) -> list:
        files_list = []
        for root, dirs, files in os.walk(path, topdown=True):
            for name in files:
                file_path = os.path.join(root, name)
                file = FileClass(file_path)
                files_list.append(file)
        return files_list
    
