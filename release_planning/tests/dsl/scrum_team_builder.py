from scrum_team import ScrumTeam


class ScrumTeamBuilder(object):
    def __init__(self):
        self._scrum_team = ScrumTeam.__create__()

    def with_developer(self):
        self._scrum_team.hire_developer("")
        return self

    def please(self):
        return self._scrum_team

