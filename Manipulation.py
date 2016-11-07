import Patient_Doctor_Allocation as original
import random
import copy

print '\n Manipulation Starts\n'

#print original.patient_list_with_preference
#print original.doctor_list_with_preference

number_of_agents=original.no_of_patients/2
selected=[]

plot_data1=open("plot_manipulated_random_eff_loss_nby2_with_100.dat","a")
plot_data2=open("plot_manipulated_random_eff_loss_nby4_with_100.dat","a")
plot_data3=open("plot_manipulated_random_eff_loss_nby8_with_100.dat","a")

copy_patient_list_with_preference_for_nby2=copy.deepcopy(original.patient_list_with_preference)

print 'For N/2\n'

for i in range(number_of_agents):
	
	random_patient = random.randrange(0,original.no_of_patients)
	if random_patient in selected:
		random_patient = random.randrange(0,original.no_of_patients)
	selected.append(random_patient)

	random.shuffle(copy_patient_list_with_preference_for_nby2[random_patient])
	#original.patient_list_with_preference[random_patient]

#print original.patient_list_with_preference
del selected[:]

val1 = original.random_alloc(copy_patient_list_with_preference_for_nby2,original.doctor_list_with_preference)
plot_data1.write("%s %s\n" %(original.no_of_doctors,(val1)))



copy_patient_list_with_preference_for_nby4=copy.deepcopy(original.patient_list_with_preference)

print 'For N/4\n'

number_of_agents=original.no_of_patients/4
selected=[]

for i in range(number_of_agents):
	
	random_patient = random.randrange(0,original.no_of_patients)
	if random_patient in selected:
		random_patient = random.randrange(0,original.no_of_patients)
	selected.append(random_patient)

	random.shuffle(copy_patient_list_with_preference_for_nby4[random_patient])
	#original.patient_list_with_preference[random_patient]

#print original.patient_list_with_preference

del selected[:]

val2=original.random_alloc(copy_patient_list_with_preference_for_nby4,original.doctor_list_with_preference)
plot_data2.write("%s %s\n" %(original.no_of_doctors,(val2)))


copy_patient_list_with_preference_for_nby8=copy.deepcopy(original.patient_list_with_preference)

print 'For N/8\n'

number_of_agents=original.no_of_patients/8
selected=[]

for i in range(number_of_agents):
	
	random_patient = random.randrange(0,original.no_of_patients)
	if random_patient in selected:
		random_patient = random.randrange(0,original.no_of_patients)
	selected.append(random_patient)

	random.shuffle(copy_patient_list_with_preference_for_nby8[random_patient])
	#original.patient_list_with_preference[random_patient]

#print original.patient_list_with_preference

val3=original.random_alloc(copy_patient_list_with_preference_for_nby8,original.doctor_list_with_preference)
plot_data3.write("%s %s\n" %(original.no_of_doctors,(val3)))