def conference_picker(cities_visited, cities_offered):
    matches = [city in cities_visited for city in cities_offered]
    if False in matches:
        return cities_offered[matches.index(False)]
    else:
        return 'No worthwhile conferences this year!'