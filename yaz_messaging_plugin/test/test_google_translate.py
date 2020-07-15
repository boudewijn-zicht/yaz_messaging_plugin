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

    def test_010_fix__google_translate(self):
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
        caller("fix", "--changes", "overwrite", "--sync", "google-translate")
        self.assertEqual(expected_nl, self.get_file_content("translate.nl.yml"))
        self.assertEqual(expected_en, self.get_file_content("translate.en.yml"))

class TestGoogleTranslateWithEmptyString(TestCase):
    files = {
        "translate.nl.yml": """
controller:
    action:
        empty: ''
""".lstrip(),
        "translate.en.yml": ""
    }

    def test_010_fix__google_translate(self):
        expected_nl = """
controller:
    action:
        empty: ''
""".lstrip()

        expected_en = """
controller:
    action:
        empty: ''
""".lstrip()

        caller = self.get_caller()
        caller("fix", "--changes", "overwrite", "--sync", "google-translate")
        self.assertEqual(expected_nl, self.get_file_content("translate.nl.yml"))
        self.assertEqual(expected_en, self.get_file_content("translate.en.yml"))

class TestGoogleTranslateWithPlaceholders(TestCase):
    files = {
        "translate.nl.yml": """
controller:
    action:
        farewell_a: Tot ziens !username
        farewell_b: Tot ziens !username, het was leuk dat je er was
        greeting_a: Hallo %username%
        greeting_b: Hallo %username%, het is vandaag %today% en je hebt nog %thingsTodo% dingen te doen
""".lstrip(),
        "translate.en.yml": ""
    }

    def test_010_fix__google_translate(self):
        expected_en = """
controller:
    action:
        farewell_a: Bye !username
        farewell_b: Goodbye !username, it was nice that you had
        greeting_a: Hello %username%
        greeting_b: Hello %username%, today %today% and you have to do it %thingsTodo% things
""".lstrip()

        caller = self.get_caller()
        caller("fix", "--changes", "overwrite", "--sync", "google-translate")
        self.assertEqual(expected_en, self.get_file_content("translate.en.yml"))
