def list_animals(animals):
    return "".join(f"{i+1}. {animal}\n" for i, animal in enumerate(animals))