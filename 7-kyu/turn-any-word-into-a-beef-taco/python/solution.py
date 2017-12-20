def tacofy(word):
    recipe = dict(zip("aeioutlcgs",
                            ["beef"] * 5 +
                            ["tomato",
                            "lettuce",
                            "cheese",
                            "guacamole",
                            "salsa"]
                            )
                       )
    ingredients = [recipe[ch.lower()] for ch in word if ch.lower() in recipe]
    return  ["shell"] + ingredients + ["shell"]