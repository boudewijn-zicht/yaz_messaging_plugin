from .tester import TestCase


class TestSync(TestCase):
    files = {
        "sync.nl.yml": """
controller:
    action:
        description_a: a
""".lstrip(),
        "sync.en.yml": """
controller:
    action:
        description_b: b
""".lstrip()
    }

    def test_010_cleanup__ignore(self):
        expected_nl = """
controller:
    action:
        description_a: a
""".lstrip()

        expected_en = """
controller:
    action:
        description_b: b
""".lstrip()

        caller = self.get_caller()
        caller("cleanup", "--changes", "overwrite", "--sync", "ignore")
        self.assertEqual(expected_nl, self.get_file_content("sync.nl.yml"))
        self.assertEqual(expected_en, self.get_file_content("sync.en.yml"))

    def test_020_cleanup__use_key(self):
        expected_nl = """
controller:
    action:
        description_a: a
        description_b: controller.action.description_b
""".lstrip()

        expected_en = """
controller:
    action:
        description_a: controller.action.description_a
        description_b: b
""".lstrip()

        caller = self.get_caller()
        caller("cleanup", "--changes", "overwrite", "--sync", "use-key")
        self.assertEqual(expected_nl, self.get_file_content("sync.nl.yml"))
        self.assertEqual(expected_en, self.get_file_content("sync.en.yml"))

    def test_030_cleanup__fail(self):
        args = (self.get_caller(), "cleanup", "--sync", "fail")
        self.assertRaisesRegex(RuntimeError, r"Translatable .* is not set in .*", *args)
