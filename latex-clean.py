import os
import re
import argparse

extensions = [
    "\.aux$", 
    "\.bbl$", 
    "\.bcf$", 
    "\.blg$", 
    "\.fdb_latexmk$", 
    "\.fls$", 
    "\.log$", 
    "\.run\.xml$", 
    "\.gz$"
    ]

ext_string = ", ".join(extensions)

parser = argparse.ArgumentParser(description=('Clean a LaTeX build directory of aux files. Currently removes the following files: ' + ext_string))
parser.add_argument("dir", help='Directory to be cleaned. Defaults to the current directory.', nargs='?', default=os.getcwd())
args = parser.parse_args()

dir = args.dir

files = os.listdir(dir)

for file in files:
    file = os.path.join(dir, file)
    for ext in extensions:
        if re.search(ext, file):
            os.remove(file)
            extensions.remove(ext)
            break

print("Directory '", args.dir, "' cleaned of additional LaTeX files", sep = '')
