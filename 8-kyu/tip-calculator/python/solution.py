from math import ceil

def calculate_tip(amount, rating):
    try:
        return ceil(amount * {'terrible': 0,'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}[rating.lower()])
    except KeyError:
        return 'Rating not recognised'