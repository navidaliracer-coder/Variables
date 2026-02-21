class flashcard:
    def __init__(self, Character, Role):
        self.Character = Character
        self.role = Role
    def __str__(self):

        return self.Character+' ( '+self.Character+' )'
    
flash = []
print("Welcome to a Batman FlashCard thingy: Made by Navid Ali")

while True:
    Character = input("Enter the Batman character you want to add to the flashcard (Hero or villan, idc)")
    Role = input ("Now Enter the thing that character does, e.g. 'Run around gotham dressed as bat', or just pure chaos, whatever u want")

    flash.append(flashcard(Character, Role))
    option = int(input("Enter da number 0, or if you want to make more flashcards enter 1: "))
    
    if(option):
        break

    print("\nYour flashcards Master Bruce")
    for i in flash:
        print(">", i)


       
