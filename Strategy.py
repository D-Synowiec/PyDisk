from Interfaces.scanner import *
from Scanner.win_scanner import WinScanner
from Scanner.lin_scanner import LinScanner
from platform import system

from Scanner.win_scanner import WinScanner
class Context():
    
    def __init__(self, scanner: Scanner) -> None:
        
        self._scanner = scanner
        
    @property
    def scanner(self) -> Scanner:
        
        return self._scanner
    
    @scanner.setter
    def scanner(self, scanner: Scanner) -> None:
        self._scanner = scanner
        
    def scan_files(self) -> None:
        self._scanner.scan_disk('C:\\')
        

if __name__ == "__main__":
    context = Context(WinScanner())
    context.scan_files()

    context.scanner = LinScanner()
    
    context.scan_files()