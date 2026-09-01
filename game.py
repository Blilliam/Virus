import random
from turtle import width
import pygame
from playScene import PlayScene
from box import Box
from center import Center
from config import Config
from graph import Graph
from menuScene import MenuScene
import person
from person import Person
from pulse import Pulse

class Game:
    def __init__(self, screen_width, screen_height):

        self.c = Config.load()

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.infectionRate = self.c.get("person", "infectionRate")

        self.simulation_boxes = []

        self.center = Center(800, 400, 100, 100)

        self.history = []

        self.people = []
        self.pulses = []

        self.historyTimer = 0

        self.graph = Graph(self, 600, 600, 400, 400)

        self.play = PlayScene(self)
        self.menu = MenuScene(self)

        self.gameState = self.menu

    def add_box(self, box):
        self.simulation_boxes.append(box)

    def update(self, dt):
        self.gameState.update(dt)
        

    def draw(self, screen):
        self.gameState.draw(screen)

    def handleClick(self, event):
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

                    trueRate = self.infectionRate * self.dt * strength

                    person.currInfectionCount += trueRate
                    if person.currInfectionCount >= person.infectionThreshold:
                        person.state = Person.STATE_INFECTED
                        print(distance, strength, person.pos, pulseVector)




    def updateHistory(self):
        infectedCount = sum(1 for p in self.people if p.state == 1)
        uninfectedCount = sum(1 for p in self.people if p.state == 0)
        recoveredCount = sum(1 for p in self.people if p.state == -1)
        self.history.append([uninfectedCount, infectedCount, recoveredCount])
