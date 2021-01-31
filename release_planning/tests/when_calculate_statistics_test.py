import unittest

from eventsourcing.domain.model.events import subscribe

from analythics.analytics import Analytics
from product_backlog import ProductBacklog
from tests.dsl.given import Given


class WhenCalculateStatistics(unittest.TestCase):
    def test_calculate_statistics_when_backlog_is_done(self):
        received_statistics_calculated_events = []
        subscribe(
            lambda e: received_statistics_calculated_events.extend(e),
            predicate=lambda events: all(isinstance(e, Analytics.StatisticsCalculated) for e in events))
        product_backlog = Given.product_backlog().please()
        analytics = Given.analytics().please()

        product_backlog.__trigger_event__(ProductBacklog.BacklogIsDone)

        self.assertEqual(1, len(received_statistics_calculated_events))


if __name__ == '__main__':
    unittest.main()
