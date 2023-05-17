def pair(*arg) :
    if not arg :
        return None
    return [c for c in arg if c%2==0]
