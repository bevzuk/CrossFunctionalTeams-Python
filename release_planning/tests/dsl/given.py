from tests.dsl.product_backlog_builder import ProductBacklogBuilder
from tests.dsl.scrum_team_builder import ScrumTeamBuilder


class Given:
    @classmethod
    def scrum_team(cls):
        return ScrumTeamBuilder()

    @classmethod
    def product_backlog(cls):
        return ProductBacklogBuilder()
