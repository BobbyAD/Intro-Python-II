# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item
class Player:
    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = items
    
    def move(self, d):
        if d == 'n' and self.current_room.n_to:
            self.current_room = self.current_room.n_to
            return f"You are now in {self.current_room}"
        elif d == 's' and self.current_room.s_to:
            self.current_room = self.current_room.s_to
            return f"You are now in {self.current_room}"
        elif d == 'e' and self.current_room.e_to:
            self.current_room = self.current_room.e_to
            return f"You are now in {self.current_room}"
        elif d == 'w' and self.current_room.w_to:
            self.current_room = self.current_room.w_to
            return f"You are now in {self.current_room}"
        else:
            return "There is no room in that direction"

    def pickup(self, item):
        self.items.append(item)
        self.current_room.items.remove(item)
        print_list = "\n".join([i.__str__() for i in self.items])
        print(f"\nYou have:\n{print_list}\n")
    
    def drop(self, item):
        self.current_room.items.append(item)
        self.items.remove(item)
        print_list = "\n".join([i.__str__() for i in self.items])
        print(f"\nYou have:\n{print_list}\n")

    def check_inventory(self):
        print_list = "\n".join([i.__str__() for i in self.items])
        print(f"\nYou have:\n{print_list}\n")