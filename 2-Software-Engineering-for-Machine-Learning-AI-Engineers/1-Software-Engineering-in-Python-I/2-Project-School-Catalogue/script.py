class School:
  def __init__(self, name, level, numberOfStudents):
    self._name = name
    self._level = level
    self._numberOfStudents = numberOfStudents
  
  def get_name(self):
    return self._name

  def get_level(self):
    return self._level

  def get_numberOfStudents(self):
    return self._numberOfStudents

  def set_numberOfStudents(self, numberOfStudents):
    self._numberOfStudents = numberOfStudents

  def __repr__(self):
    return(f'A {self._level} school named {self._name} with {self._numberOfStudents} students.')

test = School('IOL', 'primary', 24)

print(test)
test.set_numberOfStudents(31)
print(test)

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'primary', numberOfStudents)
    self._pickupPolicy = pickupPolicy

  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    school_repr = super().__repr__()
    return school_repr + f'The pickup policy is {self._pickupPolicy}.'

test = PrimarySchool('Eros', 24, 'from 11:30 to 13')

print(test)
test.set_numberOfStudents(31)
print(test)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self._sportsTeams = sportsTeams
  
  def get_sportsTeams(self):
    return self._sportsTeams

  def __repr__(self):
    school_repr = super().__repr__()
    return school_repr + f'And have these sports teams available: {self._sportsTeams}!'
  
test = HighSchool('Cefet', 100, ['Thunders in summer', 'Love plane', 'Chilvary of the magots'])

print(test)
test.set_numberOfStudents(31)
print(test)
