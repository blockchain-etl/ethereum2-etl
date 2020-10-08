from datetime import datetime

GENESIS_TIME = 1596546008
SECONDS_PER_SLOT = 12
SLOTS_PER_EPOCH = 32


def compute_timestamp_at_slot(slot):
    if slot is None:
        return None

    timestamp = GENESIS_TIME + int(slot) * SECONDS_PER_SLOT
    return timestamp


def compute_slot_at_timestamp(ts):
    if ts is None:
        return None

    slot_with_fractions = compute_slot_with_fractions_at_timestamp(ts)
    return int(slot_with_fractions)


def compute_slot_with_fractions_at_timestamp(ts):
    if ts is None:
        return None

    if isinstance(ts, datetime):
        ts = ts.timestamp()

    slot = (ts - GENESIS_TIME) / SECONDS_PER_SLOT
    return slot


def compute_epoch_at_slot(slot):
    """
    Return the epoch number at ``slot``.
    """
    return slot // SLOTS_PER_EPOCH


def compute_epoch_at_timestamp(ts):
    slot = compute_slot_at_timestamp(ts)
    epoch = compute_epoch_at_slot(slot)
    return epoch
