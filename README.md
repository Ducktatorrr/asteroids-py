# asteroids-py

A simple asteroids game written in Python using Pygame for the [Boot.dev](https://boot.dev) Object Oriented Programming project.

## Base game

The base game as built in the Boot.dev project is a simple base game that draws a player, asteroids, and shots. The player can move, rotate, and shoot. Asteroids can be destroyed by the player's shots and on player-asteroid collision the game is quit.

## Personal additions

I added a few personal additions to the game:

- Player lives (I called it hearts but thery're really circles)
- Respawn logic with invulnerability timer
- Player score
- Start and game over screens

## Running the game

Clone the repository, create a virtual environment, and install the dependencies:

```bash
git clone https://github.com/tobiasklaver/asteroids-py.git
cd asteroids-py
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the game:

```bash
python main.py
```
