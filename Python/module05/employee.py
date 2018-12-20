class Employee:
    def __init__(self, first_name, last_name, salary):

        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.full_name = first_name + ', ' + last_name

        # Написать методы добавления и удаления скилов в список
        self.skills = []


class Manager:
    pass


class DevOps:
    pass


if __name__ == "__main__":

    empl1 = Employee("John", "Doe", 500)
    print(empl1.first_name, empl1.last_name, empl1.full_name)
