import json

class Doctor:
    def doctor_list(self):
        with open('/home/user/Desktop/Fellowship/Programming/oops/Json_files/clinique.json','r') as open_file:
            data = json.load(open_file)
            for i in range(0,len(data['Doctors'])):
                Doc_Name = data['Doctors'][i]['Doc_Name']
                Doc_ID = data['Doctors'][i]['Doc_ID']
                Spec = data['Doctors'][i]['Spec']
                Avaliability = data['Doctors'][i]['Avaliability']

            dict1 = {"Doc_Name":Doc_Name, "Doc_ID":Doc_ID, "Spec":Spec, "Avaliability":Avaliability}
            while True:
                print()
                print('----------- SEARCH BY ----------')
                print("""[ 1 ] Name    [ 2 ] ID     [ 3 ] Spec  [ 4 ] Avaliability [0] EXIT """)
                option = int(input('enter your choice to search = ')) 

                if option == 1:
                    s_name = input("enter the DOCTOR name you want to search = ")
                    for i in range(0,len(data['Doctors'])):
                        if data['Doctors'][i]['Doc_Name'] == s_name: 
                            print()
                            print(data['Doctors'][i])
                            break
                        else:
                            print("No such Doctor")
                    
                elif option == 2:
                    s_id = input("enter the doc ID you want to search = ")
                    for i in range(0,len(data['Doctors'])):
                        if data['Doctors'][i]['Doc_ID'] == s_id: 
                            print(data['Doctors'][i])
                            break
                        else:
                            print("No such Doctor ID")
                
                elif option == 3:
                    s_spec = input("enter the doc SPEC you want to search = ")
                    for i in range(0,len(data['Doctors'])):
                        if data['Doctors'][i]['Spec'] == s_spec: 
                            print(data['Doctors'][i])
                            break
                        else:
                            print("No such Doctor by spec")
                
                elif option == 4:
                    s_aval = input("enter the doc Avaliability you want to search = ")
                    for i in range(0,len(data['Doctors'])):
                        if data['Doctors'][i]['Avaliability'] == s_aval: 
                            print(data['Doctors'][i])
                            break
                        else:
                            print("No such Doctor in that Avaliability")
                elif option == 0:
                    break
    def validate_appointment(self):
         with open('/home/user/Desktop/Fellowship/Programming/oops/Json_files/clinique.json','r') as open_file:
            data = json.load(open_file)
            for i in range(0,len(data['Doctors'])):
                Doc_Name = data['Doctors'][i]['Doc_Name']
                Doc_ID = data['Doctors'][i]['Doc_ID']
                Spec = data['Doctors'][i]['Spec']
                Avaliability = data['Doctors'][i]['Avaliability']
                Appointment_avaliable = data['Doctors'][i]['Appointment_avaliable']
                
                dict1 = {"Doc_Name":Doc_Name, "Doc_ID":Doc_ID, "Spec":Spec, "Avaliability":Avaliability,"Appointment_avaliable":Appointment_avaliable}
     
        
            choose_doc_name = input("Enter the Doctor name = ")
            for i in range(0,len(data['Doctors'])):
                current_doc = data['Doctors'][i]['Doc_Name']
                if current_doc == choose_doc_name:
                    Avaliability1 = data['Doctors'][i]['Avaliability']
                    Appointment_avaliable1 = data['Doctors'][i]['Appointment_avaliable']
                    #print(Avaliability1,Appointment_avaliable1)
                    if Avaliability1== "yes" and Appointment_avaliable1 < 5:
                        print("Appointment  is Avaliable.. would you like to take it !!")
                        response = int(input("1.yes or 0.no.....="))
                        if response == 1:
                            print("Your appointment has been fixed with Mr.{}".format(choose_doc_name))
                            Appointment_avaliable1 += 1
                            data['Doctors'][i]['Appointment_avaliable'] = Appointment_avaliable1
                            with open('/home/user/Desktop/Fellowship/Programming/oops/Json_files/clinique.json','w') as out_file:
                                json.dump(data,out_file,indent=4,separators=(", ", " : "))
                                print("Appointment_avaliable Updated Successfully in Register")
                    

                
                       
                        
                            
                        elif response == 0:
                            break

                   
                   
                    else:
                        print("Kindly enter the correct doctor name...")
                        Doctor.validate_appointment(self)

            