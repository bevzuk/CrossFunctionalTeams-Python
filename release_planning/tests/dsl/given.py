from scrum_team import ScrumTeam


class ScrumTeamBuilder(object):
    def with_developer(self):
        return self

    def please(self):
        return ScrumTeam()


class Given:
    @classmethod
    def scrum_team(cls):
        return ScrumTeamBuilder()
