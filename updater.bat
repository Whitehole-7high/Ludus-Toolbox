chcp 65001 >nul
if not exist version.txt start "" https://lt.free.je/ & exit
set /p ver=<version.txt
set url=https://lt.free.je/update/?ver=%ver%
start "" %url%