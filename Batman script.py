class Batman:

    def __init__(self):
        print("Batman is ready")

    def whoisthis(self):
        print("Vigilante crime fighter")

    def fight(self):
        print("Fight Batman, FIGHT!!")

class Penguin(Batman):

    def __init__(self):
        super().__init__()
        print("The penguin is ready")

    def whoisthis(self):
        print("The penguin")

    def run(self):
        print("RUN PENGUIN RUUUNNNN!!")


peggy = Penguin()
peggy.whoisthis()
peggy.fight()
peggy.run()




        