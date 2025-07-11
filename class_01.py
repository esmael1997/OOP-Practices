class Person:
    count = 0

    def __init__(self, name, birth_year, age):
        self.name = name
        self.age = age
        self.birth_year = birth_year
        Person.count += 1

    def get_name(self):
        print(f'Name: {self.name}')

    def get_age(self):
        return self.age

    def calculate_age_from_year(self):
        # Let's assume the current year is 1410 (Hijri Shamsi)
        return 1410 - self.birth_year

    def get_info(self):
        print(f'Name: {self.name}, Age: {self.age}')

    def birthday(self):
        self.age += 1
        print(f'Happy birthday, {self.name}!')

    def return_count(self):
        return Person.count


# Create a Person instance
esmael = Person('Esmael', 1376, 74)

# Get name and info
esmael.get_name()
esmael.get_info()

# Compare age with calculated age from birth year
user_age = esmael.get_age()
calculated_age = esmael.calculate_age_from_year()

if user_age != calculated_age:
    print(f' Age mismatch detected! The correct age should be: {calculated_age}')
else:
    print(' Great! Your age is calculated correctly.')
