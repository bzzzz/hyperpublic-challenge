TASKS = 98, 42, 23, 17, 3, 2
CORNER_CASES = None
P_INF = float("+inf")

def laziest_recur(total, available=TASKS):
    if total < 0:
        return P_INF
    elif total == 0:
        return 0

    l = len(available)

    if l > 1:
        if total >= available[0]:
            return min(
                1 + laziest_recur(total-available[0], available),
                laziest_recur(total, available[1:])
            )
        else:
            return laziest_recur(total, available[1:])
    elif l == 1:
        return 1 + laziest_recur(total-available[0], available)

def corner_cases(case):
    global CORNER_CASES

    if CORNER_CASES is None:
        CORNER_CASES = [laziest_recur(i) for i in xrange(196)]

    return CORNER_CASES[case]

def min_tasks_for(points):
    num_98, remaining = divmod(points, 98)
    return num_98 + corner_cases(remaining)


data = (("Doug", 2349), ("Jordan", 2102),
    ("Eric", 2001), ("Jon", 1747))

for staff, points in data:
    print staff, "had", points, "points; needed",\
        min_tasks_for(points), "tasks."
