def inclass(kls):
    """
    Decorator that adds the decorated function
    as a method in specified class
    """
    def _(func):
        setattr(kls,func.__name__, func)
        return func
    return _
