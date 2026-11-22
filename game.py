import pygame
from center import Center
from config import Config
from graph import Graph
from menuScene import MenuScene
from person import Person

class Game:
    def __init__(self, screen_width, screen_height):

        self.c = Config.load()

        self.timeScale = 1

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.default_settings = {
            "infection_rate": float(self.c.get("person", "infectionRate", default=5)),
            "infection_radius": float(self.c.get("person", "infectionRadius", default=30)),
            "population": int(self.c.get("population", "count", default=50)),
            "infection_threshold": float(self.c.get("person", "infectionThreshold", default=0.5)),
            "recovery_time": float(self.c.get("person", "recoveryTime", default=18)),
            "movement_speed": float(self.c.get("person", "movementSpeed", default=1.0)),
            "simulation_speed": 1.0,
        }
        self.settings = self.default_settings.copy()
        self.running = True

        self.simulation_boxes = []

        self.center = Center(800, 400, 100, 100)

        self.history = []

        self.people = []
        self.pulses = []

        self.historyTimer = 0

        self.graph = Graph(self, 600, 600, 400, 400)

        self.menu = MenuScene(self)

        self.gameState = self.menu

    def add_box(self, box):
        self.simulation_boxes.append(box)

    def update(self, dt):
        newDt = dt * self.timeScale
        self.gameState.update(newDt)
        

    def draw(self, screen):
        self.gameState.draw(screen)

    def handleClick(self, event):
        if self.gameState:
            self.gameState.handleClick(event)


    def handlePulseCollisions(self, pulse):
        for person in self.people:
            if person.state == Person.STATE_UNINFECTED and pulse.person != person and pulse.person.state == Person.STATE_INFECTED:
                pulseVector = pygame.Vector2(pulse.x, pulse.y)
                distance = pulseVector.distance_to(person.pos)
                if distance < person.size + pulse.size:

                    maxDist = pulse.size + person.size
                    ratio = distance / maxDist

                    strength = 1-ratio

                    trueRate = self.settings["infection_rate"] * self.dt * strength

                    person.currInfectionCount += trueRate
                    if person.currInfectionCount >= person.infectionThreshold:
                        person.state = Person.STATE_INFECTED




    def updateHistory(self):
        infectedCount = sum(1 for p in self.people if p.state == 1)
        uninfectedCount = sum(1 for p in self.people if p.state == 0)
        recoveredCount = sum(1 for p in self.people if p.state == -1)
        self.history.append([uninfectedCount, infectedCount, recoveredCount])
