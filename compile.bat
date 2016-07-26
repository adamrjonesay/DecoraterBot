@echo off
goto choice

:choice
echo Do you want to build 32-bit pyd files? [Y, N]
set /P c=
if /I "%c%" EQU "Y" goto :buildx86
if /I "%c%" EQU "N" goto :choice2

:choice2
echo Do you want to build 64-bit pyd files? [Y, N]
set /P c=
if /I "%c%" EQU "Y" goto :buildx64
if /I "%c%" EQU "N" goto :pause_things


:buildx86
"%SystemDrive%\Python35\python.exe" ".\setup.py" --quiet build
goto choice2

:buildx64
"%SystemDrive%\Python35X64\python.exe" ".\setup.py"  --quiet build
goto pause_things


:pause_things
echo Build Complete.
pause
