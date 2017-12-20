def find_number_in_string(s):
    return filter(lambda x: x.isdigit(), s)

def order(sentence):
    return ' '.join(sorted(sentence.split(), key=find_number_in_string))