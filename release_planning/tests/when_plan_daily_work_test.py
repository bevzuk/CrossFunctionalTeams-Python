import unittest

from tests.dsl.given import Given


class WhenPlanDailyWork(unittest.TestCase):
    def test_plan_single_item(self):
        scrum_team = Given.scrum_team().with_developer("Homer", "A").please()
        product_backlog = Given.product_backlog().with_item("US1", "A").please()

        plan = scrum_team.plan_day(product_backlog)

        self.assertEqual({"Homer": [("US1", "A")]}, plan)

    def test_choose_task_matching_skill(self):
        scrum_team = Given \
            .scrum_team() \
            .with_developer("Homer", "B") \
            .please()
        product_backlog = Given \
            .product_backlog() \
            .with_item("US1", "A") \
            .with_item("US2", "B") \
            .please()

        plan = scrum_team.plan_day(product_backlog)

        self.assertEqual({"Homer": [("US2", "B")]}, plan)

    def test_when_no_work_do_nothing(self):
        scrum_team = Given \
            .scrum_team() \
            .with_developer("Homer", "A") \
            .please()
        product_backlog = Given \
            .product_backlog() \
            .with_item("US1", "B") \
            .please()

        plan = scrum_team.plan_day(product_backlog)

        self.assertEqual({"Homer": []}, plan)

    def test_one_task_for_two_developers(self):
        scrum_team = Given \
            .scrum_team() \
            .with_developer("Homer", "A") \
            .with_developer("Marge", "A") \
            .please()
        product_backlog = Given \
            .product_backlog() \
            .with_item("US1", "A") \
            .please()

        plan = scrum_team.plan_day(product_backlog)

        self.assertEqual({
            "Homer": [("US1", "A")],
            "Marge": [],
        }, plan)

    def test_two_tasks_in_single_story_for_two_developers(self):
        scrum_team = Given \
            .scrum_team() \
            .with_developer("Homer", "A") \
            .with_developer("Marge", "B") \
            .please()
        product_backlog = Given \
            .product_backlog() \
            .with_item("US1", "A", "B") \
            .please()

        plan = scrum_team.plan_day(product_backlog)

        self.assertEqual({
            "Homer": [("US1", "A")],
            "Marge": [("US1", "B")],
        }, plan)

    def test_two_tasks_in_two_stories_for_two_developers(self):
        scrum_team = Given \
            .scrum_team() \
            .with_developer("Homer", "A") \
            .with_developer("Marge", "B") \
            .please()
        product_backlog = Given \
            .product_backlog() \
            .with_item("US1", "B") \
            .with_item("US2", "A") \
            .please()

        plan = scrum_team.plan_day(product_backlog)

        self.assertEqual({
            "Homer": [("US2", "A")],
            "Marge": [("US1", "B")],
        }, plan)

    def test_tshape_developer(self):
        scrum_team = Given \
            .scrum_team() \
            .with_developer("Homer", "A") \
            .with_developer("Marge", "A", "B") \
            .please()
        product_backlog = Given \
            .product_backlog() \
            .with_item("US1", "A", "B") \
            .please()

        plan = scrum_team.plan_day(product_backlog)

        self.assertEqual({
            "Homer": [("US1", "A")],
            "Marge": [("US1", "B")],
        }, plan)


if __name__ == '__main__':
    unittest.main()
