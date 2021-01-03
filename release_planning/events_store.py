class EventsStore(object):
    events = []

    @classmethod
    def publish(cls, events):
        cls.events.extend(events)