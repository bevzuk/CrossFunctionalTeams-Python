from product_backlog import ProductBacklog


class ProductBacklogBuilder(object):
    def please(self):
        return ProductBacklog.__create__()

