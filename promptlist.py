import sys

from knack.log import get_logger
from knack.prompting import NoTTYException, verify_is_a_tty, prompt

logger = get_logger(__name__)


def _delete_last_line():
    "Use this function to delete the last line in the STDOUT"
    # cursor up one line
    sys.stdout.write('\x1b[1A')
    # delete last line
    sys.stdout.write('\x1b[2K')


def delete_last_n_lines(n):
    "Use this function to delete the last 'n' lines in the STDOUT"
    from colorama import init, deinit
    init()
    for _x in range(0, n):
        _delete_last_line()
    deinit()


def prompt_user_friendly_choice_list(msg, a_list, help_string=None):
    """Prompt user to select from a list of possible choices.
    :param msg: A message displayed to the user before the choice list
    :type msg: str
    :param a_list: The list of choices (list of strings or list of dicts with 'name' & 'desc')
    "type a_list: list
    :param help_string: Help message to be displayed on the input terminal
    :type help_string: str
    :returns: The list index of the item chosen.
    """
    PAGE_SIZE = 30
    allowed_vals = list(range(1, len(a_list) + 1))

    num_pages = 1
    last_page_full = True
    if len(a_list) % PAGE_SIZE == 0:
        num_pages = int(len(a_list)/PAGE_SIZE)
    else:
        num_pages = int(len(a_list)/PAGE_SIZE) + 1
        last_page_full = False
    printed_page_id = 1
    while True:
        # Handle last page 
        lines_to_print = PAGE_SIZE
        if printed_page_id == num_pages and not last_page_full:
            lines_to_print = len(a_list) % PAGE_SIZE
        lines_to_delete = lines_to_print
        page_start = (printed_page_id - 1) * PAGE_SIZE
        options = _get_options(display_list=a_list, size=lines_to_print, starting_index=page_start)
        print(msg)
        print(options)
        if num_pages > 1:
            print('...showing page {} of {}, press Enter for next page...'.format(printed_page_id, num_pages))
            lines_to_delete = lines_to_print + 1
        val = prompt('Please enter a choice: ')
        if val == '?' and help_string is not None:
            delete_last_n_lines(lines_to_delete + 2)
            if num_pages > 1:
                print('...showing page {} of {}, press Enter for next page...'.format(printed_page_id, num_pages))
                lines_to_delete = lines_to_print + 1
            print('Please enter a choice: {}'.format('?'))
            print(help_string)
            continue
        if not val:
            delete_last_n_lines(lines_to_delete + 2)
            if num_pages > 1:
                printed_page_id = printed_page_id + 1
                if printed_page_id != num_pages:
                    printed_page_id = printed_page_id % num_pages
            continue
        try:
            ans = int(val)
            if ans in allowed_vals:
                delete_last_n_lines(lines_to_delete + 1)
                print('Please enter a choice: {}'.format(a_list[ans - 1]))
                print('')
                # array index is 0-based, user input is 1-based
                return ans - 1
            raise ValueError
        except ValueError:
            delete_last_n_lines(lines_to_delete + 2)
            print('Please enter a choice: {}'.format(val))
            logger.warning('Valid values are %s', allowed_vals)


def _get_options(display_list, size, starting_index):
    return '\n'.join([' [{}] {}{}'
                         .format(i + starting_index + 1,
                                 x['name'] if isinstance(x, dict) and 'name' in x else x,
                                 ' - ' + x['desc'] if isinstance(x, dict) and 'desc' in x else '')
                         for i, x in enumerate(display_list[starting_index:starting_index + size])])


mylist = [x+1 for x in range(500)]
prompt_user_friendly_choice_list("Hello World", mylist, help_string="Help message is this.")
