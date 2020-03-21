# wma2mp3
Converts wma-files to mp3-files recursively

SETUP
------------------

The tool depends of ffmpeg, which can be downloaded e.g. here:
https://ffmpeg.zeranoe.com/builds/

After installing ffmpeg, the path to your ...\ffmpeg\bin\ has to be added to the path variable.

Here you find a description how this can be done in Windows 10:
https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/


USAGE
-------------------
* After starting the tool, you will be asked to open a folder.
* Select the folder were all your music files are contained.
* A neighboring folder will be created with the postfix _mp3 (e.g. if you select _C:\Users\JohnDoe\Music_ your output folder will be named _C:\Users\JohnDoe\Music_mp3_).
* The output folder will contain the same subfolder structure as the input folder, all wma files will be converted to mp3 files. All subfolder that do not contain any wma files in the input folder, will not be present in the output folder.
