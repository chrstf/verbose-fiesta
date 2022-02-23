import numpy as np
from os import get_terminal_size


_columns = get_terminal_size().columns  # for log messages


def progress_bar(current: int, list_len: int, lead: str = "",
                 verbose: int = 0, verbose_level_threshold: int = 1):
    """
    Progress bar.
    :param current: current list index.
    :param list_len: Length of the list.
    :param lead: Leading string.
    :param verbose: Verbose output.
    :param verbose_level_threshold: This hurdle needs to be overcome in oder to get verbose
    """
    symbol = "█"
    bar_end = "\r"
    if verbose == 0:
        return None

    if verbose < verbose_level_threshold:
        return None

    lead += f" {((float(current) + 1) / float(list_len)) * 100:5.1f} %"
    to_substract = len(lead)
    bar_range = np.linspace(0, _columns - (to_substract+1), list_len, endpoint=True)
    bar = f"{lead} {symbol * (int(bar_range[current])-1)}"
    if (current + 1) == list_len:
        bar_end = "\n"
    print(f"{bar}{' ' * (_columns - len(bar) - 1)}|", end=bar_end)
