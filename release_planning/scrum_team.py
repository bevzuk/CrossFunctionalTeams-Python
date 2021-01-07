from eventsourcing.domain.model.entity import DomainEntity
from eventsourcing.domain.model.events import subscribe

from developer import Developer
from naive_plan_strategy import NaivePlanStrategy


class ScrumTeam(DomainEntity):
    def __init__(self, **kwargs):
        super(ScrumTeam, self).__init__(**kwargs)
        self._developers = []
        subscribe(self.work, self._is_day_planned_event)

    def hire_developer(self, name="", skills=None):
        if skills is None:
            skills = []
        self.__trigger_event__(ScrumTeam.DeveloperHired, name=name, skills=skills)

    def number_of_developers(self):
        return len(self._developers)

    def developers(self):
        return list(self._developers)

    def plan_day(self, product_backlog):
        plan = NaivePlanStrategy().plan(self._developers, product_backlog)
        self.__trigger_event__(ScrumTeam.DayPlanned, plan=plan)

    def work(self, events):
        for event in events:
            self._do_work(event.plan)

    def _do_work(self, plan):
        for developer in self._developers:
            self._do_developer_work(developer, plan)
        pass

    def _do_developer_work(self, developer, plan):
        tasks = plan[developer.name()]
        for task in tasks:
            self.__trigger_event__(ScrumTeam.TaskIsDone, developer=developer, task=task)

    def _is_day_planned_event(self, events):
        return all(isinstance(e, ScrumTeam.DayPlanned) and e.originator_id == self.id for e in events)

    class DeveloperHired(DomainEntity.Event):
        def mutate(self, scrum_team) -> None:
            developer = Developer(self.__dict__["name"])
            for skill in self.__dict__["skills"]:
                developer.learn(skill)
            scrum_team._developers.append(developer)

    class DayPlanned(DomainEntity.Event):
        pass

    class TaskIsDone(DomainEntity.Event):
        pass
