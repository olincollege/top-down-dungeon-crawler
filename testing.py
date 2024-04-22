import pygame
from pytmx.util_pygame import load_pygame

tmx = load_pygame("Resources/test_map.tmx")
print(dir(tmx.get_layer_by_name("Dirt")))
