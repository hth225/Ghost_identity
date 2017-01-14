from faker import Factory
fake = Factory.create('en-us')

def Get_person_identity():
    print(fake.simple_profile())

def Various_identity():
    for _ in range(0, 10):
        print(fake.simple_profile())

def write_identities(cache):
    file = open("Got_Identities.txt", 'a')
    file.write(str(cache))
    file.close()


if __name__ == "__main__":
    while 1:
        print("1 : Single identity\n2 : Various identity\n3 : Exit\n")
        value = input(">")
        if (value == '1'):
            Get_person_identity()
            cache = Get_person_identity()
            q = input("Do you want to write this on text file? (y/n)\n")
            if(q == 'y'):
                write_identities(str(cache))
                print("Successfully done")
            else:
                break
        elif(value == '2'):
            print("Make 10person identity")
            Various_identity()
        else:
            print("exit")
            break


# person = {
#     "name": fake.namae(),
#     "age": fake.namae(),
# }
# person['name']