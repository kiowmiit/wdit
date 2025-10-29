import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {
                '__type__': 'Person',
                'name': obj.name,
                'age': obj.age
            }
        return json.JSONEncoder.default(self, obj)

person = Person("Alice", 30)
json_string = json.dumps(person, cls=PersonEncoder, indent=4)


def decode_person(dct):
    """Custom decoder hook to deserialize objects."""
    # Check if the dictionary has the custom type hint
    if '__type__' in dct and dct['__type__'] == 'Person':
        # Recreate the Person object from the dictionary data
        return Person(dct['name'], dct['age'])

    # Return the dictionary if it's not a Person object
    return dct


# Use the custom hook with json.loads()
person_restored = json.loads(json_string, object_hook=decode_person)

print("-" * 20)
print(f"Restored Object Type: {type(person_restored)}")
print(f"Restored Person Name: {person_restored.name}")
print(f"Restored Person Age: {person_restored.age}")


class CreditCard:
    name = None
    number = None
    expiration = None

