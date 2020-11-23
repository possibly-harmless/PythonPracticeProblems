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
