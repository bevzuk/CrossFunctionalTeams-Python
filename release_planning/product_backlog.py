from eventsourcing.domain.model.entity import DomainEntity


class ProductBacklog(DomainEntity):
    def __init__(self, **kwargs):
        super(ProductBacklog, self).__init__(**kwargs)
        self._items = []

    def add(self, item_name, tasks):
        self.__trigger_event__(ProductBacklog.ItemAdded, name=item_name, tasks=tasks)

    def items(self):
        return self._items.copy()

    class Item(object):
        def __init__(self, name, tasks):
            self._name = name
            self._tasks = tasks

        def name(self):
            return self._name

        def tasks(self):
            return self._tasks.copy()

    class ItemAdded(DomainEntity.Event):
        def mutate(self, product_backlog) -> None:
            item = ProductBacklog.Item(self.__dict__["name"], self.__dict__["tasks"])
            product_backlog._items.append(item)
