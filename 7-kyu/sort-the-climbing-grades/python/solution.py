def sort_grades(lst):
    grades = ['VB', 'V0', 'V0+'] + ['V{}'.format(n) for n in range(1, 18)]
    return sorted(lst, key=lambda x: grades.index(x))