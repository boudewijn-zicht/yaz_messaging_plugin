import yaz
from .tester import TestCase


class TestDuplicate(TestCase):
    files = {
        "duplicate_keys.nl.yml": """
controller.action.description_a: A
controller.action.description_b: B
controller.action.description_c: C
controller:
    action:
        description_a: a
        description_b: b
        description_c: c
    """.lstrip()
    }

    def test_010_fix__first(self):
        expected = """
controller:
    action:
        description_a: A
        description_b: B
        description_c: C
""".lstrip()

        caller = self.get_caller()
        caller("fix", "--changes", "overwrite", "--duplicate", "first")
        self.assertEqual(expected, self.get_file_content("duplicate_keys.nl.yml"))

    def test_020_fix__last(self):
        expected = """
controller:
    action:
        description_a: a
        description_b: b
        description_c: c
""".lstrip()

        caller = self.get_caller()
        caller("fix", "--changes", "overwrite", "--duplicate", "last")
        self.assertEqual(expected, self.get_file_content("duplicate_keys.nl.yml"))

    def test_030_fix__fail(self):
        caller = self.get_caller()
        with self.assertRaisesRegex(yaz.Error, r"Translatable .* has multiple possible values .*"):
            caller("fix", "--duplicate", "fail")
