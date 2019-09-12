# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        print_list = "\n".join([i.__str__() for i in self.items])
        print_str = ""
        if len(self.items) > 0:
            print_str = f"{self.name}\n\n{self.description}\n\nYou can see some items:\n{print_list}\n"
        else:
            print_str = f"{self.name}\n\n{self.description}\n"
        return print_str

    n_to = ''
    s_to = ''
    e_to = ''
    w_to = ''