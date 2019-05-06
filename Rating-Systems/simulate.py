from game_handler import GameHandler
from player import Player

jill = Player("Jill", 50, 10)
jack = Player("Jack", 60, 20)
hansel = Player("Hansel", 40, 30)
gretel = Player("Gretel", 50, 40)

game = GameHandler([jill, jack, hansel, gretel])

game.round_robin(3)


