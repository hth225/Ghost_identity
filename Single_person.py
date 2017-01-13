from faker import Factory
fake = Factory.create('en-us')

def file_write(sorted_iden):
    file = open("identities.txt", 'a')
    file.write(sorted_iden)
    file.close()

def sort(iden):
    file = open("identities.txt", 'r')
    unsorted = file.read()
    file.close()
    unsorted.replace(', ', '\n')
    sorted_iden = unsorted
    file_write(sorted_iden)

if __name__ == "__main__":
    iden = fake.simple_profile()
    sort(iden)