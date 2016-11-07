import networkx as nx
import numpy as np
import copy
import random
import matplotlib.pyplot as plt

no_of_patients=500
no_of_doctors=500
total_no=no_of_doctors+no_of_patients

eff_loss_random=[]
eff_loss_algo=[]
eff_loss_algo2=[]
first_preference_random=[]
first_preference_algo=[]
first_preference_algo2=[]

"""THIS FUNCTION IS RANDOMONLY ALLOCATING DOCTORS TO PATIENTS"""

def random_alloc(patient_list_with_preference,doctor_list_with_preference):
	
	selected=[]
	doctors_alloted_to_patients=[]

	for i in range(no_of_patients):
		
		random_doctor=random.randrange(0,no_of_doctors)
		
		while random_doctor in selected:
			random_doctor=random.randrange(0,no_of_doctors)	

		doctors_alloted_to_patients.append(random_doctor+no_of_doctors)
		selected.append(random_doctor)

	#print 'Randomly Allocated',doctors_alloted_to_patients

	sum=0
	count=0

	for i in range(no_of_patients):
		pos=patient_list_with_preference[i].index(doctors_alloted_to_patients[i])
		
		if pos==0:
			count=count+1
		
		sum=sum+pos

	print 'First Preference',count	
	first_preference_random.append(count)

	print 'Efficieny Loss',sum
	eff_loss_random.append(sum)
	return sum

	del selected[:]
	del doctors_alloted_to_patients[:]

"""
	
	THIS FUNCTION IMPLEMENTS PART FROM THE PATIENTS SIDE

	FIRST FIVE NODES IN THE GRAPH (0-no_of_patients-1) ARE PATIENTS 
	NEXT FIVE NODES IN THE GRAPH (no_of_doctors-total_no) ARE DOCTORS
	
"""

def patient_side_alloc(patient_list_with_preference,doctor_list_with_preference):

	G=nx.Graph()
	
	for i in range(no_of_patients+no_of_doctors):
		G.add_node(i)

	doctors_alloted_to_patients=[]

	for i in range(no_of_patients):
		alloted_doctor=patient_list_with_preference[i][0]
		doctors_alloted_to_patients.append(alloted_doctor)
		G.add_edge(i,alloted_doctor)

	flag=0
	flag2=1
	count=[]

	for i in range(no_of_patients):
		count.append(1)

	while flag2==1:

		flag2=0

		for i in range(no_of_doctors):
			
			mini=100
			doctor_no=i+no_of_doctors
			flag=0
			degree_of_doctor=G.degree(doctor_no)
			#print 'For Doctor no.',doctor_no

			if degree_of_doctor>1:
				
				flag2=1
				patients_connected=G[doctor_no]
				patients_connected2=copy.deepcopy(patients_connected)
				
				for x in patients_connected2:
					
					pos=doctor_list_with_preference[doctor_no-no_of_doctors].index(x)
					#print 'For patient',x,'position is',pos
					
					if flag==0:
						mini=pos
						flag=1
						continue

					if pos<mini:
						remove = doctor_list_with_preference[doctor_no-no_of_doctors][mini]
						G.remove_edge(remove,doctor_no)
						mini=pos
					else:
						remove = doctor_list_with_preference[doctor_no-no_of_doctors][pos]
						G.remove_edge(remove,doctor_no)
						
		if flag2==0:
			break

		for i in range(no_of_patients):

			patient_no=i
			degree_of_patient=G.degree(patient_no)
			if degree_of_patient==0:
				
				alloted_doctor=patient_list_with_preference[i][count[patient_no]]
				count[patient_no]=count[patient_no]+1
				
				G.add_edge(i,alloted_doctor)

	#print 'Patients who got their preferences',count
	
	print 'First Preference', count.count(1)	
	first_preference_algo.append(count.count(1))
	
	sum=0
	for i in range(no_of_patients):
		index=count[i]-1
		sum=sum+index

	print 'Efficieny Loss',sum
	eff_loss_algo.append(sum)

	del count[:]
	del doctors_alloted_to_patients[:]
	
"""
	
THIS FUNCTION IMPLEMENTS PART FROM THE DOCTORS SIDE

FIRST FIVE NODES IN THE GRAPH (0-no_of_patients-1) ARE PATIENTS 
NEXT FIVE NODES IN THE GRAPH (no_of_doctors-total_no) ARE DOCTORS
	
"""

def doctor_side_alloc(patient_list_with_preference,doctor_list_with_preference):

	F=nx.Graph()

	for i in range(no_of_patients+no_of_doctors):
		F.add_node(i)

	patients_alloted_to_doctors=[]

	for i in range(no_of_doctors):
		alloted_patient=doctor_list_with_preference[i][0]
		patients_alloted_to_doctors.append(alloted_patient)
		F.add_edge(i+no_of_doctors,alloted_patient)

	#print 'Under Algorithm starts here',patients_alloted_to_doctors

	flag=0
	flag2=1
	count2=[]

	for i in range(no_of_doctors):
		count2.append(1)

	while flag2==1:

		flag2=0

		for i in range(no_of_patients):
			
			mini=100
			patient_no=i
			flag=0
			degree_of_patient=F.degree(patient_no)
			#print 'For Patient no.',patient_no

			if degree_of_patient>1:
				
				flag2=1
				doctors_connected=F[patient_no]
				doctors_connected2=copy.deepcopy(doctors_connected)
				#print patient_no,doctors_connected2

				for x in doctors_connected2:

					pos=patient_list_with_preference[patient_no].index(x)
					#print 'For patient',x,'position is',pos
					
					if flag==0:
						mini=pos
						flag=1
						continue

					if pos<mini:
						remove = patient_list_with_preference[patient_no][mini]
						F.remove_edge(remove,patient_no)
						mini=pos
					else:
						remove = patient_list_with_preference[patient_no][pos]
						F.remove_edge(remove,patient_no)
						
		if flag2==0:
			break

		for i in range(no_of_doctors):

			doctor_no=i+no_of_doctors
			degree_of_doctor=F.degree(doctor_no)
			if degree_of_doctor==0:

				alloted_patient=doctor_list_with_preference[i][count2[i]]
				count2[i]=count2[i]+1
				
				F.add_edge(doctor_no,alloted_patient)

	#print 'Patients who got their preferences',count2
	
	print 'First Preference', count2.count(1)	
	first_preference_algo2.append(count2.count(1))
	
	sum=0
	for i in range(no_of_doctors):
		index=count2[i]-1
		sum=sum+index

	print 'Efficieny Loss',sum
	eff_loss_algo2.append(sum)


	del patients_alloted_to_doctors[:]
	del count2[:]


"""MAIN FUNCTION"""

for i in range(1):

	patient_list_with_preference = [[0 for x in range(no_of_patients)] for y in range(no_of_doctors)] 
	doctor_list_with_preference = [[0 for x in range(no_of_patients)] for y in range(no_of_doctors)]

	taken_once=[]

	for i in range(no_of_patients):
		for j in range(no_of_doctors):
			random_doctor=random.randrange(0,no_of_doctors)
			if random_doctor not in taken_once:
				taken_once.append(random_doctor)
				patient_list_with_preference[i][j]=random_doctor+no_of_doctors
			else:
				while random_doctor in taken_once:
					random_doctor=random.randrange(0,no_of_doctors)
			taken_once.append(random_doctor)
			patient_list_with_preference[i][j]=random_doctor+no_of_doctors
		del taken_once[:]

	#print 'Doctors that the Patients Prefer: ', patient_list_with_preference			

	del taken_once[:]

	for i in range(no_of_doctors):
		for j in range(no_of_patients):
			random_patient=random.randrange(0,no_of_patients)
			if random_patient not in taken_once:
				taken_once.append(random_patient)
				doctor_list_with_preference[i][j]=random_patient
			else:
				while random_patient in taken_once:
					random_patient=random.randrange(0,no_of_patients)
				taken_once.append(random_patient)
				doctor_list_with_preference[i][j]=random_patient	
		del taken_once[:]

	del taken_once[:]

	#print 'Patients that the Doctors prefer: ', doctor_list_with_preference	

	random_alloc(patient_list_with_preference,doctor_list_with_preference)

	patient_side_alloc(patient_list_with_preference,doctor_list_with_preference)

	doctor_side_alloc(patient_list_with_preference,doctor_list_with_preference)



plot_data1=open("plot_algo_eff_loss_with_100.dat","a")
plot_data2=open("plot_algo2_eff_loss_with_100.dat","a")
plot_data3=open("plot_random_eff_loss_with_100.dat","a")

print 'Efficieny Loss\n'

print eff_loss_random
print eff_loss_algo
print eff_loss_algo2

plot_data1.write("%s %s\n" %(no_of_doctors,((eff_loss_algo))))
plot_data2.write("%s %s\n" %(no_of_doctors,((eff_loss_algo2))))
plot_data3.write("%s %s\n" %(no_of_doctors,((eff_loss_random))))

"""
print "\nBest Allocation"

plot_data4=open("plot_algo_best.dat","a")
plot_data5=open("plot_algo2_best.dat","a")
plot_data6=open("plot_random_best.dat","a")

print np.mean(first_preference_random)
print np.mean(first_preference_algo)
print np.mean(first_preference_algo2)

plot_data4.write("%s\n" %((np.mean(first_preference_algo))))
plot_data5.write("%s\n" %((np.mean(first_preference_algo2))))
plot_data6.write("%s\n" %((np.mean(first_preference_random))))
"""

"""
nx.draw(G,with_labels=True,node_size=500)
plt.show()

nx.draw(F,with_labels=True,node_size=500)
plt.show()


"""