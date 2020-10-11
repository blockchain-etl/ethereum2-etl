def to_int(val):
    if val is None:
        return val
    if val == b'':
        return 0
    if isinstance(val, bytes):
        return int.from_bytes(val, 'big')
    if isinstance(val, str):
        return int(val)

    return val