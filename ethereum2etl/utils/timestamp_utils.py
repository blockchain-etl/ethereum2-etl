from datetime import datetime, timezone


def format_timestamp(ts):
    if ts is None:
        return None

    if isinstance(ts, int):
        ts = datetime.fromtimestamp(ts, tz=timezone.utc)

    return ts.strftime('%Y-%m-%dT%H:%M:%SZ')