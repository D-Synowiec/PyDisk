# PyDisk

*This readme works rn as info spreader, will write it correctly later.*

**For now, you need to run it in Virtual Environment!**

*Check [here](https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/50194143#50194143) how to do it.*

*Looks like no more, but it's better to keep it that way.*

## GUI

Oh Boy. I don't really want to do it. Tk, maybe I'll find better solution to it.

Middleware (Logic-GUI connector), should be easy, but first of all, We need that GUI to move forward.

## Duplicate-Finder

Skipping for now.

## Scanner

- [FileClass](PyDisk/DataClasses/fileClass.py) - Class to hold every single file -> Also hash it to duplicate searching
- [win_scanner](PyDisk/Scanner/OSScanners/win_scanner.py) - Scans files. I think it would work with Linux, but for Strategy purpose it's here
- [lin_scanner](PyDisk/Scanner/OSScanners/lin_scanner.py) - Just to test
- [Strategy](PyDisk/Scanner/Strategy.py) - Main point to run a strategy and backend of scanning
- [Deleter](PyDisk/Deleter/Deleter.py) - Class with static methods to remove files.
- [Archiver](Pydisk/Archiver/Archiver.py) - Class with static method to ZIP files.

## Deleter

- [x] Delete file/files (GUI has to make list from files to delete) Note: We have to refresh disk after deleting (Add event to deleting)
- [ ] Hadnle entire dir to delete (Duh)
