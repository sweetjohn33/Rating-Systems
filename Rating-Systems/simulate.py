from game_handler import GameHandler
from player import Player

jill = Player("Jill", 40, 10)
jack = Player("Jack", 45, 10)
hansel = Player("Hansel", 50, 10)
gretel = Player("Gretel", 55, 10)
george = Player("George", 60, 10)
isaac = Player("Isaac", 65, 10)
paul = Player("Paul", 70, 10)

game = GameHandler([jill, jack, hansel, gretel, george, isaac, paul])



if __name__ == '__main__':
    for i in range(20):
        game.round_robin(100)
        print("\n \n \n ")
