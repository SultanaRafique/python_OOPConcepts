class Creature:
    def introduce(self):
        print("Creature")


class Person(Creature):
    def introduce(self):
        print("Person")
        super().introduce()


class Fish(Creature):
    def introduce(self):
        print("Fish")
        super().introduce()


class Mermaid(Person, Fish):
    def introduce(self):
        print("Mermaid")
        super().introduce()


mermaid = Mermaid()
mermaid.introduce()