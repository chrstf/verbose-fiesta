from babble import post
from babble.exceptions import ErrorMessage
from babble import progressbar
from time import sleep


def test():
    msg = 'Hello world!'
    post.message(msg)
    for color in post.BColors.__dict__.keys():
        if color in ['__module__', '__dict__', '__weakref__', '__doc__']:
            continue
        post.message(f'{msg}: {color}', c=color)
    post.warning_m(f'{msg}: warning')
    try:
        post.error_m(f'{msg}: error')
    except ErrorMessage:
        post.message('Error caught')

    # progress bar
    rng = 5
    for i in range(rng):
        progressbar.progress_bar(i, rng)
        sleep(1)

    return None


if __name__ == '__main__':
    test()
