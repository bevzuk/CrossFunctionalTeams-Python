from events_store import EventsStore


def mutate(entity, event):
    return ScrumTeam()


def publish(events):
    EventsStore.publish(events)


class ScrumTeam(object):
    def number_of_developers(self):
        return 1

    @classmethod
    def __create__(cls):
        event = ScrumTeam.Created()
        scrum_team = mutate(None, event)
        publish([event])
        return scrum_team

    class Created(object):
        pass
