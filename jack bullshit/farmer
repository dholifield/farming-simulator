class Farmer:
    def __init__(self):
        self.money = 1000
        self.season = 'spring'
        self.crops = {'wheat': {'level': 1, 'yield': 10, 'cost': 50},
                      'corn': {'level': 1, 'yield': 20, 'cost': 100},
                      'soybeans': {'level': 1, 'yield': 30, 'cost': 150}}
        self.seasons_crops = {'spring': ['wheat', 'corn'],
                              'summer': ['corn', 'soybeans'],
                              'fall': ['soybeans', 'wheat'],
                              'winter': []}

    def change_season(self):
        if self.season == 'spring':
            self.season = 'summer'
        elif self.season == 'summer':
            self.season = 'fall'
        elif self.season == 'fall':
            self.season = 'winter'
        else:
            self.season = 'spring'
        print(f'The season has changed to {self.season}.')
        
    def harvest(self, crop_name):
        if crop_name in self.seasons_crops[self.season]:
            crop = self.crops[crop_name]
            yield = crop['yield'] * crop['level']
            self.money += yield
            print(f'You have harvested {yield} units of {crop_name}.')
            print(f'You now have {self.money} money.')
        else:
            print(f'{crop_name} cannot be harvested during {self.season} season.')

    def upgrade_crop(self, crop_name):
        if crop_name in self.seasons_crops[self.season]:
            crop = self.crops[crop_name]
            cost = crop['cost'] * crop['level']
            if self.money >= cost:
                self.money -= cost
                self.crops[crop_name]['level'] += 1
                print(f'You have upgraded {crop_name} to level {self.crops[crop_name]['level']}.')
                print(f'You now have {self.money} money.')
            else:
                print(f'You do not have enough money to upgrade {crop_name}.')
        else:
            print(f'{crop_name} cannot be upgraded during {self.season} season.')
