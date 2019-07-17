import subprocess, os, platform

def open_file(filepath):
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filepath)
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))

inputstring = ''

if inputstring is not None and inputstring.lower() == 'true':
    open_file("open_file.py")
else:
    print("open_file.py")