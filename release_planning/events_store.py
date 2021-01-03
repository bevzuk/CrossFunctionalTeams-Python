def publish(events):
    EventsStore.publish(events)


class EventsStore(object):
    events = []

    @classmethod
    def publish(cls, events):
        cls.events.extend(events)
