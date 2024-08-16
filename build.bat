@echo off


if "%1"=="cleanUP" (
    echo Performing cleanup only...
    echo Removing dist, build and spec
    rmdir /s /q dist
    rmdir /s /q build
    del *.spec
    echo Cleanup complete. Press any key to exit.
    pause
    exit /b
)


echo Deleting old build artifacts...
    echo Removing dist, build and spec
rmdir /s /q dist
rmdir /s /q build
del *.spec


echo Rebuilding the executable...
pyinstaller --onefile --windowed main.py

echo Build complete. Press any key to exit.
pause