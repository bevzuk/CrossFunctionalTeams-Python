import unittest

from task_status import TaskStatus
from tests.dsl.given import Given


class WhenDoWork(unittest.TestCase):
    def test_backlog_item_task_is_done(self):
        scrum_team = Given.scrum_team().with_developer("Homer", "A").please()
        backlog = Given.product_backlog().with_item("US1", "A").please()

        scrum_team.plan_day(backlog)

        task = backlog.items()[0].tasks()[0]
        self.assertEqual(TaskStatus.Done, task.status())


if __name__ == '__main__':
    unittest.main()
