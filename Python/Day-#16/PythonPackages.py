# Python Package Index (Pypi) - 

# $ pip3 install PrettyTable
# Collecting PrettyTable
#   Downloading prettytable-2.1.0-py3-none-any.whl (22 kB)
# Requirement already satisfied: wcwidth in c:\users\nkrishnappa\appdata\roaming\python\python38\site-packages (from PrettyTable) (0.2.5)
# Installing collected packages: PrettyTable
# Successfully installed PrettyTable-2.1.0
# WARNING: You are using pip version 20.1.1; however, version 21.2.4 is available.
# You should consider upgrading via the 'c:\users\nkrishnappa\appdata\local\programs\python\python38-32\python.exe -m pip install --upgrade pip' command.

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander",])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table.align)
table.align = "l"
print(table.align)

"""
# table.field_names = ["Pokemon Name", "Type"]
# table.add_rows(
#     [
#         ["Pikachu", "Electric"],
#         ["Squirtle", "Water"],
#         ["Charmander", "Fire"],
#     ]
# )

{'Pokemon Name': 'c', 'Type': 'c'}
{'Pokemon Name': 'l', 'Type': 'l'}
+--------------+----------+
| Pokemon Name | Type     |
+--------------+----------+
| Pikachu      | Electric |
| Squirtle     | Water    |
| Charmander   | Fire     |
+--------------+----------+
"""

print(table)
