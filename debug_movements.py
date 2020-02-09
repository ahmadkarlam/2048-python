import json
from terminaltables import AsciiTable

with open('movements.json') as json_file:
    movements = json.load(json_file)

    print("--------------------------------------------------------------------------------")
    for i in range(0, len(movements)):
        movement = movements[i]
        movement["numbers"].insert(0, [0, 1, 2, 3])
        print("key: ", movement["key"])
        print("random location: ", movement["random_location"])
        print("random number: ", movement["random_number"])
        table = AsciiTable(movement["numbers"])
        table.padding_left = 4
        table.padding_right = 4
        print(table.table)
        print("--------------------------------------------------------------------------------")
