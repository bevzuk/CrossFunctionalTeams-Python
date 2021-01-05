from scrum_team import ScrumTeam


class ScrumTeamBuilder(object):
    def __init__(self):
        self._scrum_team = ScrumTeam.__create__()

    def with_developer(self, name="", *skills):
        self._scrum_team.__trigger_event__(ScrumTeam.DeveloperHired, name=name, skills=list(skills))
        return self

    def please(self):
        return self._scrum_team
