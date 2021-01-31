from eventsourcing.domain.model.entity import DomainEntity
from eventsourcing.domain.model.events import subscribe

from product_backlog import ProductBacklog


class Analytics(DomainEntity):
    def __init__(self, **kwargs):
        super(Analytics, self).__init__(**kwargs)
        subscribe(self.calculate_analytics, self._is_backlog_done)

    def calculate_analytics(self, events):
        for _ in events:
            self._calculate_analytics()

    def _is_backlog_done(self, events):
        return all(isinstance(e, ProductBacklog.BacklogIsDone) for e in events)

    def _calculate_analytics(self):
        self.__trigger_event__(Analytics.StatisticsCalculated)

    class StatisticsCalculated(DomainEntity.Event):
        pass
