# Solar System Simulation (2D)

A simple solar system simulation made with python, pygame and pymunk.
Just for fun - to see how gravitational forces could work - and to play around.

Demo video: <a href="https://www.youtube.com/watch?v=WyyJNSKWbjk">Solar System Simulation (2D)</a>

Works with >= python3.7.

---

## Run the program

```bash
pip install -r requirements.txt
```

```bash
python solar_system.py
```

---

## Controls

1. Leftclick to add a moon.
2. Rightclick to add a planet.
3. Middleclick to move the sun (and the center of the gravitational pull)
4. Enjoy! 🚀

## How it is implemented

-   Objects that spawn do not have any initial velocity.
-   Objects will have a random mass and random radius.
-   The mass depends on the radius.
-   The mass of the sun is way bigger than that of any object.
-   Objects that are farther than 2500 units away from the sun will be removed.
