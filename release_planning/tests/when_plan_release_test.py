import unittest

from tests.dsl.given import Given


class WhenPlanRelease(unittest.TestCase):
    def test_can_hire_developer(self):
        scrum_team = Given\
            .scrum_team()\
            .with_developer()\
            .please()

        self.assertEqual(1, scrum_team.number_of_developers())

    def test_can_hire_developer_with_name(self):
        scrum_team = Given\
            .scrum_team()\
            .please()

        scrum_team.hire_developer("Homer")

        self.assertEqual("Homer", scrum_team.developers()[0].name())


if __name__ == '__main__':
    unittest.main()
