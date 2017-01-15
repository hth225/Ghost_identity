from faker import Factory
fake = Factory.create('en-us')

def write_Various_identities(): #writing various identities on various.txt
    file_record = open("various.txt", 'a')
    for _ in range(0, 10):
        file_record.write(str(fake.simple_profile()))
        file_record.write("\n")
    file_record.close()

def Get_person_identity(): #get single person identity
    print(fake.simple_profile())

def Various_identities(): #get various identities
    for _ in range(0, 10):
        print(fake.simple_profile())

def write_identities(): #writing single identities on Got_Identities.txt
    file = open("Got_Identities.txt", 'a')
    file.write(str(fake.simple_profile()))
    file.write("\n")
    file.close()

def file_flush(): #clear all information that wrote
    file = open("various.txt", "w")
    file_2nd = open("Got_Identities.txt", "w")
    file.write("")
    file.close()
    file_2nd.write("")
    file_2nd.close()

if __name__ == "__main__":
    while 1:
        print("1 : Single identity\n2 : Various identity\n3 : File flush\n4 : Exit")
        value = input(">")
        if (value == '1'): #get one identity
            Get_person_identity()
            q = input("Do you want to write additional identities on text file? (y/n)\n")
            if(q == 'y'): #writing on text file
                write_identities()
                print("Successfully done\n")
            else: #if user typed n or another charachter, escape loop
                break
        elif(value == '2'): #get various identities for 10 person
            print("Make 10person identity\n")
            Various_identities()
            value = Various_identities()
            qe = input("Do you want to write additional identities on text file? (y/n)\n")
            if(qe == 'y'): #writing on text file
                write_Various_identities()
                print("Successfully done\n")
            else: #if user typed n or another charachter, escape loop
                break
        elif(value == '3'):
            print("file flush process successfully done")
            file_flush()
        else: #exit
            print("exit")
            break