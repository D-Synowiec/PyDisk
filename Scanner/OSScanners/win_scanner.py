from pathlib import Path
from Interfaces.scanner import Scanner
from DataClasses.fileClass import FileClass
import os

class WinScanner(Scanner):
    def scan_disk(self, path: Path) -> list:
        files_list = []
        for root, dirs, files in os.walk(path, topdown=True):
            for name in files:
                file_path = os.path.join(root, name)
                split_tup = os.path.splitext(file_path)
                file_extension = split_tup[1][1:]
                file_stat = os.stat(file_path)
                file_size = round(file_stat.st_size / (1024 * 1024))
                file = FileClass(name, file_size,file_extension, file_path)
                files_list.append(file)
        return files_list
    
