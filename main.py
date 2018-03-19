import pygame , sys , game_function as g_f
from pygame.sprite import Group
#   сис -  для закінчення програми
from setinngs import Setings
from ship import Ship
def init_game():
    pygame.init()
    game_setinngs=Setings()

    screen=pygame.display.set_mode((game_setinngs.screen_width,game_setinngs.screen_height)) # ет мод для висоти і ширини екрану
    ship = Ship(screen)
    bullets= Group()
    bg_color=game_setinngs.bg_color

    pygame.display.set_caption("gamenambawan")
    while True:
        g_f.cheek_evens(game_setinngs, ship, screen, bullets)
        g_f.update_screen(game_setinngs,ship,screen,bullets)
        ship.update()
        bullets.update()
init_game()