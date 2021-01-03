class Developer(object):
    def __init__(self, name):
        self._name = name
        self._skills = []

    def name(self):
        return self._name

    def skills(self):
        return list(self._skills)

    def learn(self, skill):
        self._skills.append(skill)
