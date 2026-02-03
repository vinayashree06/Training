class Pen:
    def use(self):
        return "Writing"

class Eraser:
    def use(self):
        return "Erasing"

def perform(tool):
    print(tool.use())

perform(Pen())
perform(Eraser())