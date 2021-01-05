import unittest

from tests.dsl.given import Given


class WhenPlanDailyWork(unittest.TestCase):
    def test_plan_single_item(self):
        scrum_team = Given.scrum_team().with_developer("Homer", "A").please()
        product_backlog = Given.product_backlog().with_item("US1", "A").please()

        plan = scrum_team.plan_day(product_backlog)

        self.assertEqual({"Homer": [("US1", "A")]}, plan)


if __name__ == '__main__':
    unittest.main()
