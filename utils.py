def clamp(v, lo, hi):
    return max(lo, min(hi, v))


def parse_args(raw):
    return [a.strip() for a in raw.split(',') if a.strip()]
