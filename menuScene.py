from scene import Scene
import buttons

class MenuScene(Scene):
    def __init__(self, game):
        self.infectionRadiusMult = 1
        self.infectionThresholdMult = 1
        self.infectionRateMult = 1
        self.game = game

        self.playButton = buttons.Button(200, 200, 200, 100, "Play")

    def draw(self, screen):
        self.playButton.draw(screen)
        
    def update(self, dt):
        self.playButton.update(dt)

        if self.playButton.value:
            self.game.gameState = self.game.play


    def handleClick(self, event):
        self.playButton.handleClick(event)



