# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Fish:
    def __init__(self, name: str, habitat: str, habitat_depth: int):
        self.name = name
        self.habitat = habitat
        self.habitat_depth = habitat_depth

    def fish_features(self):
        return self.habitat_depth


class Bird:
    def __init__(self, name: str, habitat: str, wingspan: int):
        self.name = name
        self.habitat = habitat
        self.wingspan = wingspan

    def bird_features(self):
        return self.wingspan


class Reptile:
    def __init__(self, name: str, habitat: str, body_temperature: int):
        self.name = name
        self.habitat = habitat
        self.body_temperature = body_temperature

    def reptile_features(self):
        return self.body_temperature


fishes = Fish('Salmon', 'Atlantic ocean', 15)
birds = Bird('Eagle', 'Caucasus', 3)
reptiles = Reptile('Salamander', 'South Europe', 22)


if __name__ == '__main__':
    print(fishes.fish_features())
    print(birds.bird_features())
    print(reptiles.reptile_features())
