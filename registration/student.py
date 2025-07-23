class Student:
    valid_gender = ["male", "female"]
    valid_course = ["bsit", "bscs", "bscis", "bsba", "bsa", "bsais", "bsma", "bsrtcs", "art"]
    valid_year = ["1st year", "first year", "2nd year", "second year",
                  "3rd year", "third year", "4th year", "fourth year"]

    def __init__(self, name, gender, course, year):
        self.name = name
        self.gender = Student.standardize_gender(gender)
        self.course =Student.standardize_course(course)
        self.year = Student.standardize_year(year)

    def display(self):
        return (f"    Name   : {self.name.title()}\n"
                f"    Gender : {self.gender}\n"
                f"    Course : {self.course}\n"
                f"    Year   : {self.year}")

    @staticmethod
    def standardize_year(year_input):
        mapping = {
            "first year": "1st Year",
            "1st year": "1st Year",
            "second year": "2nd Year",
            "2nd year": "2nd Year",
            "third year": "3rd Year",
            "3rd year": "3rd Year",
            "fourth year": "4th Year",
            "4th year": "4th Year"
        }
        return mapping.get(year_input.lower(), year_input.title())

    @staticmethod
    def standardize_gender(gender_input):
        mapping = {
            "male": "Male",
            "female": "Female",
        }
        return mapping.get(gender_input.lower(), gender_input.title())

    @staticmethod
    def standardize_course(course_input):
        mapping = {
            "bsit": "BSIT",
            "bscs": "BSCS",
            "bsba": "BSBA",
            "bsa": "BSA",
            "bsais": "BSAIS",
            "bsma": "BSMA",
            "bsrtcs": "BSRTCS",
            "art": "ART",
        }
        return mapping.get(course_input.lower(), course_input.upper())
