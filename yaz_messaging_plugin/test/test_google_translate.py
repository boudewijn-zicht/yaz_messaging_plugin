import yaz
from .tester import TestCase


class TestGoogleTranslate(TestCase):
    files = {
        "translate.nl.yml": """
controller:
    action:
        hello_world: Hallo Wereld
""".lstrip(),
        "translate.en.yml": """
controller:
    action:
        quick: The quick brown fox jumps over the lazy dog
""".lstrip()
    }

    def test_010_cleanup__google_translate(self):
        expected_nl = """
controller:
    action:
        hello_world: Hallo Wereld
        quick: De snelle bruine vos springt over de luie hond
""".lstrip()

        expected_en = """
controller:
    action:
        hello_world: Hello World
        quick: The quick brown fox jumps over the lazy dog
""".lstrip()

        caller = self.get_caller()
        caller("cleanup", "--changes", "overwrite", "--sync", "google-translate")
        self.assertEqual(expected_nl, self.get_file_content("translate.nl.yml"))
        self.assertEqual(expected_en, self.get_file_content("translate.en.yml"))

class TestGoogleTranslateWithPlaceholders(TestCase):
    files = {
        "translate.nl.yml": """
controller:
    action:
        greeting_a: Hallo %username%
        greeting_b: Hallo %username%, het is vandaag %today% en je hebt nog %thingsTodo% dingen te doen
""".lstrip(),
        "translate.en.yml": ""
    }

    def test_010_cleanup__google_translate(self):
        expected_en = """
controller:
    action:
        greeting_a: Hello %username%
        greeting_b: Hello %username%, today %today% and you have to do it %thingsTodo% things
""".lstrip()

        caller = self.get_caller()
        caller("cleanup", "--changes", "overwrite", "--sync", "google-translate")
        self.assertEqual(expected_en, self.get_file_content("translate.en.yml"))
