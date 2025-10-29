import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PersonEncoder(json.JSONEncoder):
    """Custom encoder to serialize Person objects."""
    def default(self, obj):
        # Check if the object is an instance of the Person class
        if isinstance(obj, Person):
            # Convert the object into a dictionary with a type hint
            return {
                '__type__': 'Person',
                'name': obj.name,
                'age': obj.age
            }
        # Let the base class handle other types
        return json.JSONEncoder.default(self, obj)

# --- Example of Serialization ---
person = Person("Alice", 30)

# Use the custom encoder with json.dumps()
json_string = json.dumps(person, cls=PersonEncoder, indent=4)

print(f"Serialized JSON:\n{json_string}")
# Expected output (or similar):
# {
#     "__type__": "Person",
#     "name": "Alice",
#     "age": 30
# })