import numpy as np
from os import get_terminal_size


_columns = get_terminal_size().columns  # for log messages


def progress_bar(current: int, list_len: int, lead: str = "",
                 verbose: int = True, at_v_level: int = 1):
    """
    Progress bar.
    :param current: current list index.
    :param list_len: Length of the list.
    :param columns: Number of terminal columns.
    :param lead: Leading string.
    :param verbose: Verbose output.
    :param at_v_level: At which verbosity level the progress bar should be printed.
    """
    symbol = "█"
    bar_end = "\r"
    if verbose != at_v_level:
        return None
    lead += f" {((float(current) + 1) / float(list_len)) * 100:5.1f} %"
    to_substract = len(lead)
    bar_range = np.linspace(0, _columns - (to_substract+1), list_len, endpoint=True)
    bar = f"{lead} {symbol * (int(bar_range[current])-1)}"
    if (current + 1) == list_len:
        bar_end = "\n"
    print(f"{bar}{' ' * (_columns - len(bar) - 1)}|", end=bar_end)
