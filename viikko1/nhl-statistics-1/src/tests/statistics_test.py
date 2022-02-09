import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search(self):
        player = self.statistics.search("Lemieux")
        self.assertEqual(str(player),"Lemieux PIT 45 + 54 = 99")

    def test_search_no_player(self):
        player = self.statistics.search("Alfred")
        self.assertEquals(player, None)

    def test_team(self):
        team = self.statistics.team("EDM")
        teamstring = [str(x) for x in team]
        self.assertCountEqual(teamstring, [str(Player("Semenko", "EDM", 4, 12)),
            str(Player("Kurri",   "EDM", 37, 53)),
            str(Player("Gretzky", "EDM", 35, 89))])

    def test_team_no_team(self):
        team = self.statistics.team("Moo")
        self.assertCountEqual(team, list())

    def test_top_scorers(self):
        topScorers = self.statistics.top_scorers(2)
        topScorerString = [str(x) for x in topScorers]
        self.assertCountEqual(topScorerString,[str(Player("Gretzky", "EDM", 35, 89)),str(Player("Yzerman", "DET", 42, 56)), str(Player("Lemieux", "PIT", 45, 54))])
            


    





