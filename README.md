# PyDisk

*This readme works rn as info spreader, will write it correctly later.*

**For now, you need to run it in Virtual Environment!** 

*Check [here](https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/50194143#50194143) how to do it.*

## Scanner

- [FileClass](Scanner/DataClasses/fileClass.py) - Class to hold every single file -> Also hash it to duplicate searching
- [win_scanner](Scanner/OSScanners/win_scanner.py) - Scans files. I think it would work with Linux, but for Strategy purpose it's here
- [lin_scanner](Scanner/OSScanners/lin_scanner.py) - Just to test
- [Strategy](Scanner/Strategy.py) - Main point to run a strategy and backend of scanning


## Archiver

Static as well.

```py
Archiver(pathToArchive: Path, listOfFiles: list [fileClass])
```

## Deleter 

~~Idk if it should be in FileClass or directly in other class, to consider :)~~

Class with static methods


