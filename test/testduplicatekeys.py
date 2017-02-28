import os.path
import tempfile
import yaz

from yaz_messaging_plugin import Messaging


class TestDuplicateKeys(yaz.TestCase):
    def create_translation_file(self, dir, filename, content):
        file_path = os.path.join(dir, filename)
        with open(file_path, "w") as file:
            file.write(content)
        return file_path

    def test_010_cleanup__overwrite__first(self):
        content = """
controller.action.description_a: A
controller.action.description_b: B
controller.action.description_c: C
controller:
    action:
        description_a: a
        description_b: b
        description_c: c
""".lstrip()

        expected = """
controller:
    action:
        description_a: A
        description_b: B
        description_c: C
""".lstrip()

        with tempfile.TemporaryDirectory() as dir:
            file_path = self.create_translation_file(dir, "duplicate_keys.nl.yml", content)

            plugin = yaz.get_plugin_instance(Messaging)
            plugin.dirs = [dir]

            caller = self.get_caller([Messaging])
            caller("cleanup", "--changes-strategy", "overwrite", "--duplicate-key-strategy", "first")

            self.assertEqual(expected, open(file_path, "r").read())

    def test_020_cleanup__overwrite__last(self):
        content = """
controller.action.description_a: A
controller.action.description_b: B
controller.action.description_c: C
controller:
    action:
        description_a: a
        description_b: b
        description_c: c
""".lstrip()

        expected = """
controller:
    action:
        description_a: a
        description_b: b
        description_c: c
""".lstrip()

        with tempfile.TemporaryDirectory() as dir:
            file_path = self.create_translation_file(dir, "duplicate_keys.nl.yml", content)

            plugin = yaz.get_plugin_instance(Messaging)
            plugin.dirs = [dir]

            caller = self.get_caller([Messaging])
            caller("cleanup", "--changes-strategy", "overwrite", "--duplicate-key-strategy", "last")

            self.assertEqual(expected, open(file_path, "r").read())
