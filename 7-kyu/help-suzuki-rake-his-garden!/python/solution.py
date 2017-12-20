def rake_garden(garden):
    garden = garden.split()
    return ' '.join([item if item in ['gravel','rock'] else 'gravel' for item in garden])