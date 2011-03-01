def friends(userstring):
    return [i for i, isfriend in enumerate(userstring)
            if isfriend == "X"]

def read_userstrings(file_):
    users = []
    with open(file_) as f:
        for line in f:
            users.append(friends(line))

    return users

def calc_influence(id_):
    global friends_of, influences

    influence = 0

    for friend in friends_of[id_]:
        if influences[friend] is None:
            influence += calc_influence(friend)
        else:
            influence += influences[friend]
        influence += 1

    influences[id_] = influence
    return influence

friends_of = read_userstrings("challenge2input.txt")
influences = [None] * len(friends_of)

for id_ in xrange(len(influences)):
    calc_influence(id_)

influences = sorted(list(enumerate(influences)),
    cmp=lambda x,y: 1 if x[1]>y[1] else 0 if x[1]==y[1] else -1,
    reverse=True)

for user, influence in influences[0:3]:
    print "User #%d, influence %s: %s" % (user, influence, friends_of[user])
