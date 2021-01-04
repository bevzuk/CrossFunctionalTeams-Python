from events_store import publish


def mutate(entity, event):
    if isinstance(event, ProductBacklog.Created):
        return event.mutate()
    if isinstance(event, ProductBacklog.ItemAdded):
        event.mutate(entity)
    else:
        raise NotImplementedError(type(event))


class ProductBacklog(object):
    def __init__(self):
        self._items = []

    @classmethod
    def __create__(cls):
        event = ProductBacklog.Created()
        product_backlog = mutate(None, event)
        publish([event])
        return product_backlog

    def add(self, item_name):
        event = ProductBacklog.ItemAdded(item_name)
        mutate(self, event)
        publish([event])

    def items(self):
        return list(self._items)

    class Item(object):
        def __init__(self, name):
            self._name = name

        def name(self):
            return self._name

    class Created(object):
        def mutate(self):
            return ProductBacklog()

    class ItemAdded(object):
        def __init__(self, name):
            self._name = name

        def mutate(self, product_backlog):
            product_backlog._items.append(ProductBacklog.Item(self._name))
