import os
import tempfile

import yaz
from yaz_messaging_plugin import Messaging


class TestCase(yaz.TestCase):
    files = {}

    def setUp(self):
        self.__temporary_directory = tempfile.TemporaryDirectory()

        for filename, content in self.files.items():
            with open(os.path.join(self.__temporary_directory.name, filename), "w") as file:
                file.write(content)

        plugin = yaz.get_plugin_instance(Messaging)
        plugin.dirs = [self.__temporary_directory.name]

    def tearDown(self):
        self.__temporary_directory.cleanup()

    def get_caller(self, white_list=None):
        assert white_list is None, "Please let the tester handle this parameter"
        return super().get_caller([Messaging])

    def get_file_content(self, filename):
        with open(os.path.join(self.__temporary_directory.name, filename), "r") as file:
            return file.read()

class ClassTestCase(yaz.TestCase):
    files = {}
    __temporary_directory = None

    @classmethod
    def setUpClass(cls):
        cls.__temporary_directory = tempfile.TemporaryDirectory()

        for filename, content in cls.files.items():
            with open(os.path.join(cls.__temporary_directory.name, filename), "w") as file:
                file.write(content)

        plugin = yaz.get_plugin_instance(Messaging)
        plugin.dirs = [cls.__temporary_directory.name]

    @classmethod
    def tearDownClass(cls):
        cls.__temporary_directory.cleanup()

    def get_caller(self, white_list=None):
        assert white_list is None, "Please let the tester handle this parameter"
        return super().get_caller([Messaging])

    def get_file_content(self, filename):
        with open(os.path.join(self.__temporary_directory.name, filename), "r") as file:
            return file.read()
