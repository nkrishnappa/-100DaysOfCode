# def greet(name):
#     print(f"Hello {name}")
#     print(f"How fo you do {name}")
#     print(f"isn't the weather is nice today")

# # Function Arguments
# # parameter : name 
# # arguments : Nandisha
# greet("Nandisha")

def greet_with(name: str, location: str) -> None:
    print(f"Hello {name}")
    print(f"How fo you do {name}")
    print(f"isn't the {location} weather is nice today?")

# greet_with("Nandisha", "London")
greet_with(name="Nandisha", location="London")