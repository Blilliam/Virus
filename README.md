# Virus Project

## What it is
This Python project simulates a basic **virus‑spread** model in a small community.  Each person is represented by the `Person` class, and the program runs one day‑step at a time.

## How it works
* **People** are stored in `main.py` and live inside a list.
* On each day, every infected person may spread the virus to their neighbours.
* The simulation keeps track of **susceptible**, **infected** and **recovered** people.

## Features
* Simple command‑line interface – just run `python main.py`.
* Configurable parameters like infection chance, recovery time and population size are in `config.py`.
* Visual output is printed to the console; each line shows how many people are in each state.

## Running the program
```bash
# First install the virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # on Windows: .\.venv\Scripts\activate

python -m pip install -r requirements.txt


# Run the simulation
python main.py
```

The program will print a short report for each day until everyone has recovered or died.

## Extending the project
Feel free to add new behaviours:
* Add a `death` state.
* Make the infection probability vary by age group.
* Visualise with a simple GUI or plot the daily counts.

## Contributing
If you find bugs or want to add features, open an issue or submit a pull request.  Please keep the coding style consistent with the existing files.

---
© 2026, wtscudder – Free to use under an MIT‑style license.
