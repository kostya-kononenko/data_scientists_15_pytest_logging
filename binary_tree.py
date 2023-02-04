class Tree:

    def __init__(self, id_n):
        self.id_n = id_n
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_n)

    def add_from_list(self, lst):
        for id_n in lst:
            self.insert_new_item(id_n)

    def insert_new_item(self, id_n):
        if self.id_n:
            if id_n < self.id_n:
                if self.left is None:
                    self.left = Tree(id_n)
                else:
                    self.left.insert_new_item(id_n)
            elif id_n > self.id_n:
                if self.right is None:
                    self.right = Tree(id_n)
                else:
                    self.right.insert_new_item(id_n)
        else:
            self.id_n = id_n

    def find(self, find_value):
        if find_value < self.id_n:
            if self.left is None:
                return str(find_value) + " Not Found"
            return self.left.find(find_value)
        elif find_value > self.id_n:
            if self.right is None:
                return str(find_value) + " Not Found"
            return self.right.find(find_value)
        else:
            print(str(self.id_n) + ' is found')

    def check_my_node(self, find_value):
        if not find_value:
            return None
        if find_value < self.id_n:
            if self.left is None:
                return False
            return bool(self.left.check_my_node(find_value))
        elif find_value > self.id_n:
            if self.right is None:
                return False
            return bool(self.right.check_my_node(find_value))
        else:
            return bool(self)

    def print_my_tree(self):
        if self.left:
            self.left.print_my_tree()
        print(self.id_n),
        if self.right:
            self.right.print_my_tree()

    def find_min_node(self):
         if self.left is None:
             return self.id_n
         return self.left.find_min_node()

    def find_max_node(self):
         if self.right is None:
             return self.id_n
         return self.right.find_max_node()

    def delete_some_node(self, node):
        if self is None:
            return self
        if node < self.id_n:
            self.left = self.left.delete_some_node(node)
            return self
        if node > self.id_n:
            self.right = self.right.delete_some_node(node)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        element = self.right
        while self.find_min_node.left:
            element = element.left
        self.id_n = element.id_n
        self.right = self.right.delete_some_node(element.id_n)
        return self