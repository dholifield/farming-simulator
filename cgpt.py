# Farm game

class Farm:
    def __init__(self):
        self.crops = []
        
    def plant(self, crop):
        self.crops.append(crop)
        print("You have planted a", crop)
        
    def harvest(self):
        if len(self.crops) > 0:
            print("You have harvested the following crops:")
            for crop in self.crops:
                print(crop)
            self.crops = []
        else:
            print("There are no crops to harvest.")
            
    def status(self):
        if len(self.crops) > 0:
            print("Your farm has the following crops planted:")
            for crop in self.crops:
                print(crop)
        else:
            print("Your farm has no crops planted.")

# Main game loop
farm = Farm()
while True:
    print("Welcome to your farm!")
    print("1. Plant a crop")
    print("2. Harvest crops")
    print("3. Check farm status")
    print("4. Exit game")
    choice = input("What would you like to do? ")
    if choice == "1":
        crop = input("What crop would you like to plant? ")
        farm.plant(crop)
    elif choice == "2":
        farm.harvest()
    elif choice == "3":
        farm.status()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")