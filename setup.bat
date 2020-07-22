set curpath=%~dp0
echo %curpath%
setx PATH=%PATH%;%curpath%; /M
echo "Path set."
