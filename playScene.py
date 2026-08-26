import random

from box import Box
import person
from pulse import Pulse
from scene import Scene

class PlayScene(Scene):
    def __init__(self, game):
        self.game = game

        boxHeight = game.c.get("box", "height")
        boxWidth = game.c.get("box", "width")

        game.add_box(Box(50, 50, boxWidth, boxHeight, self))
        game.add_box(Box(50, 600, boxWidth, boxHeight, self))

        for i in range(50):
            p = person.Person(game, game.simulation_boxes[i%2])
            game.people.append(p)
            game.pulses.append(Pulse(p))

        random.choice(self.game.people).state = 1  # start with one infected

    def update(self, dt):
        self.game.dt = dt

        for i in range(len(self.game.people)):
            self.game.people[i].update(dt)
            self.game.pulses[i].update(dt)
            self.game.handlePulseCollisions(self.game.pulses[i])

        self.game.historyTimer += 1
        if self.game.historyTimer % 3 == 0:
            self.game.updateHistory()

    def draw(self, screen):
        self.game.center.draw(screen)

        for box in self.game.simulation_boxes:
            box.draw(screen)

        for i in range(len(self.game.people)):
            self.game.people[i].draw(screen)
            self.game.pulses[i].draw(screen)

        self.game.graph.draw(screen)