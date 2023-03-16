from assets.myplayers import *


class Player:

    all_players = []
    my_players = players

    def __init__(self, my_players):
        self.name = my_players['name']
        self.age = my_players['age']
        self.position = my_players['position']
        self.team = my_players['team']
        Player.all_players.append(self)

    def display_player(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)
        return self

    def display_all_players():
        for player in Player.all_players:
            player.display_player()
            print("\n")
        return Player.all_players

    @classmethod
    def get_team(cls, team_list):
        bonus_team = []
        for x in team_list:
            bonus_team.append(Player(x))
        print(bonus_team)
        return bonus_team


# player_kevin = Player(kevin)
# player_jason = Player(jason)
# player_kyrie = Player(kyrie)
# player_damian = Player(damian)
# player_joel = Player(joel)


# player_joel.display_player()

# new_team = []
# for x in players:
#     new_team.append(Player(x))
# print(new_team)

# Player.get_team(bonus)
# Player.display_all_players()
