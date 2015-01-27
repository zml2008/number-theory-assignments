__author__ = 'zml'


class gathering_input(object):
    """
    Decorator to be used on methods that require a single int as user input.
    Example:

    @gathering_input
    """
    def __init__(self, prompt="Pick a number: "):
        self.prompt = prompt

    def __call__(self, f):
        def func(*args, **kwargs):
            if len(args) > 0:
                num = args[0]
                args = args[1:]
            else:
                num = int(input(self.prompt))

            return f(num, *args, **kwargs)
        return func


def factors(num):
    ret = set()
    for i in range(1, num):
        if num % i == 0:
            ret.add(i)
    ret.add(num)
    return ret