from unittest import TestCase, main

from task1.score import generate_game, get_score


class TestScore(TestCase):

    def setUp(self) -> None:
        self.game = generate_game()
        self.stamps = [{'offset': 0, 'score': {'home': 0, 'away': 0}},
                       {'offset': 3, 'score': {'home': 1, 'away': 0}},
                       {'offset': 6, 'score': {'home': 1, 'away': 1}},
                       {'offset': 9, 'score': {'home': 1, 'away': 2}},
                       {'offset': 12, 'score': {'home': 2, 'away': 2}},
                       {'offset': 15, 'score': {'home': 3, 'away': 2}},
                       {'offset': 18, 'score': {'home': 3, 'away': 2}},
                       {'offset': 21, 'score': {'home': 3, 'away': 3}}]

    def test_start_offset_function(self):
        self.assertEqual(get_score(self.game, 0), (0, 0))

    def test_value_not_in_stamp(self):
        self.assertEqual(get_score(self.stamps, 2), (0, 0))
        self.assertEqual(get_score(self.stamps, 19), (3, 2))

    def test_value_stamps(self):
        self.assertEqual(get_score(self.stamps, 3), (1, 0))
        self.assertEqual(get_score(self.stamps, 6), (1, 1))
        self.assertEqual(get_score(self.stamps, 9), (1, 2))
        self.assertEqual(get_score(self.stamps, 12), (2, 2))
        self.assertEqual(get_score(self.stamps, 15), (3, 2))
        self.assertEqual(get_score(self.stamps, 18), (3, 2))
        self.assertEqual(get_score(self.stamps, 21), (3, 3))

    def test_zero_value_function(self):
        self.assertEqual(get_score(self.game, -1), (0, 0))
        self.assertEqual(get_score(self.game, -15), (0, 0))
        self.assertEqual(get_score(self.game, -150), (0, 0))
        self.assertEqual(get_score(self.game, -1500), (0, 0))
        self.assertEqual(get_score(self.game, -15000), (0, 0))


if __name__ == '__main__':
    main()
