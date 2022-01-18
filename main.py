from pygame.math import Vector2
import core
from Joueur import Joueur
from Joueur2 import Joueur2
from Balle import Balle


def setup():
    print("Setup START---------")

    core.fps = 60
    core.WINDOW_SIZE = [1600, 900]
    core.memory("Joueur", Joueur())
    core.memory("Joueur2", Joueur2())
    #core.memory("Balle", Balle())

    core.memory("z", Vector2(0, -1))
    core.memory("q", Vector2(-1, 0))
    core.memory("s", Vector2(0, 1))
    core.memory("d", Vector2(1, 0))

def run():
    core.cleanScreen()

    core.memory("Joueur").afficher(core.screen)
    core.memory("Joueur2").afficher(core.screen)
    #core.memory("Balle").afficher(core.screen)

    core.memory(("Joueur")).deplacement(core.getKeyPressList("z"),core.getKeyPressList("s"))
    core.memory(("Joueur2")).deplacement(core.getKeyPressList("o"), core.getKeyPressList("l"))


core.main(setup, run)