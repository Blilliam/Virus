import pygame
import pygame_gui
from scene import Scene
from playScene import PlayScene

class MenuScene(Scene):
    def __init__(self, game):
        self.game = game
        
        # Initialize the UI Manager using game screen resolution
        self.manager = pygame_gui.UIManager((game.screen_width, game.screen_height))

        # Read defaults from config
        default_rate = float(game.c.get("person", "infectionRate") or 5.0)
        default_radius = float(game.c.get("person", "infectionRadius") or 30.0)
        default_sim_speed = getattr(game, "time_scale", 1.0)

        # Infection Rate Slider
        self.rate_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((200, 50), (300, 30)),
            text=f"Infection Rate: {default_rate:.1f}",
            manager=self.manager
        )
        self.rate_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((200, 80), (300, 30)),
            start_value=default_rate,
            value_range=(1.0, 20.0),
            manager=self.manager
        )

        # Infection Radius Slider
        self.radius_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((200, 130), (300, 30)),
            text=f"Infection Radius: {default_radius:.1f}",
            manager=self.manager
        )
        self.radius_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((200, 160), (300, 30)),
            start_value=default_radius,
            value_range=(5.0, 60.0),
            manager=self.manager
        )

        # Simulation Speed (dt multiplier) Slider
        self.sim_speed_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((200, 210), (300, 30)),
            text=f"Sim Speed: {default_sim_speed:.1f}x",
            manager=self.manager
        )
        self.sim_speed_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((200, 240), (300, 30)),
            start_value=default_sim_speed,
            value_range=(0.1, 5.0),
            manager=self.manager
        )

        # Play Button
        self.play_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((250, 310), (200, 50)),
            text="Play",
            manager=self.manager
        )

    def draw(self, screen):
        self.manager.draw_ui(screen)

    def update(self, dt):
        # Update manager timer
        self.manager.update(dt)

        # Dynamically update labels when sliders move
        self.rate_label.set_text(f"Infection Rate: {self.rate_slider.get_current_value():.1f}")
        self.radius_label.set_text(f"Infection Radius: {self.radius_slider.get_current_value():.1f}")
        self.sim_speed_label.set_text(f"Sim Speed: {self.sim_speed_slider.get_current_value():.1f}x")

    def handleClick(self, event):
        # Pass pygame events to manager
        self.manager.process_events(event)

        # Detect button click
        if event.type == pygame_gui.UI_BUTTON_START_PRESS:
            if event.ui_element == self.play_button:
                # Apply configured slider values
                self.game.infectionRate = self.rate_slider.get_current_value()
                self.game.c.data["person"]["infectionRadius"] = self.radius_slider.get_current_value()

                # Reinitialize PlayScene with updated variables and launch
                self.game.play = PlayScene(self.game)
                self.game.time_scale = self.sim_speed_slider.get_current_value()
                self.game.gameState = self.game.play