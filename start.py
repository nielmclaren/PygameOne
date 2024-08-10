#!/usr/bin/python3

import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False

  screen.fill("purple")

  pygame.draw.circle(screen, "cyan", player_pos, 40)

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

  if direction.magnitude():
    player_pos += direction.normalize() * 300 * dt

  pygame.display.flip()

  dt = clock.tick(60) / 1000 # Set 60 FPS limit

pygame.quit()
