from pathlib import Path
import string
from Interfaces.scanner import Scanner

class LinScanner(Scanner):
    def scan_disk(self, path: string):
        print('Linux scanner')