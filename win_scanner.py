from pathlib import Path
import string
from scanner import Scanner

class WinScanner(Scanner):
    def scan_disk(self, path: string):
        print('Windows Scanner')