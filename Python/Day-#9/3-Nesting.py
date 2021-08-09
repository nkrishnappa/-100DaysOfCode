'''
{
    key: [List],
    key2: {Dict},
    key3: string,
    key4: int/float
    ...
}


'''
# Nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

# Nesting a List in a Dictionary
travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berling", "Hamburg", "Stuttagart"]
}

# Nesting a Dictionary in Dictionary
travel_log = {
    "France" : {
        "cities_visited" : ["Paris", "Lille", "Dijon"]
    },
    "Germany" : ["Berling", "Hamburg", "Stuttagart"]
}

travel_log = {
    "France" : {
        "cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits": 12
    },
    "Germany" : {
        "cities_visited" : ["Berling", "Hamburg", "Stuttagart"], "total_visits" : 5
    }
}

# Nesting a Dictionary inside  a List
travel_log = [
    { 
        "country" : "France",
        "cities_visited" : ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country" : "Germany",
        "cities_visited" : ["Berling", "Hamburg", "Stuttagart"],
        "total_visits" : 5
    }
]

# print(travel_log[0]["country"])



