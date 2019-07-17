### CODE PART 1 ###
from knack.prompting import prompt_pass
password = prompt_pass(msg="Password: ")
print(password)


### CODE PART 2 ###
# import getpass
# password = getpass.getpass(prompt="Password: ")
# print(password)

### CODE PART 3 ###
# import msvcrt
# def win_getpass(prompt='Password: ', stream=None):
#     """Prompt for password with echo off, using Windows getch()."""
#     for c in prompt:
#         msvcrt.putwch(c)
#     pw = ""
#     while 1:
#         c = msvcrt.getwch()
#         if c == '\r' or c == '\n':
#             break
#         if c == '\003':
#             raise KeyboardInterrupt
#         if c == '\b':
#             pw = pw[:-1]
#         else:
#             pw = pw + c
#     msvcrt.putwch('\r')
#     msvcrt.putwch('\n')
#     return pw


# password = win_getpass(prompt="Password: ")
# print(password)
