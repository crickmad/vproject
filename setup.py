import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['p.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="p.ico"
)

# SETUP CX FREEZE
setup(
    name = "ZIA",
    version = "1.0",
    description = "AI ",
    author = "Noob?Tech",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
