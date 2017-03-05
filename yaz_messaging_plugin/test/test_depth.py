import yaz
from .tester import TestCase


class TestDepthWithoutConflicts(TestCase):
    files = {
        "depth.nl.yml": """
double_first.double_second: b
single_first: a
triple_first.triple_second.triple_third: c
""".lstrip()
    }

    def test_010_cleanup(self):
        expected = """
double_first:
    double_second: b
single_first: a
triple_first:
    triple_second:
        triple_third: c
""".lstrip()

        caller = self.get_caller()
        caller("cleanup", "--changes", "overwrite")
        self.assertEqual(expected, self.get_file_content("depth.nl.yml"))

    def test_020_cleanup__max_depth_0(self):
        expected = """
double_first.double_second: b
single_first: a
triple_first.triple_second.triple_third: c
""".lstrip()

        caller = self.get_caller()
        caller("cleanup", "--changes", "overwrite", "--max-depth", "0")
        self.assertEqual(expected, self.get_file_content("depth.nl.yml"))

    def test_030_cleanup__max_depth_1(self):
        expected = """
double_first:
    double_second: b
single_first: a
triple_first:
    triple_second.triple_third: c
""".lstrip()

        caller = self.get_caller()
        caller("cleanup", "--changes", "overwrite", "--max-depth", "1")
        self.assertEqual(expected, self.get_file_content("depth.nl.yml"))

    def test_040_cleanup__max_depth_2(self):
        expected = """
double_first:
    double_second: b
single_first: a
triple_first:
    triple_second:
        triple_third: c
""".lstrip()

        caller = self.get_caller()
        caller("cleanup", "--changes", "overwrite", "--max-depth", "2")
        self.assertEqual(expected, self.get_file_content("depth.nl.yml"))


class TestConflictingDepth(TestCase):
    files = {
        "depth.nl.yml": """
a: A
a.b.c: ABC
""".lstrip()
    }

    def test_010_cleanup__join(self):
        expected = """
a: A
a.b:
    c: ABC
""".lstrip()

        caller = self.get_caller()
        caller("cleanup", "--changes", "overwrite", "--depth", "join")
        self.assertEqual(expected, self.get_file_content("depth.nl.yml"))

    def test_020_cleanup__fail(self):
        caller = self.get_caller()
        with self.assertRaisesRegex(yaz.Error, r"Conflicting keys when expanding path .*"):
            caller("cleanup", "--depth", "fail")
