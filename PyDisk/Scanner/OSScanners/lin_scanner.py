from pathlib import Path
import string
from PyDisk.Scanner.Interfaces.scanner import Scanner

class LinScanner(Scanner):
    def scan_disk(self, path: string):
        print('Linux scanner')