import os
import tempfile
import unittest

from main import load_graph, shortest_path


class LoadGraphTests(unittest.TestCase):
    def test_load_graph_builds_bidirectional_edges(self):
        csv_content = "\n".join(
            [
                "A,B,5",
                "A,D,3",
                "I,0,0",
            ]
        )

        with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8", newline="") as temp_file:
            temp_file.write(csv_content)
            filename = temp_file.name

        try:
            graph = load_graph(filename)
        finally:
            os.remove(filename)

        self.assertEqual(graph["A"]["B"], 5)
        self.assertEqual(graph["B"]["A"], 5)
        self.assertEqual(graph["A"]["D"], 3)
        self.assertEqual(graph["D"]["A"], 3)
        self.assertEqual(graph["I"], {})


class ShortestPathTests(unittest.TestCase):
    def setUp(self):
        self.graph = {
            "A": {"B": 5, "D": 3, "E": 4},
            "B": {"A": 5, "C": 4},
            "C": {"B": 4, "G": 2},
            "D": {"A": 3, "G": 6},
            "E": {"A": 4, "F": 6},
            "F": {"E": 6, "H": 5},
            "G": {"C": 2, "D": 6, "H": 3},
            "H": {"G": 3, "F": 5},
            "I": {},
        }

    def test_a_to_b(self):
        path, cost = shortest_path(self.graph, "A", "B")
        self.assertEqual(path, ["A", "B"])
        self.assertEqual(cost, 5)

    def test_b_to_a(self):
        path, cost = shortest_path(self.graph, "B", "A")
        self.assertEqual(path, ["B", "A"])
        self.assertEqual(cost, 5)

    def test_c_to_f(self):
        path, cost = shortest_path(self.graph, "C", "F")
        self.assertEqual(path, ["C", "G", "H", "F"])
        self.assertEqual(cost, 10)

    def test_f_to_g(self):
        path, cost = shortest_path(self.graph, "F", "G")
        self.assertEqual(path, ["F", "H", "G"])
        self.assertEqual(cost, 8)

    def test_f_to_c(self):
        path, cost = shortest_path(self.graph, "F", "C")
        self.assertEqual(path, ["F", "H", "G", "C"])
        self.assertEqual(cost, 10)

    def test_unreachable_node_returns_none(self):
        path, cost = shortest_path(self.graph, "A", "I")
        self.assertIsNone(path)
        self.assertIsNone(cost)

    def test_unknown_node_returns_none(self):
        path, cost = shortest_path(self.graph, "A", "Z")
        self.assertIsNone(path)
        self.assertIsNone(cost)


if __name__ == "__main__":
    unittest.main()
