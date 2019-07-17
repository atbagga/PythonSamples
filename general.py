"""
this is doc string
"""
import os

def get_repo_root():
        """Returns the path to the source code root directory"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        import pdb
        pdb.set_trace()

        files = os.listdir(recordings_folder)
        if files:
            print('Number of recordings found - {}'.format(len(files))
            # for cur_file in files:
            #     print('Deleting file - {}'.format(cur_file))

        while not os.path.exists(os.path.join(current_dir, 'CONTRIBUTING.md')):
            current_dir = os.path.dirname(current_dir)

        return current_dir


string1 = None
string2 = None

if not string1 and not string2:
    print('not string 1')
else:
    print('string 1')


get_repo_root()


# import collections

# d1 = collections.OrderedDict()
# devops_org = 'https://dev.azure.com/miprotocolbugbash'

# d1[devops_org] = 'my org'
# d1['b'] = 'B'
# d1['c'] = 'C'
# d1['d'] = 'D'
# d1['e'] = 'E'

# if (devops_org not in d1):
#     print("no command")

# print(d1[devops_org])

# abc = 'this is is a long string' \
#       'and this is part of it'


# abca = ('this is is a long string' 
#       'and this is part of it too')

# print(abc)
# print(abca)

# ARG = {'a':'b', 'c':'d'}

# print(ARG.get('a', None))
# print(ARG.get('b', None))
# print(ARG.get('c', None))



# def print_kwargs(argv):
#     if argv:
#         print(argv[0])
#     else:
#         print('No Argv')


# kwargs = {'command':'devops', 'commands':'devopss'}

# if (kwargs.get('command', None) and kwargs['command'].startswith(('devops', 'boards', 'artifacts', 'pipelines', 'repos'))):
#     if ('command' not in kwargs):
#         print("no command")
#     print_kwargs(kwargs['command'].split())




# A = True
# B = False
# c = True
# D = True
# e = True
# f = True
# g = True

# if (A or B or c or D or e or f or g): # pylint: disable=too-many-boolean-expressions 
#     print('Success')

# if (A or B or c or D or e or f):
#     print('Success')
