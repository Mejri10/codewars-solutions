def lyrics():
    result = []
    for i in range(99, 2, -1):
        result.append(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        result.append(f"Take one down and pass it around, {i - 1} bottles of beer on the wall.")
    
    result.append("2 bottles of beer on the wall, 2 bottles of beer.")
    result.append("Take one down and pass it around, 1 bottle of beer on the wall.")
    result.append("1 bottle of beer on the wall, 1 bottle of beer.")
    result.append("Take one down and pass it around, no more bottles of beer on the wall.")
    result.append("No more bottles of beer on the wall, no more bottles of beer.")
    result.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
    return "\n".join(result)

def HQ9(code):
    return {
        "H": "Hello World!",
        "Q": code,
        "9": lyrics()
    }.get(code, None)