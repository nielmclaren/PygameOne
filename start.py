#!/usr/bin/python3

import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

def poll_events():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()

while running:
  poll_events()

  screen.fill("purple")

  pygame.display.flip()
  clock.tick(60) # Set 60 FPS limit

pygame.quit()
