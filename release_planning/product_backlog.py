from typing import Any, Type

from eventsourcing.domain.model.entity import DomainEntity

from events_store import publish


def mutate(entity, event):
    if isinstance(event, ProductBacklog.ItemAdded):
        event.mutate(entity)
    else:
        raise NotImplementedError(type(event))


class ProductBacklog(DomainEntity):
    def __init__(self, **kwargs):
        super(ProductBacklog, self).__init__(**kwargs)
        self._items = []

    def add(self, item_name):
        event = ProductBacklog.ItemAdded(item_name)
        mutate(self, event)
        publish([event])

    def items(self):
        return list(self._items)

    def __trigger_event__(self, event_class: Type[object], **kwargs: Any) -> None:
        event = event_class(**kwargs)
        mutate(self, event)
        publish([event])

    class Item(object):
        def __init__(self, name, tasks):
            self._name = name
            self._tasks = tasks

        def name(self):
            return self._name

        def tasks(self):
            return list(self._tasks)

    class ItemAdded(object):
        def __init__(self, name, tasks=[]):
            self._name = name
            self._tasks = tasks

        def mutate(self, product_backlog):
            product_backlog._items.append(ProductBacklog.Item(self._name, self._tasks))
