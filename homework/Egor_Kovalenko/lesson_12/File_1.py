class Flower:
    def __init__(self, color, stem_length, cost, lifetime):
        self.color = color
        self.stem_length = stem_length
        self.cost = cost
        self.lifetime = lifetime


class Rose(Flower):
    def __init__(self, color, stem_length, cost, lifetime, name):
        super().__init__(color, stem_length, cost, lifetime)
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


class Lily(Flower):
    def __init__(self, color, stem_length, cost, lifetime, name):
        super().__init__(color, stem_length, cost, lifetime)
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        return self.flowers.append(flower)

    def calc_avg_lifetime(self):
        total_lifetime = sum(flower.lifetime for flower in self.flowers)
        avg_fresh = total_lifetime / len(self.flowers)
        return avg_fresh

    def sort_by_params(self, attribute):
        return sorted(self.flowers, key=lambda flower: getattr(flower, attribute))

    def search_by_lifetime(self, lifetime):
        return [flower for flower in self.flowers if flower.lifetime == lifetime]


rose = Rose('red', 23, 103, 12, 'Rose')
lyli = Lily('white', 10, 133, 15, 'Lily')

bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(lyli)

print(bouquet.sort_by_params('stem_length'))
print(bouquet.search_by_lifetime(15))
