from eventsourcing.domain.model.entity import DomainEntity

from developer import Developer


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
        plan = {}
        for developer in self._developers:
            plan[developer.name()] = self._plan_developer(product_backlog)
        return plan

    def _plan_developer(self, product_backlog):
        developer_plan = []
        for item in product_backlog.items():
            for task in item.tasks():
                developer_plan.append((item.name(), task))
        return developer_plan

    class DeveloperHired(DomainEntity.Event):
        def mutate(self, scrum_team):
            developer = Developer(self.__dict__["name"])
            for skill in self.__dict__["skills"]:
                developer.learn(skill)
            scrum_team._developers.append(developer)
