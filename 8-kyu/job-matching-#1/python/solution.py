def match(candidate, job):
    return 0.9*candidate['min_salary'] <= job['max_salary']