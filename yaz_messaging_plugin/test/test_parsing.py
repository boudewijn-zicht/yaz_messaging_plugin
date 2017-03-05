import yaz
from .tester import TestCase


class TestParsingWithColon(TestCase):
    """
    The message should not contain an unquoted colon (:), this results in a parser error
    """

    files = {
        "colon.nl.yml": """
message: this line has a colon at : the end
""".lstrip()
    }

    def test_010_cleanup(self):
        caller = self.get_caller()
        with self.assertRaisesRegex(yaz.Error, r"mapping values are not allowed here"):
            caller("cleanup")


class TestParsingWithExclamationMark(TestCase):
    """
    If the message starts with an exclamation mark, this results in a parser error
    """

    files = {
        "exclamation.nl.yml": """
message: !foo should be quoted
""".lstrip()
    }

    def test_010_cleanup(self):
        caller = self.get_caller()
        with self.assertRaisesRegex(yaz.Error, r"could not determine a constructor for the tag .!foo."):
            caller("cleanup")
