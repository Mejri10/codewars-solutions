humanMsgs = [
    "hello",
    "blip",
    'die stupid people',
    'your brain looks delicious',
    'try to find duplicated kata'
]

alienMsgs = [
    "]()]|_]|_]][-]|-|]",
    '{|^{|{{|_{]3{',
    '..[-.|_.|^....().[-.|^.__..|)...|.|^.|_|..~|~._\\~.__...[-..|.|)..',
    "'''_\\~'|_|'()'|''('|'|_'[-'|)''__'_\\~'/<'()'()'|_'''__'|\\|'|''/\\'/?']3'__''/?'|_|''()'`/''",
    '}/\\}~|~}/\\}/<}__}|)}}}[-}~|~}/\\}(}|}|_}|^}|_|}|)}__}|)}}}|\\|}|}/=}__}()}}}~|~}__}`/}/?}}~|~}'
]

def clear_msg(m):
    key = m[0]
    return  [alienLetter for alienLetter in m.split(key) if alienLetter][::-1]

# Construct dictionary with entries given in sample tests
dictionary = {}

for alienMsg, humanMsg in zip(alienMsgs, humanMsgs):
    for alienLetter, humanLetter in zip(clear_msg(alienMsg), humanMsg):
        dictionary[alienLetter] = humanLetter

# Complement dictionary through guesswork
dictionary['_T'] = 'j'
dictionary['><'] = 'x'
dictionary['\\/'] = 'v'
dictionary['~/_'] = 'z'
dictionary['\\/\\/'] = 'w'
dictionary['(_,'] = 'g'
dictionary['|\\/|'] = 'm'
dictionary['()_'] = 'q'

def decode(m):
    alienLetters = clear_msg(m)
    return ''.join(dictionary[letter] for letter in alienLetters)