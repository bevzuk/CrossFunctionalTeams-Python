class NaivePlanStrategy(object):
    def plan(self, developers, product_backlog):
        plan = {}
        tasks = self._linearize(product_backlog)
        for developer in developers:
            plan[developer.name()] = self._plan_developer(developer, tasks)
        return plan

    def _plan_developer(self, developer, tasks):
        developer_plan = []
        for task in tasks:
            if task[1] in developer.skills():
                developer_plan.append((task[0].name(), task[1]))
                tasks.remove(task)
        return developer_plan

    def _linearize(self, product_backlog):
        tasks = []
        for item in product_backlog.items():
            for task in item.tasks():
                tasks.append((item, task))
        return tasks