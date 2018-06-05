@echo off
IF %COMP% == LAPTOP GOTO start
IF %COMP% == HOME GOTO home

:start
C:\Python34\Scripts\ipython3 notebook
goto end

:home
D:\Python34\Scripts\ipython3 notebook

:end
echo CIAO


