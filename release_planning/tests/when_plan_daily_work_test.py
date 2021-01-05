import unittest

from eventsourcing.domain.model.events import subscribe

from scrum_team import ScrumTeam
from tests.dsl.given import Given


class WhenPlanDailyWork(unittest.TestCase):
    received_day_planned_events = []

    def is_day_planned_event(self, events):
        return all(isinstance(e, ScrumTeam.DayPlanned) for e in events)

    def setUp(self) -> None:
        self.received_day_planned_events = []
        subscribe(lambda e: self.received_day_planned_events.extend(e), predicate=self.is_day_planned_event)

    def test_plan_single_item(self):
        scrum_team = Given.scrum_team().with_developer("Homer", "A").please()
        product_backlog = Given.product_backlog().with_item("US1", "A").please()

        scrum_team.plan_day(product_backlog)
        plan = self.received_day_planned_events[0].plan

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

        scrum_team.plan_day(product_backlog)
        plan = self.received_day_planned_events[0].plan

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

        scrum_team.plan_day(product_backlog)
        plan = self.received_day_planned_events[0].plan

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

        scrum_team.plan_day(product_backlog)
        plan = self.received_day_planned_events[0].plan

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

        scrum_team.plan_day(product_backlog)
        plan = self.received_day_planned_events[0].plan

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

        scrum_team.plan_day(product_backlog)
        plan = self.received_day_planned_events[0].plan

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

        scrum_team.plan_day(product_backlog)
        plan = self.received_day_planned_events[0].plan

        self.assertEqual({
            "Homer": [("US1", "A")],
            "Marge": [("US1", "B")],
        }, plan)


if __name__ == '__main__':
    unittest.main()
