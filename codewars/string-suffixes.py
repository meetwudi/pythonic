def len_common_prefix(str_a, str_b):
    minlen = min(len(str_a), len(str_b))
    for i in reversed(xrange(1, minlen+1)):
        if (str_a[:i] == str_b[:i]):
            return i
    return 0


def string_suffix(str_):
    slen = len(str_)
    substrs = [str_[i:] for i in xrange(0, slen)]
    return sum([len_common_prefix(substr, str_) for substr in substrs])
