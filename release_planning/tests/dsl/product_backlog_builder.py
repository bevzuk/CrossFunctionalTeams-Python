from product_backlog import ProductBacklog


class ProductBacklogBuilder(object):
    def __init__(self):
        self._backlog = ProductBacklog.__create__()

    def with_item(self, name, *tasks):
        self._backlog.__trigger_event__(ProductBacklog.ItemAdded, name=name,
                                        tasks=list(map(lambda t: ProductBacklog.Task(t), tasks)))
        return self

    def please(self):
        return self._backlog

