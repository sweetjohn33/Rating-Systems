from game_handler import GameHandler
from player import Player

jill = Player("Jill", 50, 5)
jack = Player("Jack", 50, 10)
hansel = Player("Hansel", 50, 15)
gretel = Player("Gretel", 50, 20)

game = GameHandler([jill, jack, hansel, gretel])

## for i in range(3):

game.round_robin(100000)
game.reset()
game.round_robin(100000)
game.reset()
game.round_robin(100000)
game.reset()




