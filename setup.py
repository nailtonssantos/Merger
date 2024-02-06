import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("mergerPDF.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = ["logo.jpg"],
        excludes = []
)




setup(
    name = "JuntarPDF",
    version = "2.0",
    description = "Junte PDFs de maneira rápida e fácil",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
