import pygame
import pygame_gui
from scene import Scene
from playScene import PlayScene


class MenuScene(Scene):
    def __init__(self, game):
        self.game = game
        self.manager = pygame_gui.UIManager((game.screen_width, game.screen_height))

        self.panel_width = min(560, game.screen_width - 32)
        self.panel_height = 570
        self.panel_x = (game.screen_width - self.panel_width) // 2
        self.panel_y = max(12, (game.screen_height - self.panel_height) // 2)
        control_x = self.panel_x + 60
        control_width = self.panel_width - 120

        self.title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.panel_x + 20, self.panel_y + 12),
                                      (self.panel_width - 40, 40)),
            text="Simulation settings",
            manager=self.manager
        )

        settings = game.settings
        controls = [
            ("Infection rate", "infection_rate", 0.0, 20.0, "{:.1f}"),
            ("Infection radius", "infection_radius", 5.0, 80.0, "{:.1f} px"),
            ("Population", "population", 10.0, 150.0, "{:.0f}"),
            ("Infection threshold", "infection_threshold", 0.1, 2.0, "{:.2f}"),
            ("Recovery time", "recovery_time", 5.0, 60.0, "{:.0f} s"),
            ("Movement speed", "movement_speed", 0.25, 2.0, "{:.2f}x"),
            ("Simulation speed", "simulation_speed", 0.1, 5.0, "{:.1f}x"),
        ]

        self.sliders = {}
        self.labels = {}
        for index, (label, key, minimum, maximum, value_format) in enumerate(controls):
            y = self.panel_y + 58 + index * 64
            self.labels[key] = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((control_x, y), (control_width, 26)),
                text="",
                manager=self.manager
            )
            self.sliders[key] = pygame_gui.elements.UIHorizontalSlider(
                relative_rect=pygame.Rect((control_x, y + 27), (control_width, 24)),
                start_value=settings[key],
                value_range=(minimum, maximum),
                manager=self.manager
            )
            self.labels[key].set_text(
                f"{label}: {value_format.format(settings[key])}"
            )

        button_y = self.panel_y + self.panel_height - 62
        self.play_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((control_x, button_y), (control_width // 2 - 6, 42)),
            text="Start simulation",
            manager=self.manager
        )
        self.reset_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((control_x + control_width // 2 + 6, button_y),
                                      (control_width // 2 - 6, 42)),
            text="Reset defaults",
            manager=self.manager
        )
        self.quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.panel_x + self.panel_width - 54,
                                       self.panel_y + 15), (36, 34)),
            text="X",
            manager=self.manager
        )
        self.controls = controls

    def draw(self, screen):
        pygame.draw.rect(
            screen, (25, 31, 42),
            (self.panel_x, self.panel_y, self.panel_width, self.panel_height),
            border_radius=14
        )
        pygame.draw.rect(
            screen, (72, 88, 110),
            (self.panel_x, self.panel_y, self.panel_width, self.panel_height),
            width=2, border_radius=14
        )
        self.manager.draw_ui(screen)

    def update(self, dt):
        self.manager.update(dt)
        for label, key, _, _, value_format in self.controls:
            value = self.sliders[key].get_current_value()
            self.labels[key].set_text(f"{label}: {value_format.format(value)}")

    def handleClick(self, event):
        self.manager.process_events(event)
        if event.type != pygame_gui.UI_BUTTON_START_PRESS:
            return

        if event.ui_element == self.reset_button:
            for key, slider in self.sliders.items():
                slider.set_current_value(self.game.default_settings[key])
        elif event.ui_element == self.quit_button:
            self.game.running = False
        elif event.ui_element == self.play_button:
            for key, slider in self.sliders.items():
                value = slider.get_current_value()
                self.game.settings[key] = int(round(value)) if key == "population" else value
            self.game.timeScale = self.game.settings["simulation_speed"]
            self.game.play = PlayScene(self.game)
            self.game.gameState = self.game.play
