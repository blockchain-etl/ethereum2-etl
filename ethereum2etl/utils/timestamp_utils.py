from datetime import datetime


def format_timestamp(ts):
    if ts is None:
        return None

    if isinstance(ts, int):
        ts = datetime.fromtimestamp(ts)

    return ts.strftime('%Y-%m-%dT%H:%M:%SZ')