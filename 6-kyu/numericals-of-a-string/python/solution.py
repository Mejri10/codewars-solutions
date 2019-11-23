def numericals(s):
    ans, seen = [], {}
    for c in s:
        count = seen.get(c, 1)
        ans.append(str(count))
        seen[c] = count + 1
    return ''.join(ans)
    