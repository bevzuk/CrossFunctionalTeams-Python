from analythics.analytics import Analytics


class AnalyticsBuilder(object):
    def please(self):
        return Analytics.__create__()
