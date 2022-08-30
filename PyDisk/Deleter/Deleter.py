from shutil import rmtree
from PyDisk.DataClasses.fileClass import FileClass
from pathlib import Path

class Deleter():
    
    @staticmethod
    def deleteFile(files: list[FileClass]) -> None:

        for file in files:  
            try:
                Path(file.path).unlink(missing_ok=True) # Handles if file was moved/deleted/whatever before script list refreshes
            except:
                print('Error') # TODO: Handle it somehow
     
    # TODO: Implement deteing entire folder (That works, but Try, Except...)           
    # @staticmethod
    # def deleteDir(path: Path) -> None:
    #     rmtree(path)
        
