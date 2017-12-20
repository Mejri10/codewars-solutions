def answer(question, information):
    scores = [sum([word.lower() in info.lower().split() for word in question.split()]) for info in information]
    return information[scores.index(max(scores))] if max(scores) else None