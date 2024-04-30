# Sandman's Topdown Adventure
## Summary
This project was created for the Software Design final project, Spring 2024.

Sandman's Topdown Adventure is an adventure game inspired by the top-down
view of classic JRPGs like Pokemon, Dragon Quest, and Chrono Trigger. In
this game, the player explores a vast world and meets characters with
different problems. When the player helps solve each of the characters'
problems, they win! Afterwards, the player is free to continue exploring
the world.

## Running The Game
In order to run this program, users should navigate to the game.py file
in the root folder and press run. If all system requirements and package
installs are up to par with the project requirements listed below, the project
should run without a hitch!

## Program Architecture
This game follows an MVC architecture with a Controller class, a View class,
and a series of Model classes. All files that track and update the game state
can be found in the Model folder. The files that contain the Controller and
the View classes are named as such and can be found in the project's root
folder.

Most supplemental resources can be found in the Resources folder. This
includes JSON files that store hard-coded game data, as well as visual assets
such as player sprites, NPC sprites, and map tilesets. The one exception to
this is the .tmx map files, which needed to be stored in the project's root
folder in order to load correctly. Additionally, unit tests can be found in the
aptly named Unit Tests folder. Finally, the files for the Github Pages website
can be found in the docs folder.

Finally, the file game.py, which runs the program, can be found in the
project's root folder.

## Imports
We imported the following packages for this project:
- pygame (to provide a data structure for sprites)
- pyTMX (to port our .tmx map files into pygame structure)
- json (to load json data into our project)

Note that the first two packages, pygame and pyTMX, will need to be installed
(see requirements.txt for more information). json is a built-in package with
Python and therefore does not need to be installed.

## System Tools
This project was created in VSCode in Python 3.11.8; as such, users should be
sure that their Python is up to date. For more information, users can look at
the Software Design Computational Setup:
https://softdes.olin.edu/docs/setup/setup-instructions/

## Other Requirements
For additional information, please look at the requirements.txt file. This file
was generated using code provided by the Software Design teaching team.

## Asset Credits
Here is a list of the assets used in our project and their sources. All assets
were either purchased or were permissible to use by the artists.

Tilesets by Clockwork Raven on Itch.io
Link: https://itch.io/s/87673/raven-fantasy-tilesets-full-collection

Player sprites by PizzaSun and tebited15 on DeviantArt
Link: https://www.deviantart.com/pizzasun/art/Pokemon-XY-Male-Trainer-Gen-IV-Style-698428061

NPC sprites by Pipoya on Itch.io
Link: https://pipoya.itch.io/pipoya-free-rpg-character-sprites-32x32
