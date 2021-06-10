from unittest import TestCase

from CPU import CPU


class ResourceTest(TestCase):
    def setUp(self) -> None:
        self.cpu_object = CPU("cpu_name", "cpu_manufacturer", 15, 8, 4, "socket", 200)

    def test_category(self):
        print(self.cpu_object.category())
