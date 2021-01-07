import unittest

from scrum_team import ScrumTeam
from tests.dsl.given import Given


class WhenDayWorkIsDone(unittest.TestCase):
    def test_done_items_are_removed(self):
        backlog = Given \
            .product_backlog() \
            .with_item("US1", "A") \
            .with_item("US2", "B") \
            .please()
        backlog.items()[0].tasks()[0].done()
        scrum_team = Given.scrum_team().please()

        scrum_team.__trigger_event__(ScrumTeam.DayWorkIsDone)

        self.assertEqual(1, len(backlog.items()))
        self.assertEqual("US2", backlog.items()[0].name())

    def test_done_tasks_are_removed(self):
        backlog = Given \
            .product_backlog() \
            .with_item("US1", "A", "B") \
            .please()
        backlog.items()[0].tasks()[0].done()
        scrum_team = Given.scrum_team().please()

        scrum_team.__trigger_event__(ScrumTeam.DayWorkIsDone)

        self.assertEqual(1, len(backlog.items()[0].tasks()))
        self.assertEqual("B", backlog.items()[0].tasks()[0].name())


if __name__ == '__main__':
    unittest.main()
