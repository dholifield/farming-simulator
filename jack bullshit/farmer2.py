class Farmer:
    def __init__(self):
        self.money = 1000
        self.crops = {'wheat': {'level': 1, 'yield': 10, 'cost': 50},
                      'corn': {'level': 1, 'yield': 20, 'cost': 100},
                      'soybeans': {'level': 1, 'yield': 30, 'cost': 150}}
                     
    def harvest(self, crop_name):
        crop = self.crops[crop_name]
        yield = crop['yield'] * crop['level']
        self.money += yield
        print(f'You have harvested {yield} units of {crop_name}.')
        print(f'You now have {self.money} money.')
        
    def upgrade_crop(self, crop_name):
        crop = self.crops[crop_name]
        cost = crop['cost'] * crop['level']
        if self.money >= cost:
            self.money -= cost
            self.crops[crop_name]['level'] += 1
            print(f'You have upgraded {crop_name} to level {self.crops[crop_name]['level']}.')
            print(f'You now have {self.money} money.')
        else:
            print(f'You do not have enough money to upgrade {crop_name}.')

# Example usage:
farmer = Farmer()
farmer.harvest('wheat')
farmer.upgrade_crop('wheat')
farmer.harvest('wheat')