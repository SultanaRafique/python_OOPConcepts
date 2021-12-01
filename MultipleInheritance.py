class CreaturePerson:
    def introduce(self):
        print("CreaturePerson")


class CreatureFish:
    def introduce(self):
        print("CreatureFish")


class Person(CreaturePerson):
    def introduce(self):
        print("Person")
        super().introduce()


class Fish(CreatureFish):
    def introduce(self):
        print("Fish")
        super().introduce()


class Mermaid(Person, Fish):
    def introduce(self):
        print("Mermaid")
        super().introduce()


mermaid = Mermaid()
mermaid.introduce()
