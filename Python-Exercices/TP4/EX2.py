def pair(*args) :
    if not args :
        return None
    return [c for c in args if c%2==0]
