"""
Run:

    python3 -m unittest test_brotab
    pytest brotab

"""
from unittest import TestCase

# from brotab import brotab
from brotab.operations import infer_delete_and_move_commands
# from brotab import get_longest_contiguous_increasing_sequence
from brotab.operations import get_longest_increasing_subsequence
from brotab.operations import infer_move_commands
from brotab.operations import apply_move_commands
from brotab.tab import parse_tab_lines


# class TestLIS(TestCase):
#     def test_one(self):
#         seq = [1, 3, 0, 5, 6, 4, 7, 2, 0]
#         result = get_longest_increasing_subsequence(seq)
#         self.assertEqual([1, 3, 5, 6, 7], result)


class TestReconstruct(TestCase):
    def test_one_move_from_start_to_end(self):
        before = parse_tab_lines([
            'f.0.0\ta\turl',
            'f.0.1\ta\turl',
            'f.0.2\ta\turl',
            'f.0.3\ta\turl',
            'f.0.4\ta\turl',
        ])
        after = parse_tab_lines([
            'f.0.1\ta\turl',
            'f.0.2\ta\turl',
            'f.0.3\ta\turl',
            'f.0.4\ta\turl',
            'f.0.0\ta\turl',
        ])
        commands = infer_move_commands(before, after)
        self.assertEqual(commands, [(0, 4)])
        actual_after = apply_move_commands(before, commands)
        self.assertEqual(actual_after, after)

    def test_one_move_from_end_to_start(self):
        before = parse_tab_lines([
            'f.0.0\ta\turl',
            'f.0.1\ta\turl',
            'f.0.2\ta\turl',
            'f.0.3\ta\turl',
            'f.0.4\ta\turl',
        ])
        after = parse_tab_lines([
            'f.0.4\ta\turl',
            'f.0.0\ta\turl',
            'f.0.1\ta\turl',
            'f.0.2\ta\turl',
            'f.0.3\ta\turl',
        ])
        commands = infer_move_commands(before, after)
        self.assertEqual(commands, [(4, 0)])
        actual_after = apply_move_commands(before, commands)
        self.assertEqual(actual_after, after)

    def test_one_move_from_start_to_center(self):
        before = parse_tab_lines([
            'f.0.0\ta\turl',
            'f.0.1\ta\turl',
            'f.0.2\ta\turl',
            'f.0.3\ta\turl',
            'f.0.4\ta\turl',
            'f.0.5\ta\turl',
            'f.0.6\ta\turl',
            'f.0.7\ta\turl',
            'f.0.8\ta\turl',
        ])
        after = parse_tab_lines([
            'f.0.1\ta\turl',
            'f.0.2\ta\turl',
            'f.0.3\ta\turl',
            'f.0.4\ta\turl',
            'f.0.0\ta\turl',
            'f.0.5\ta\turl',
            'f.0.6\ta\turl',
            'f.0.7\ta\turl',
            'f.0.8\ta\turl',
        ])
        commands = infer_move_commands(before, after)
        self.assertEqual(commands, [(0, 4)])
        actual_after = apply_move_commands(before, commands)
        self.assertEqual(actual_after, after)

    def test_crossings(self):
        before = parse_tab_lines([
            'f.0.0\ta\turl',
            'f.0.1\ta\turl',
            'f.0.2\ta\turl',
            'f.0.3\ta\turl',
            'f.0.4\ta\turl',
            'f.0.5\ta\turl',
            'f.0.6\ta\turl',
            'f.0.7\ta\turl',
            'f.0.8\ta\turl',
        ])
        after = parse_tab_lines([
            'f.0.4\ta\turl',
            'f.0.0\ta\turl',
            'f.0.1\ta\turl',
            'f.0.2\ta\turl',
            'f.0.3\ta\turl',
            'f.0.6\ta\turl',
            'f.0.7\ta\turl',
            'f.0.8\ta\turl',
            'f.0.5\ta\turl',
        ])
        commands = infer_move_commands(before, after)
        self.assertEqual(commands, [(4, 0), (5, 8)])
        actual_after = apply_move_commands(before, commands)
        self.assertEqual(actual_after, after)


    def test_decreasing_ids_from_start_to_end(self):
        before = parse_tab_lines([
            'f.0.10\ta\turl',
            'f.0.9\ta\turl',
            'f.0.8\ta\turl',
            'f.0.7\ta\turl',
        ])
        after = parse_tab_lines([
            'f.0.9\ta\turl',
            'f.0.8\ta\turl',
            'f.0.7\ta\turl',
            'f.0.10\ta\turl',
        ])
        commands = infer_move_commands(before, after)
        self.assertEqual(commands, [(10, 3)])
        actual_after = apply_move_commands(before, commands)
        self.assertEqual(actual_after, after)


# class TestSequence(TestCase):
#     def test_get_longest_contiguous_increasing_sequence(self):
#         tabs = [
#             'f.0\tFirst',
#             'f.1\tSecond',
#             'f.2\tThird',
#         ]
#         result = get_longest_contiguous_increasing_sequence(tabs)
#         self.assertEqual(result, (0, 3))

#         tabs = [
#             'f.4\te',
#             'f.1\tb',
#             'f.2\tc',
#             'f.3\td',
#             'f.0\ta',
#         ]
#         result = get_longest_contiguous_increasing_sequence(tabs)
#         self.assertEqual(result, (1, 3))

#         tabs = [
#             'f.4\te',
#             'f.1\tb',
#             'f.2\tc',
#             'f.3\td',
#             'f.0\ta',
#             'f.9\ta',
#             'f.5\tz',
#             'f.6\tz',
#             'f.7\tz',
#             'f.8\tz',
#         ]
#         result = get_longest_contiguous_increasing_sequence(tabs)
#         self.assertEqual(result, (6, 4))

#         tabs = [
#             'f.9\te',
#             'f.4\tz',
#             'f.5\tz',
#             'f.6\tz',
#             'f.7\tz',
#             'f.1\tb',
#             'f.2\tc',
#             'f.3\td',
#             'f.0\ta',
#         ]
#         result = get_longest_contiguous_increasing_sequence(tabs)
#         self.assertEqual(result, (1, 4))


class TestInferDeleteMoveCommands(TestCase):
    def _eq(self, tabs_before, tabs_after, expected_deletes, expected_moves):
        deletes, moves = infer_delete_and_move_commands(
            parse_tab_lines(tabs_before),
            parse_tab_lines( tabs_after))
        self.assertEqual(expected_deletes, deletes)
        self.assertEqual(expected_moves, moves)

    def test_only_deletes(self):
        self._eq(
            ['f.0.0\ttitle\turl',
             'f.0.1\ttitle\turl',
             'f.0.2\ttitle\turl'],
            ['f.0.2\ttitle\turl'],
            [1, 0],
            []
        )

        self._eq(
            ['f.0.0\ttitle\turl',
             'f.0.1\ttitle\turl',
             'f.0.2\ttitle\turl',
             'f.0.3\ttitle\turl'],
            ['f.0.0\ttitle\turl',
             'f.0.2\ttitle\turl'],
            [3, 1],
            []
        )

    def test_only_moves(self):
        self._eq(
            [
                'f.0.0\ttitle\turl',
                'f.0.1\ttitle\turl',
                'f.0.2\ttitle\turl',
            ],
            [
                'f.0.2\ttitle\turl',
                'f.0.0\ttitle\turl',
                'f.0.1\ttitle\turl',
            ],
            [],
            [(2, 0)]
        )

        self._eq(
            [
                'f.0.0\ttitle\turl',
                'f.0.1\ttitle\turl',
                'f.0.2\ttitle\turl',
            ],
            [
                'f.0.2\ttitle\turl',
                'f.0.1\ttitle\turl',
                'f.0.0\ttitle\turl',
            ],
            [],
            [(2, 0), (1, 1)]
        )