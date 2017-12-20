def color_2_grey(colors):
    return [[3 * [round(sum(cell)/len(cell))] for cell in row] for row in colors]
            
            