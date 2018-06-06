"""
    Memoization: Caching computed values in order to avoid repeated costly computations
"""


def costly_computation(x):
    # compute a long Time
    return 42


def cached_compute(x, _cache={}):
    if x not in _cache:
        _cache[x] = costly_computation(x)

    return _cache[x]