def validate_hello(greetings):
    foreign_greetings = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    return any(greeting in greetings.lower() for greeting in foreign_greetings)