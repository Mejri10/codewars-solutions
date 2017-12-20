def mobile_keyboard(s):
    keystrokes = dict(zip("*#0123456789abcdefghijklmnopqrstuvwxyz",
                          "11111111111123423423423423423452342345"))
    return sum(int(keystrokes[i]) for i in s)