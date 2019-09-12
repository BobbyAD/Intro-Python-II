'''
    create item file
    let player hold list of items
    let room hold list of items

    player can pick up items out of current_room
    player can drop items in to current_room
'''

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"