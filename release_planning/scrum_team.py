from eventsourcing.domain.model.entity import DomainEntity

from developer import Developer
from naive_plan_strategy import NaivePlanStrategy


class ScrumTeam(DomainEntity):
    def __init__(self, **kwargs):
        super(ScrumTeam, self).__init__(**kwargs)
        self._developers = []

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

    class DeveloperHired(DomainEntity.Event):
        def mutate(self, scrum_team) -> None:
            developer = Developer(self.__dict__["name"])
            for skill in self.__dict__["skills"]:
                developer.learn(skill)
            scrum_team._developers.append(developer)

    class DayPlanned(DomainEntity.Event):
        pass
