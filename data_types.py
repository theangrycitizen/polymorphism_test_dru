class medicine(object):
	def __init__(self, meds = None):
		self.medicine_type = meds

		if self.medicine_type != 'Pills':
			self.medicine_type = 'Intravenous'

# Inheritance
class medicines(medicines):

# Encapsulation
	__dose = 0  

	def prescription_dosage(self):
		print "Practitioner's Prescription"

	def set_dosage(self, dose):
		self.__dose = dose

	def get_dose_num(self):
		return self.__dose


class tablets(capsules):
	__dose = 0

	def prescription_dosage(self):
		print "Take 3 pills or as directed by doctor"

	def set_dose_num(self, dose):
		self.__dose = dose

	def get_dose_num(self):
		return self.__dose

# using a function to show polymorphism?

def medicine_dosage(amount_of_dosage):
	return medicine_dosage.prescription_dosage()