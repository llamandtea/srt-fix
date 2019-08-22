# srt-fix
The purpose of this software is to simplify the synchronization of .srt subtitle files. 

## Usage
Currently, srt-fix only allows for mass synchronization of the subtitles, meaning you will only be able to input an initial timestamp and shift all the following subtitle timestamps accordingly.

#### Mass-shifting
You need to invoke the python intepreter on ``` __main__.py```:
```
py __main__.py filename.srt [hh:mm:ss,msmsms]
```
The arguments are:
* ```filename.srt```: the name of the .srt file to edit
* ```[hh:mm:ss,msmsms]```: the new timestamp of the initial subtitle
