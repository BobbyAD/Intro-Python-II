# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
    def move(self, d):
        if d == 'n' and self.current_room.n_to:
            self.current_room = self.current_room.n_to
            return f"You are now in {self.current_room.name}.\n{self.current_room.description}"
        elif d == 's' and self.current_room.s_to:
            self.current_room = self.current_room.s_to
            return f"You are now in {self.current_room.name}.\n{self.current_room.description}"
        elif d == 'e' and self.current_room.e_to:
            self.current_room = self.current_room.e_to
            return f"You are now in {self.current_room.name}.\n{self.current_room.description}"
        elif d == 'w' and self.current_room.w_to:
            self.current_room = self.current_room.w_to
            return f"You are now in {self.current_room.name}.\n{self.current_room.description}"
        else:
            return "There is no room in that direction"
