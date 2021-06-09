       # Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line
import sys


class Player:
    def __init__(self, name, speed = 0, endurance = 0, accuracy = 0):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy
                     
    def introduce(self):
        return f'Hello everyone, my name is {self.name}.' #got fstrings now yes :)

    def strength(self):
        tuple_player = ('speed', self.speed, 'endurance', self.endurance, 'accuracy', self.accuracy)
        strength = max(tuple_player[1::2])
        index_higgest = tuple_player.index(strength)
        tuple_best = (tuple_player[index_higgest -1], tuple_player[index_higgest])
        return tuple_best


class Commentator(Player):
    def __init__(self, name):
        self.name = name 

    def sum_player(self, Player):
        sum = Player.speed + Player.endurance + Player.accuracy
        return sum

    def compare_players(self, Player1, Player2, attri='speed'):
        total1 = self.sum_player(Player1)
        total2 = self.sum_player(Player2)
        tuple_player1 = ('speed', Player1.speed, 'endurance', Player1.endurance, 'accuracy', Player1.accuracy)
        tuple_player2 = ('speed', Player2.speed, 'endurance', Player2.endurance, 'accuracy', Player2.accuracy)
        find_index_attri = tuple_player1.index(attri) ## 1 or 2 should work both ^^ need to improve 2 lines above....
        player1_attribute_number = tuple_player1[find_index_attri + 1]
        player2_attribute_number = tuple_player2[find_index_attri + 1]
        if player1_attribute_number > player2_attribute_number:
            return Player1.name
        elif player1_attribute_number < player2_attribute_number:
            return Player2.name
        elif player1_attribute_number == player2_attribute_number:
            best1 = Player1.strength()
            best2 = Player2.strength()
            if best1[1] > best2[1]:
                return best1
            elif best1[1] < best2[1]:
                return best2
            elif best1[1] == best2[1]:
                if total1 == total2:
                    return 'These two players might as well be twins!'
                elif total1 > total2:
                    return total2
                else:
                    return total1              
        return


