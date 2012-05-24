import model, view, controller



class Game:
    def __init__(self):
        self.model = model.Model()                                      # Data
        self.view = view.View(self.model)                               # Output
        self.controller = controller.Controller(self.model, self.view)  # Input



if __name__ == '__main__':
    game = Game()