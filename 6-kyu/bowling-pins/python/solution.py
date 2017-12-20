def bowling_pins(arr):
    mapping = {1: 27,2: 18,3: 20,4: 9,5: 11,6: 13,7: 0,8: 2,9: 4,10: 6}
    template = list("I I I I\n I I I \n  I I  \n   I   ")
    for idx in arr:
        template[mapping[idx]] =  ' '
    return ''.join(template)