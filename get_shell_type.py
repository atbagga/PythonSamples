import os 

def _remove_cmd_chars(s):
    if isinstance(s, str):
        return s.replace("'", '_').replace('"', '_').replace('\r\n', ' ').replace('\n', ' ')
    return s


def _remove_symbols(s):
    if isinstance(s, str):
        for c in '$%^&|':
            s = s.replace(c, '_')
    return s


def _get_shell_type():
    # if 'ZSH_VERSION' in os.environ:
    #     return 'zsh'
    # elif 'BASH_VERSION' in os.environ:
    #     return 'bash'
    # elif 'KSH_VERSION' in os.environ or 'FCEDIT' in os.environ:
    #     return 'ksh'
    # elif 'WINDIR' in os.environ:
    #     return 'cmd'
    return _remove_cmd_chars(_remove_symbols(os.environ.get('SHELL')))



print(_get_shell_type())
print(os.environ)
