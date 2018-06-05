@echo off
IF %COMP% == LAPTOP goto start
IF %COMP% == HOME goto normal

:start
\python33\scripts\ipython3 nbconvert --to slides python_9.ipynb --post serve
goto end

:normal
\python33b\scripts\ipython3 nbconvert --to slides python_9.ipynb --post serve

:end
echo CIAO




