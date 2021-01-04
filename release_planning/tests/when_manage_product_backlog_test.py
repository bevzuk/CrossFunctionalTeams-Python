import unittest

from tests.dsl.given import Given


class WhenManageProductBacklog(unittest.TestCase):
    def test_can_add_item(self):
        backlog = Given.product_backlog().please()

        backlog.add("User Story")

        self.assertEqual("User Story", backlog.items()[0].name())


if __name__ == '__main__':
    unittest.main()
