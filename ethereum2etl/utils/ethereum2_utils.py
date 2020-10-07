GENESIS_TIME = 1596546008
SECONDS_PER_SLOT = 12


def slot_to_timestamp(slot):
    if slot is None:
        return None

    # timestamp = genesisTime + slot * SECONDS_PER_SLOT
    timestamp = GENESIS_TIME + int(slot) * SECONDS_PER_SLOT
    return timestamp


def timestamp_to_slot(ts):
    if ts is None:
        return None
    # slot = (timestamp - genesisTime) / SECONDS_PER_SLOT
    slot = (ts - GENESIS_TIME) / SECONDS_PER_SLOT
    return slot
