from PyDisk.Scanner.Interfaces.scanner import *
from PyDisk.Scanner.OSScanners.win_scanner import WinScanner
from PyDisk.Scanner.OSScanners.lin_scanner import LinScanner
from platform import system

class Context():
    
    def __init__(self, scanner: Scanner) -> None:
        
        self._scanner = scanner
        
    @property
    def scanner(self) -> Scanner:
        
        return self._scanner
    
    @scanner.setter
    def scanner(self, scanner: Scanner) -> None:
        self._scanner = scanner
        
    def scan_files(self, path: Path) -> list:
        return self._scanner.scan_disk(path)
        
        

if __name__ == "__main__":
    context = Context(WinScanner())
    test = context.scan_files('C:\\Test')
    print(test)
