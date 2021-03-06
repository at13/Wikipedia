import functools

def debug(fn):
    def wrapper(*args, **kwargs):
        print fn.__name__, "called with args:\n", str(args) + str(kwargs), "\n"
        res = fn(*args, **kwargs)
        print "\nreturning:", res, "\n\n"
        return res
    return wrapper


class cache(object):

    def __init__(self, fn):
        self.fn = fn
        self._cache = {}
        functools.update_wrapper(self, fn)

    def __call__(self, *args, **kwargs):
        key = str(args) + str(kwargs)
        if key in self._cache:
            ret = self._cache[key]
        else:
            ret = self._cache[key] = self.fn(*args, **kwargs)

        return ret
    
    def clear_cache(self):
        self._cache = {}       
