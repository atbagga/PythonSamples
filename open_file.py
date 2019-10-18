import subprocess, os, platform

def open_file(filepath):
    """
    Opens a file in the default editor for the file type and exits.
    """
    import subprocess
    import platform
    import os
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':    # Windows
        # disable pylint warning since we run pylint on linux agent and startfile is a windows only function
        os.startfile(filepath)  # pylint: disable=no-member
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))

open_file('a.xyz')