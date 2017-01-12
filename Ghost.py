from faker import Factory
fake = Factory.create('en-us')

def Get_person_identity():
    print(fake.simple_profile())

def Various_identity(num):
    for _ in range(0, num):
        print(fake.simple_profile())

if __name__ == "__main__":
    while 1:
        print("1 : Single identity\n2 : Various identity\n3 : Exit\n")
        value = input(">")
        if (value == '1'):
            Get_person_identity()
        elif(value == '2'):
            num = input("How many?")
            Various_identity(num)
        else:
            print("exit")
            break


# person = {
#     "name": fake.namae(),
#     "age": fake.namae(),
# }
# person['name']