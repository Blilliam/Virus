# Virus Simulation

## What it is
A real-time 2D Python simulation that models how a virus spreads through a moving population. Built with **Pygame** and **pygame_gui**, it features interactive parameter sliders, spatial simulation boxes, visual infection pulses, and a live population graph.

## How it works
- **Simulation & Scenes (`game.py`, `menuScene.py`, `playScene.py`):** Starts in an interactive menu where you can adjust simulation variables before launching the active simulation.
- **Agents (`person.py`):** Each individual moves continuously inside simulation boxes (`box.py`) with randomized speed and heading, transitioning between states as the outbreak progresses.
- **Transmission (`pulse.py`):** Infected individuals emit proximity pulses that check for collisions with nearby people to spread the infection.
- **Live Tracking (`graph.py`):** Records population history over time and plots state counts visually during the run.

## Configuration
Default simulation settings (such as infection rate, infection radius, and box dimensions) are stored in `infectioninfo.toml` and loaded via `config.py`.

## Running the program
```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate

# Install dependencies
python -m pip install -r requirements.txt

# Run the simulation
python main.py