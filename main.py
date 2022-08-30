from PyDisk.Scanner.Strategy import Context
from PyDisk.Scanner.OSScanners.win_scanner import WinScanner
from PyDisk.Deleter.Deleter import Deleter

# Test playground; Later main point of program
if __name__ == "__main__":
    context = Context(WinScanner())
    test = context.scan_files('C:\\Test')
    print(test)
    
    testFile = test[0]
    Deleter.deleteFile(test[0])
    print('Deleted!', testFile.name)