def restock(current, addend, cap=100):
    if addend < 0:
        raise ValueError("cannot restock negative")
    return min(current + addend, cap)
