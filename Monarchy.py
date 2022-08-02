class Person:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        self.children = []
    
class Monarchy:
    def __init__(self, king):
        self.king = Person(king)
        self.__persons = {
            self.king.name: self.king
        }

    def birth(self, child_name, parent_name):
        parent = self.__persons[parent_name]
        new_child = Person(child_name)
        parent.children.append(new_child)
        self.__persons[child_name] = new_child

    def death(self, name):
        person = self.__persons[name]
        if person == None:
            return None
        person.is_alive = False

    def get_order_of_succession(self):
        order = []
        self.dfs(self.king, order)
        return order

    def dfs(self, current_person, order):
        if current_person.is_alive:
            order.append(current_person.name)
        for i in range(0, len(current_person.children)):
            self.dfs(current_person.children[i], order)

a = Monarchy("Jake")
a.birth("Catherine", "Jake")
a.birth("June", "Catherine")
a.birth("Farah", "June")
a.birth("Tom", "Jake")
a.birth("Celine", "Jake")
a.birth("Mark", "Catherine")
a.birth("Peter", "Celine")
b = a.get_order_of_succession()

for j in range(len(b)):
    print(b[j])
