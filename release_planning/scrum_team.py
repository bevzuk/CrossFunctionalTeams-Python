from developer import Developer
from events_store import EventsStore


def mutate(entity, event):
    if isinstance(event, ScrumTeam.Created):
        return event.mutate()
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

    def hire_developer(self):
        self._developers.append(Developer())

    def number_of_developers(self):
        return len(self._developers)

    class Created(object):
        def mutate(self):
            return ScrumTeam()

