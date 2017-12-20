def rain_amount(mm):
    if (mm < 40):
        return "You need to give your plant %smm of water" % (40 - mm)
    else:
        return "Your plant has had more than enough water for today!"