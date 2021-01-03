from developer import Developer
from events_store import EventsStore


def mutate(entity, event):
    if isinstance(event, ScrumTeam.Created):
        return event.mutate()
    elif isinstance(event, ScrumTeam.DeveloperHired):
        event.mutate(entity)
    else:
        raise NotImplementedError(type(event))


def publish(events):
    EventsStore.publish(events)


class ScrumTeam(object):
    def __init__(self):
        self._developers = []

    @classmethod
    def __create__(cls):
        event = ScrumTeam.Created()
        scrum_team = mutate(None, event)
        publish([event])
        return scrum_team

    def hire_developer(self, name):
        event = ScrumTeam.DeveloperHired(name)
        mutate(self, event)
        publish([event])

    def number_of_developers(self):
        return len(self._developers)

    def developers(self):
        return list(self._developers)

    class Created(object):
        def mutate(self):
            return ScrumTeam()

    class DeveloperHired(object):
        def __init__(self, name):
            self._name = name

        def mutate(self, scrum_team):
            scrum_team._developers.append(Developer(self._name))

