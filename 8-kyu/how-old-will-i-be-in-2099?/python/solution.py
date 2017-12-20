def calculate_age(year_of_birth, current_year):
    elapsed_years = current_year - year_of_birth
    if elapsed_years > 0:
        return "You are {} year{} old.".format(elapsed_years, 's' if elapsed_years > 1 else '')
    elif elapsed_years < 0:
        return "You will be born in {} year{}.".format(-elapsed_years, 's' if -elapsed_years > 1 else '')
    else:
        return "You were born this very year!"