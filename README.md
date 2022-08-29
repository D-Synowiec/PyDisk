# PyDisk

*This readme works rn as info spreader, will write it correctly later.*

## Scanner

- [FileClass](Scanner/DataClasses/fileClass.py) - Class to hold every single file -> Also hash it to duplicate searching
- [win_scanner](Scanner/OSScanners/win_scanner.py) - Scans files. I think it would work with Linux, but for Strategy purpose it's here
- [lin_scanner](Scanner/OSScanners/lin_scanner.py) - Just to test
- [Strategy](Scanner/Strategy.py) - Main point to run a strategy and backend of scanning


## Archiver

It needs to work with DataClasses - Mainly connected with GUI. Pretty simple I think?

```py
Archiver(pathToArchive: Path, listOfFiles: list [fileClass])
```

## Deleter 

Idk if it should be in FileClass or directly in other class, to consider :)



It would be nice to atleast tell me, that you're watching this repo :).