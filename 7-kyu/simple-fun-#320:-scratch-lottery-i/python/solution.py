def scratch(lottery):
    res = 0
    for ticket in lottery:
        elems = ticket.split()
        if elems.count(elems[0]) == 3:
            res += int(elems[-1])
    return res