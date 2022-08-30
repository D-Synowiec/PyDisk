from pathlib import Path
from zipfile import ZipFile
from PyDisk.DataClasses.fileClass import FileClass
from PyDisk.Deleter.Deleter import Deleter

class Archiver():
    
    @staticmethod
    def archiveFiles(files: list[FileClass], archive_path: Path, to_delete: bool=False) -> None:
        zipObj = ZipFile(archive_path, 'w')
        
        for file in files:
            #TODO: Add Try Except bla bla bla
            zipObj.write(file.path, arcname=file.name)
        
        if to_delete == True:
            Deleter.deleteFile(files)