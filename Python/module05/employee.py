class Employee:
    """ Employee parent class """

    def __init__(self, prm_first_name, prm_last_name, prm_salary):
        # Parse parameters of class creation call
        self.first_name = str(prm_first_name).capitalize()
        self.last_name = str(prm_last_name).capitalize()
        self.salary = int(prm_salary)

        # Create class Instance properties
        # self.full_name = self.first_name + ', ' + self.last_name
        self.email = self.first_name.lower() + '_' + self.last_name.lower() + '@example.com'

    # There are some different types of Class Functions (Class methods):
    #   @classmethod Decorated Functions should be used for working with the whole Class, not Instance of class.
    #   @staticmethod Decorated Functions should be used for creating some logic connected to Class,
    #     but it doesn't work with Class object or Instance of class.It simply provide some additional functional logic.
    #   Class Instance methods it's not decorated and simple methods of class which works with Instance of class

    # Alternative Class constructor method. It creates and return class Instance from string.
    @classmethod
    def from_str(cls, prm_empl_info_string):
        return Employee(*prm_empl_info_string.split(','))

    # Class property keeping Full Name of employee
    @property
    def full_name(self):
        return self.first_name + ', ' + self.last_name

    # === Should be refactored!!
    @full_name.setter
    def full_name(self, prm_empl_full_name_string):
        self.first_name, self.last_name = prm_empl_full_name_string.split(', ')
        self.first_name = str(self.first_name).capitalize()
        self.last_name = str(self.last_name).capitalize()


class DevOps(Employee):
    """ DevOps class. Child of Employee parent class. It has an additional property which keeps skills of employee """

    def __init__(self, prm_first_name, prm_last_name, prm_salary, prm_skills=[]):
        super().__init__(prm_first_name, prm_last_name, prm_salary)

        # It keeps skills list of DevOps class Instance
        self.skills = prm_skills

    def add_skill(self, prm_skill):
        self.skills.append(prm_skill.lower().capitalize())
        # self.skills = list(set(self.skills))

    def remove_skill(self, prm_skill):
        try:
            self.skills.remove(prm_skill.lower().capitalize())
        except ValueError:
            # print('ValueError exception!, Skill is not detected')
            pass


class Manager(Employee):
    def __init__(self, prm_first_name, prm_last_name, prm_salary, prm_slaves=[]):
        super().__init__(prm_first_name, prm_last_name, prm_salary)

        self.subordinates = prm_slaves

    def add_subordinate(self, prm_slave):
        self.subordinates.append(prm_slave)
        # self.subordinates = list(set(self.subordinates))

    def remove_subordinate(self, prm_slave):
        try:
            self.subordinates.remove(prm_slave)
        except ValueError as Err:
            # print('ValueError exception!, Employee is not detected')
            # print(Err)
            pass



if __name__ == "__main__":
    employ1 = Employee("John", "Doe", 500)
    employ2 = Employee.from_str("Kate,Petrova,300")
    employ1.full_name = "bart, simpson"

    employ_devops1 = DevOps("John", "Doe", 500,
                           ["Python", "Aws", "Bash", "Linux", "Laservision", "Bulletproof", "Superspeed"])

    employ_devops1.add_skill("virTualization")
    employ_devops1.add_skill("VIrTualization")
    employ_devops1.remove_skill("Laservision")
    employ_devops1.remove_skill("NonExistSkill")


    employ_manager1 = Manager("jane", "doe", 600)
    employ_manager2 = Manager("jane", "doe", 600, [employ_devops1, employ2])

    employ_manager1.add_subordinate(employ1)
    employ_manager1.add_subordinate(employ2)
    employ_manager1.remove_subordinate(employ1)
    print(employ_manager1.subordinates)







