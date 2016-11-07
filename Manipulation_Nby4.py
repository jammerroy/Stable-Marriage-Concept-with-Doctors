import Patient_Doctor_Allocation as original
import random

print '\n Manipulation Starts\n'

#print original.patient_list_with_preference
#print original.doctor_list_with_preference

number_of_agents=original.no_of_patients/4
selected=[]

for i in range(number_of_agents):
	
	random_patient = random.randrange(0,original.no_of_patients)
	if random_patient in selected:
		random_patient = random.randrange(0,original.no_of_patients)
	selected.append(random_patient)

	random.shuffle(original.patient_list_with_preference[random_patient])
	original.patient_list_with_preference[random_patient]

#print original.patient_list_with_preference

original.random_alloc(original.patient_list_with_preference,original.doctor_list_with_preference)
#original.patient_side_alloc(original.patient_list_with_preference,original.doctor_list_with_preference)
#original.doctor_side_alloc(original.patient_list_with_preference,original.doctor_list_with_preference)

