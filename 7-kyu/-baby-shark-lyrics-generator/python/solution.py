def baby_shark_lyrics():
    subs = ["Baby shark","Mommy shark","Daddy shark","Grandma shark","Grandpa shark","Let's go hunt"]
    doo = lambda s: "\n".join([f"{s}, doo doo doo doo doo doo"]*3+[f"{s}!"])
    return "\n".join([*[doo(s) for s in subs], "Run away,…"])
    

    