class Pokemon:
    def __init__(self, name, type, abilities, height, weight, image):
        self.name = name
        self.type = type
        self.abilities = abilities
        self.height = height
        self.weight = weight
        self.image = image

    def __str__(self):
        return f"{self.name} ({self.type}) [{self.height}m, {self.weight}kg] - {self.abilities} - {self.image}"
