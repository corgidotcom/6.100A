# for running unit tests on 6.100A student code
import sys, unittest, os
from unittest import TestCase
from ps3 import *


# Lightweight harness adapted from prior psets
class Results_600(unittest.TextTestResult):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.points = 40
        self.output = []

    def addFailure(self, test, err):
        self._handle_deduct(test)
        super().addFailure(test, err)

    def addError(self, test, err):
        self._handle_deduct(test)
        super().addError(test, err)

    def _handle_deduct(self, test):
        name = test.id().split('.')[-1]
        pts = point_values.get(name, 1)
        msg = messages.get(name, name)
        self.output.append(f"[-{pts}]: {msg}")
        self.points -= pts

    def getOutput(self):
        return "All correct!" if not self.output else "\n".join(self.output)

    def getPoints(self):
        return max(0.0, round(self.points, 3))


point_values = {
    'test_normalize_1': 1,
    'test_normalize_2': 1,
    'test_normalize_3': 1,
    'test_normalize_4': 1,
    'test_normalize_5': 1,
    'test_swap_equivalents_1': 1,
    'test_swap_equivalents_2': 1,
    'test_swap_equivalents_3': 1,
    'test_swap_equivalents_4': 1,
    'test_remove_contaminants_1': 1,
    'test_remove_contaminants_2': 1,
    'test_remove_contaminants_3': 1,
    'test_compress_runs_1': 1,
    'test_compress_runs_2': 1,
    'test_compress_runs_3': 1,
    'test_compress_runs_4': 1,
    'test_stitch_short_routes_1': 1,
    'test_stitch_short_routes_2': 1,
    'test_stitch_short_routes_3': 1,
    'test_balance_load_1': 1,
    'test_balance_load_2': 1,
    'test_balance_load_3': 1,
    'test_balance_load_4': 1,
    'test_cancel_street_1': 1,
    'test_cancel_street_2': 1,
    'test_cancel_street_3': 1,
    'test_cancel_street_4': 1,
    'test_enqueue_1': 1,
    'test_enqueue_2': 1,
    'test_enqueue_3': 1,
    'test_fast_forward_1': 1,
    'test_fast_forward_2': 1,
    'test_fast_forward_3': 1,
    'test_prioritize_1': 1,
    'test_prioritize_2': 1,
    'test_prioritize_3': 1,
    'test_prioritize_4': 1,
    'test_edge_cases': 1, 
    'test_routes_scaling': 1, 
    'test_queue_ops': 1,
}

messages = {
    'test_normalize_1': 'normalize failed on spacing/casing',
    'test_normalize_2': 'normalize failed on empty strings',
    'test_normalize_3': 'normalize failed on extra spaces',
    'test_normalize_4': 'normalize failed on capitalization',
    'test_normalize_5': 'normalize failed on spacing/casing',
    'test_swap_equivalents_1': 'error in swap_equivalents mapping logic',
    'test_swap_equivalents_2': 'error in swap_equivalents mapping logic',
    'test_swap_equivalents_3': 'error in swap_equivalents mapping logic',
    'test_swap_equivalents_4': 'error in swap_equivalents mapping logic',
    'test_remove_contaminants_1': 'remove_contaminants order/predicate',
    'test_remove_contaminants_2': 'remove_contaminants order/predicate',
    'test_remove_contaminants_3': 'remove_contaminants order/predicate',
    'test_compress_runs_1': 'compress_runs consecutive dedupe',
    'test_compress_runs_2': 'compress_runs consecutive dedupe',
    'test_compress_runs_3': 'compress_runs consecutive dedupe',
    'test_compress_runs_4': 'compress_runs consecutive dedupe',
    'test_stitch_short_routes_1': 'stitch_short_routes merging behavior',
    'test_stitch_short_routes_2': 'stitch_short_routes merging behavior',
    'test_stitch_short_routes_3': 'stitch_short_routes merging behavior',
    'test_balance_load_1': 'balance_load balancing moves',
    'test_balance_load_2': 'balance_load balancing moves',
    'test_balance_load_3': 'balance_load balancing moves',
    'test_balance_load_4': 'balance_load balancing moves',
    'test_cancel_street_1': 'cancel_street removal and empty routes',
    'test_cancel_street_2': 'cancel_street removal and empty routes',
    'test_cancel_street_3': 'cancel_street removal and empty routes',
    'test_cancel_street_4': 'cancel_street removal and empty routes',
    'test_enqueue_1': 'enqueue_all basic extend',
    'test_enqueue_2': 'enqueue_all basic extend',
    'test_enqueue_3': 'enqueue_all basic extend',
    'test_fast_forward_1': 'fast_forward slice deletion',
    'test_fast_forward_2': 'fast_forward slice deletion',
    'test_fast_forward_3': 'fast_forward slice deletion',
    'test_prioritize_1': 'prioritize stable partition',
    'test_prioritize_2': 'prioritize stable partition',
    'test_prioritize_3': 'prioritize stable partition',
    'test_prioritize_4': 'prioritize stable partition',
    'test_edge_cases': 'edge cases for empty lists and other operations', 
    'test_routes_scaling': 'stitching and balancing on larger routes', 
    'test_queue_ops': 'queue operations composition',
}


class TestPS3(TestCase):
    def test_normalize_1(self):
        s = ["  Water   Bottle ", "  CAN", "  ", "Box "]
        normalize(s)
        self.assertEqual(s, ['water bottle', 'can', '', 'box'])
    
    def test_normalize_2(self):
        s = ["", " ", "   "]
        normalize(s)
        self.assertEqual(s, ['', '', ''])
    
    def test_normalize_3(self):
        spaces_case = ["  water   bottle", " plastic", "  ", "box  "]
        normalize(spaces_case)
        self.assertEqual(spaces_case, ['water bottle', 'plastic', '', 'box'])
    
    def test_normalize_4(self):
        capitalization_case = ["WateR BoTtle", "CAN", "CaN"]
        normalize(capitalization_case)
        self.assertEqual(capitalization_case, ['water bottle', 'can', 'can'])
    
    def test_normalize_5(self):
        s_2 = ["  Water   Bottle ", "  CAN", "  ", "Box "]
        normalize(s_2)
        self.assertEqual(s_2, ['water bottle', 'can', '', 'box'])

    def test_swap_equivalents_1(self):
        s = ['water bottle', 'box', 'flyers', 'glass']
        c = swap_equivalents(s, EQUIV)
        self.assertEqual(c, 3)
        self.assertEqual(s, ['plastic', 'cardboard', 'cardboard', 'glass'])
    
    def test_swap_equivalents_2(self):
        s = ['water bottle', 'box', 'flyers', 'can', 'takeout']
        c = swap_equivalents(s, EQUIV)
        self.assertEqual(c, 5)
        self.assertEqual(s, ['plastic', 'cardboard', 'cardboard', 'metal', 'plastic'])
    
    def test_swap_equivalents_3(self):
        s = ['plastic', 'cardboard', 'banana peel', '']
        c = swap_equivalents(s, EQUIV)
        self.assertEqual(c, 0)
        self.assertEqual(s, ['plastic', 'cardboard', 'banana peel', ''])
    
    def test_swap_equivalents_4(self):
        s = ['plastic', 'plastic', 'cardboard', 'cardboard', 'glass']
        c = swap_equivalents(s, EQUIV)
        self.assertEqual(c, 0)
        self.assertEqual(s, ['plastic', 'plastic', 'cardboard', 'cardboard', 'glass'])

    def test_remove_contaminants_1(self):
        s = ['plastic', 'cardboard', 'banana peel', '']
        removed = remove_contaminants(s, ALLOWED)
        self.assertEqual(removed, 2)
        self.assertEqual(s, ['plastic', 'cardboard'])
    
    def test_remove_contaminants_2(self):
        s = ['cardboard', 'glass', 'plastic']
        removed = remove_contaminants(s, ALLOWED)
        self.assertEqual(removed, 0)
        self.assertEqual(s, ['cardboard', 'glass', 'plastic'])
    
    def test_remove_contaminants_3(self):
        s = ['not allowed', '8900', 'cheese']
        removed = remove_contaminants(s, ALLOWED)
        self.assertEqual(removed, 3)
        self.assertEqual(s, [])

    def test_compress_runs_1(self):
        s = ['plastic', 'plastic', 'cardboard', 'cardboard', 'glass']
        r = compress_runs(s)
        self.assertEqual(r, 2)
        self.assertEqual(s, ['plastic', 'cardboard', 'glass'])
    
    def test_compress_runs_2(self):
        s = ['plastic', 'plastic', 'cardboard', 'plastic', 'plastic']
        r = compress_runs(s)
        self.assertEqual(r, 2)
        self.assertEqual(s, ['plastic', 'cardboard', 'plastic'])
    
    def test_compress_runs_3(self):
        s = ['plastic', 'plastic', 'plastic']
        r = compress_runs(s)
        self.assertEqual(r, 2)
        self.assertEqual(s, ['plastic'])
    
    def test_compress_runs_4(self):
        s = ['plastic', 'cardboard', 'glass', 'metal', 'paper']
        r = compress_runs(s)
        self.assertEqual(r, 0)
        self.assertEqual(s, ['plastic', 'cardboard', 'glass', 'metal', 'paper'])

    def test_stitch_short_routes_1(self):
        day = [["Ash", "Birch"], ["Cedar"], ["Dover", "Elm", "Fir"]]
        merges = stitch_short_routes(day, 2)
        self.assertEqual(merges, 1)
        self.assertEqual(day, [["Ash", "Birch"], ["Cedar", "Dover", "Elm", "Fir"]])
    
    def test_stitch_short_routes_2(self):
        day = [["Ash"], ["Birch"], ["Cedar"], ["Dover"], ["Elm"], ["Fir"]]
        merges = stitch_short_routes(day, 2)
        self.assertEqual(merges, 3)
        self.assertEqual(day, [['Ash', 'Birch'], ['Cedar', 'Dover'], ['Elm', 'Fir']])
    
    def test_stitch_short_routes_3(self):
        day = [["Ash", "Birch", "Cedar"], ["Dover", "Elm", "Fir"]]
        merges = stitch_short_routes(day, 2)
        self.assertEqual(merges, 0)
        self.assertEqual(day, [["Ash", "Birch", "Cedar"], ["Dover", "Elm", "Fir"]])
    
    def test_balance_load_1(self):
        day = [["A", "B", "C", "D"], ["E"], ["F", "G"]]
        moves = balance_load(day)
        self.assertEqual(moves, 1)
        self.assertEqual(day, [["A", "B", "C"], ["E", "D"], ["F", "G"]])

    def test_balance_load_2(self):
        day = [["Ash", "Birch", "Cedar"], ["Dover", "Elm", "Fir"]]
        moves = balance_load(day)
        self.assertEqual(moves, 0)
        self.assertEqual(day, [["Ash", "Birch", "Cedar"], ["Dover", "Elm", "Fir"]])
    
    def test_balance_load_3(self):
        day = [["Ash", "Birch", "Cedar", "Dover"], ["Elm"], ["Fir"]]
        moves = balance_load(day)
        self.assertEqual(moves, 2)
        self.assertEqual(day, [["Ash", "Birch"], ["Elm", "Dover"], ["Fir", "Cedar"]])
    
    def test_balance_load_4(self):
        day = [["Ash", "Birch", "Cedar", "Dover"], ["Fir"], ["Elm", "Grove"]]
        moves = balance_load(day)
        self.assertEqual(moves, 1)
        self.assertEqual(day, [["Ash", "Birch", "Cedar"], ["Fir", "Dover"], ["Elm", "Grove"]])

    def test_cancel_street_1(self):
        day = [["Ash", "Birch", "Cedar"], ["Dover"], ["Birch", "Elm"]]
        removed = cancel_street(day, "Birch")
        self.assertEqual(removed, 2)
        self.assertEqual(day, [["Ash", "Cedar"], ["Dover"], ["Elm"]])

    def test_cancel_street_2(self):
        day = [["Ash", "Birch", "Cedar"], ["Dover"], ["Elm"]]
        removed = cancel_street(day, "Elm")
        self.assertEqual(removed, 1)
        self.assertEqual(day, [["Ash", "Birch", "Cedar"], ["Dover"]])
    
    def test_cancel_street_3(self):
        day = [["Ash", "Birch", "Elm"], ["Dover"], ["Elm"]]
        removed = cancel_street(day, "Elm")
        self.assertEqual(removed, 2)
        self.assertEqual(day, [["Ash", "Birch"], ["Dover"]])
    
    def test_cancel_street_4(self):
        day = [["Ash", "Birch", "Elm"], ["Dover"], ["Elm"]]
        removed = cancel_street(day, "Grove")
        self.assertEqual(removed, 0)
        self.assertEqual(day, [["Ash", "Birch", "Elm"], ["Dover"], ["Elm"]])

    def test_enqueue_1(self):
        q = []
        n = enqueue_all(q, ["plastic", "food"]) 
        self.assertEqual(n, 2)
        self.assertEqual(q, ["plastic", "food"])
    
    def test_enqueue_2(self):
        q = ['plastic', 'food']
        n = enqueue_all(q, ['plastic', 'cardboard', 'glass'])
        self.assertEqual(n, 5)
        self.assertEqual(q, ['plastic', 'food', 'plastic', 'cardboard', 'glass'])
    
    def test_enqueue_3(self):
        q = ['plastic', 'plastic']
        n = enqueue_all(q, ['glass', 'glass'])
        self.assertEqual(n, 4)
        self.assertEqual(q, ['plastic', 'plastic', 'glass', 'glass'])

    def test_fast_forward_1(self):
        q = ["p", "f", "c"]
        out = fast_forward(q, 2)
        self.assertEqual(out, ["p", "f"])
        self.assertEqual(q, ["c"])
    
    def test_fast_forward_2(self):
        q = ['plastic', 'food', 'cardboard', 'glass']
        out = fast_forward(q, 5)
        self.assertEqual(out, ['plastic', 'food', 'cardboard', 'glass'])
        self.assertEqual(q, [])
    
    def test_fast_forward_3(self):
        q = ['plastic', 'plastic', 'plastic']
        out = fast_forward(q, 1)
        self.assertEqual(out, ['plastic'])
        self.assertEqual(q, ['plastic', 'plastic'])

    def test_prioritize_1(self):
        q = ["plastic", "food", "cardboard", "food"]
        prioritize(q, lambda x: x == "food")
        self.assertEqual(q, ["food", "food", "plastic", "cardboard"])

    def test_prioritize_2(self):
        q = ['plastic', 'cardboard', 'glass']
        prioritize(q, lambda x: x == 'metal')
        self.assertEqual(q, ['plastic', 'cardboard', 'glass'])
    
    def test_prioritize_3(self):
        q = ['plastic', 'plastic', 'plastic']
        prioritize(q, lambda x: x == 'plastic')
        self.assertEqual(q, ['plastic', 'plastic', 'plastic'])
    
    def test_prioritize_4(self):
        q = ['plastic', 'food', 'plastic', 'food', 'cardboard', 'food']
        prioritize(q, lambda x: x == 'food')
        self.assertEqual(q, ['food', 'food', 'food', 'plastic', 'plastic', 'cardboard'])

    def test_edge_cases(self):
        a = []
        normalize(a); self.assertEqual(a, [])
        self.assertEqual(compress_runs(a), 0)
        day = []
        self.assertEqual(balance_load(day), 0)
        self.assertEqual(stitch_short_routes(day, 3), 0)
        q = []
        self.assertEqual(fast_forward(q, 5), [])
        self.assertEqual(q, [])

    def test_routes_scaling(self):
        day = [ [f"S{i}_{j}" for j in range(k)] for i,k in enumerate([1,2,5,1,4,1,6,2,1,4]) ]
        stitch_short_routes(day, 3)
        # After balancing, lengths differ by at most 1
        balance_load(day)
        lens = list(map(len, day))
        self.assertLessEqual(max(lens)-min(lens), 1)

    def test_queue_ops(self):
        q = []
        enqueue_all(q, ['plastic']*3 + ['food']*4 + ['glass'])
        removed = fast_forward(q, 2)
        self.assertEqual(removed, ['plastic','plastic'])
        prioritize(q, lambda x: x=='food')
        self.assertTrue(q[:4] == ['food']*4)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestPS3))
    result = unittest.TextTestRunner(verbosity=2, resultclass=Results_600).run(suite)
    print("\n\nProblem Set 3 Unit Test Results:")
    print(result.getOutput())
    print("Points for these tests: %s/40" % result.getPoints())
