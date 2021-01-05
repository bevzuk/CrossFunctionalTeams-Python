from eventsourcing.domain.model.entity import DomainEntity

from developer import Developer


class ScrumTeam(DomainEntity):
    def __init__(self, **kwargs):
        super(ScrumTeam, self).__init__(**kwargs)
        self._developers = []

    def hire_developer(self, name="", skills=[]):
        self.__trigger_event__(ScrumTeam.DeveloperHired, name=name, skills=skills)

    def number_of_developers(self):
        return len(self._developers)

    def developers(self):
        return list(self._developers)

    class DeveloperHired(DomainEntity.Event):
        def mutate(self, scrum_team):
            developer = Developer(self.__dict__["name"])
            for skill in self.__dict__["skills"]:
                developer.learn(skill)
            scrum_team._developers.append(developer)
