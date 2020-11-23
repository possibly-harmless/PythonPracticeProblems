# Note that the performance of the solutions below will not be great,
# since we use python lists here, while linked lists would be a better
# structure to use for such recursive solutions.
#
# Note also that such implementations are prone to stack overflow, since
# when recursion is used as a substitute for a loop, the recursion depth
# can become pretty large.

# 1.A.1 - List filtering
def list_filter(lst, pred):
    if not lst:
        return []
    fst, *rest = lst
    if pred(fst):
        return [fst] + list_filter(rest, pred)
    else:
        return list_filter(rest, pred)


# 1.A.2 - Consecutive elements runs lengths
def count_runs(lst):
    if not lst:
        return []
    else:
        fst, *rest = lst
        for index, elem in enumerate(rest):
            if elem != fst:
                return [index + 1] + count_runs(rest[index:])
        return [len(lst)]


# 1.A.3 - Positions of a subsequence in a list
def sequence_position(lst, seq, start=0):
    if not seq or not lst or len(seq) > len(lst) - start:
        return []
    if lst[start : len(seq) + start] == seq:
        return [start] + sequence_position(lst, seq, start + 1)
    else:
        return sequence_position(lst, seq, start + 1)