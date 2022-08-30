from shutil import rmtree
from PyDisk.DataClasses.fileClass import FileClass
from pathlib import Path

class Deleter():
    
    @staticmethod
    def deleteFile(file: FileClass) -> None:
        Path(file.path).unlink()
        
    @staticmethod
    def deleteFiles(files: list[FileClass]) -> None:
        for file in files:
            Path(file.path).unlink()
            
    @staticmethod
    def deleteDir(path: Path) -> None:
        rmtree(path)