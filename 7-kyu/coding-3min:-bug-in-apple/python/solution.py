def sc(apple):
    return list([(i,apple[i].index('B')) for i in range(len(apple)) if 'B' in apple[i]][0]) 
