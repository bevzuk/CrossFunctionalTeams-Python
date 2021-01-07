import unittest

from tests.dsl.given import Given


class WhenManageProductBacklog(unittest.TestCase):
    def test_can_add_item(self):
        backlog = Given \
            .product_backlog() \
            .with_item("User Story") \
            .please()

        self.assertEqual("User Story", backlog.items()[0].name())

    def test_can_add_item_with_tasks(self):
        backlog = Given\
            .product_backlog()\
            .with_item("User Story", "A", "B", "C")\
            .please()

        self.assertEqual(["A", "B", "C"], list(map(lambda t: t.name(), backlog.items()[0].tasks())))


if __name__ == '__main__':
    unittest.main()
