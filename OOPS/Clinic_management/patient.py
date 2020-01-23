import doctor,json

class Patients(doctor.Doctor):
    def patient_list(self):
        with open('/home/user/Desktop/Fellowship/Programming/oops/Json_files/clinique.json','r') as open_file:
            data = json.load(open_file)
            for i in range(0,len(data['Patients'])):
                Name = data['Patients'][i]['Name']
                ID = data['Patients'][i]['ID']
                Number = data['Patients'][i]['Number']
                Age = data['Patients'][i]['Age']

            dict1 = {"Name":Name, "ID":ID, "Number":Number, "Age":Age}
            while True:
                print()
                print('----------- SEARCH BY ----------')
                print("""[ 1 ] Name    [ 2 ] ID     [ 3 ] Number  [ 4 ] Age [0] EXIT """)
                option = int(input('enter your choice to search = ')) 

                if option == 1:
                    s_name = input("enter the doc name you want to search = ")
                    for i in range(0,len(data['Patients'])):
                        if data['Patients'][i]['Name'] == s_name: 
                            print()
                            print(data['Patients'][i])
                            break
                        else:
                            print("No such Patients by that Name")
                            break
                    
                elif option == 2:
                    s_id = input("enter the doc ID you want to search = ")
                    for i in range(0,len(data['Patients'])):
                        if data['Patients'][i]['ID'] == s_id: 
                            print(data['Patients'][i])
                            break
                        else:
                            print("No such Patients by that ID")
                            break
                
                elif option == 3:
                    p_num = input("enter the patient Number you want to search = ")
                    for i in range(0,len(data['Patients'])):
                        if data['Patients'][i]['Number'] == p_num: 
                            print(data['Patients'][i])
                            break
                        else:
                            print("No such Patients by that number")
                            break
                
                elif option == 4:
                    p_age = input("enter the patient age you want to search = ")
                    for i in range(0,len(data['Patients'])):
                        if data['Patients'][i]['Age'] == p_age: 
                            print(data['Patients'][i])
                            break
                        else:
                            print("No such patient of that age")
                            break
                elif option == 0:
                    break

    def which_doc(self):
        with open('/home/user/Desktop/Fellowship/Programming/oops/Json_files/clinique.json','r') as open_file:
            data = json.load(open_file)
            for i in range(0,len(data['Doctors'])):
                Doc_Name = data['Doctors'][i]['Doc_Name']
                Doc_ID = data['Doctors'][i]['Doc_ID']
                Spec = data['Doctors'][i]['Spec']
                Avaliability = data['Doctors'][i]['Avaliability']

                dict1 = {"Doc_Name":Doc_Name, "Doc_ID":Doc_ID, "Spec":Spec, "Avaliability":Avaliability}
                for k,v in dict1.items():
                    print("{}:{}".format(k,v))
                    print()
                
        Doctor.validate_appointment(self)  
