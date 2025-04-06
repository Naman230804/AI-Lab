class Person:
    def _init_(self, name):
        self.name = name
        self.parents = []
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parents.append(self)

    def get_parents(self):
        return [parent.name for parent in self.parents]

    def get_children(self):
        return [child.name for child in self.children]

    def get_siblings(self):
        siblings = set()
        for parent in self.parents:
            siblings.update(parent.children)
        siblings.discard(self)
        return [sibling.name for sibling in siblings]

class FamilyTree:
    def _init_(self):
        self.members = {}

    def add_member(self, name):
        if name not in self.members:
            self.members[name] = Person(name)

    def add_relationship(self, parent_name, child_name):
        if parent_name in self.members and child_name in self.members:
            self.members[parent_name].add_child(self.members[child_name])
            print(f"Relationship added: {parent_name} -> {child_name}")
        else:
            print("Error: One or both members not found.")

    def get_ancestors(self, name, ancestors=None):
        if ancestors is None:
            ancestors = set()
        if name in self.members:
            for parent in self.members[name].parents:
                ancestors.add(parent.name)
                self.get_ancestors(parent.name, ancestors)
        return ancestors

    def interactive_menu(self):
        while True:
            print("\nFamily Tree Menu:")
            print("1. Add a parent-child relationship")
            print("2. Query a person's parents")
            print("3. Query a person's children")
            print("4. Query a person's siblings")
            print("5. Query a person's ancestors")
            print("6. Exit")
            
            choice = input("Choose an option: ")
            
            if choice == "1":
                parent = input("Enter the parent's name: ")
                child = input("Enter the child's name: ")
                self.add_member(parent)
                self.add_member(child)
                self.add_relationship(parent, child)
            elif choice == "2":
                name = input("Enter the person's name: ")
                if name in self.members:
                    print(f"Parents of {name}: {self.members[name].get_parents()}")
                else:
                    print("Person not found.")
            elif choice == "3":
                name = input("Enter the person's name: ")
                if name in self.members:
                    print(f"Children of {name}: {self.members[name].get_children()}")
                else:
                    print("Person not found.")
            elif choice == "4":
                name = input("Enter the person's name: ")
                if name in self.members:
                    print(f"Siblings of {name}: {self.members[name].get_siblings()}")
                else:
                    print("Person not found.")
            elif choice == "5":
                name = input("Enter the person's name: ")
                if name in self.members:
                    print(f"Ancestors of {name}: {self.get_ancestors(name)}")
                else:
                    print("Person not found.")
            elif choice == "6":
                print("Exiting program.")
                break
            else:
                print("Invalid option. Please choose a valid number.")

# Run the interactive menu
family = FamilyTree()
family.interactive_menu()