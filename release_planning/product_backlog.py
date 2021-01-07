from eventsourcing.domain.model.entity import DomainEntity
from eventsourcing.domain.model.events import subscribe

from scrum_team import ScrumTeam
from task_status import TaskStatus


class ProductBacklog(DomainEntity):
    def __init__(self, **kwargs):
        super(ProductBacklog, self).__init__(**kwargs)
        self._items = []
        subscribe(self.task_is_done, self._is_task_is_done_event)
        subscribe(self.day_work_is_done, self._is_day_work_is_done_event)

    def add(self, item_name, tasks):
        self.__trigger_event__(ProductBacklog.ItemAdded, name=item_name, tasks=tasks)

    def items(self):
        return self._items.copy()

    def task_is_done(self, events):
        for event in events:
            self._handle_done_task(event.task)

    def day_work_is_done(self, events):
        for event in events:
            self._handle_day_work_is_done()

    def _handle_day_work_is_done(self):
        self._remove_items_with_done_tasks()
        self._remove_done_tasks()

    def _remove_done_tasks(self):
        for item in self._items:
            item.remove_done_tasks()

    def _remove_items_with_done_tasks(self):
        for item in self._items:
            if all(t.status() == TaskStatus.Done for t in item.tasks()):
                self._items.remove(item)

    def _handle_done_task(self, task):
        item = self._find_item_by_name(task[0])
        if item is None:
            return
        for item_task in item.tasks():
            if item_task.name() == task[1]:
                item_task.done()

    def _find_item_by_name(self, item_name):
        for item in self._items:
            if item.name() == item_name:
                return item
        return None

    def _is_task_is_done_event(self, events):
        return all(isinstance(e, ScrumTeam.TaskIsDone) for e in events)

    def _is_day_work_is_done_event(self, events):
        return all(isinstance(e, ScrumTeam.DayWorkIsDone) for e in events)

    class ProductBacklogItem(object):
        def __init__(self, name, tasks):
            self._name = name
            self._tasks = tasks

        def name(self):
            return self._name

        def tasks(self):
            return self._tasks.copy()

        def remove_done_tasks(self):
            for task in self._tasks:
                if task.status() == TaskStatus.Done:
                    self._tasks.remove(task)

    class Task(object):
        def __init__(self, name):
            self._name = name
            self._status = TaskStatus.New

        def name(self):
            return self._name

        def status(self):
            return self._status

        def done(self):
            self._status = TaskStatus.Done

    class ItemAdded(DomainEntity.Event):
        def mutate(self, product_backlog) -> None:
            item = ProductBacklog.ProductBacklogItem(self.__dict__["name"], self.__dict__["tasks"])
            product_backlog._items.append(item)
