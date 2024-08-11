#!/usr/bin/python3

import pygame
from world import World

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

world = World((screen.get_width(), screen.get_height()))

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False

  screen.fill("purple")

  pygame.draw.circle(screen, "cyan", world.player_pos, 40)
  pygame.draw.circle(screen, "red", world.mob.pos, 40)

  keys = pygame.key.get_pressed()
  direction = pygame.Vector2()
  if keys[pygame.K_w]:
    direction.y -= 1
  if keys[pygame.K_s]:
    direction.y += 1
  if keys[pygame.K_a]:
    direction.x -= 1
  if keys[pygame.K_d]:
    direction.x += 1
  world.set_controller(direction.normalize() if direction.magnitude() else direction)

  world.step(dt)

  pygame.display.flip()

  dt = clock.tick(60) / 1000 # Set 60 FPS limit

pygame.quit()
