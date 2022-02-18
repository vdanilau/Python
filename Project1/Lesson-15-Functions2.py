def create_record(name, phone_number, address):
    """Create record"""
    record = {
        "name": name,
        "phone_number": phone_number,
        "address": address
    }
    return record


user1 = create_record("Vasyl", "+434534543", "Tunisia")
user2 = create_record("Petya", "+4455455666", "Poland")

print(user1)
print(user2)


def give_award(medal, *persons):
    for person in persons:
        print("Comrade " + person.title() + " is being awarded of " + medal)


give_award("For Honor", "vasyl", "petya")
give_award("For Berlin", "pEtya", "aLEX", "Luda")


