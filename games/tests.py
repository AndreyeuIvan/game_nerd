from unittest import TestCase
from unittest.mock import patch
from games import views


class TestGame(TestCase):
    @patch('games.views.main')
    def test_games_main(self, MockGame):
        game = MockGame()

        game.return_value = [
            {
                "name": "Scarlet Blade",
                "slug": "scarlet-blade",
                "id": 1977,
                "genres": [
                    "Role-playing (RPG)",
                    "Hack and slash/Beat 'em up"
                ],
                "platforms": [
                    "PC (Microsoft Windows)"
                ],
                "tweets": []
            }
        ]
        response = views.main()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)