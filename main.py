class Course:  # First class including course attributes
    def __init__(self, course_id, course_name, course_fee):
        self.course_id = course_id
        self.course_name = course_name  # initializing attributes
        self.course_fee = course_fee

    course_dict = {"courses": []}  # Dictionary with a nested list to hold courses that users will add


class Student:  # Second class including student attributes
    def __init__(self, student_id, student_name, student_email, course, balance):  # parameters required by program
        self.student_id = student_id
        self.student_name = student_name
        self.student_email = student_email  # initializing attributes
        self.course = course
        self.balance = balance

    registry = {"student": []}  # Dictionary with a nested list to hold student attributes that users will add

    def enroll(self):  # enroll function that updates student list and balance
        db_alpha = self.registry["student"]
        prog = Course("id", 'name', 0)  # initialize class as an instance to use within scope of the function
        db_beta = prog.course_dict["courses"]  # initialize instance and rename to utilize within scope of the function
        student_id = input("what is the student's id? ")
        ind = 0  # counter used to access nested dict list for appending to correct location when found
        for item in db_alpha:  # loop to check through dict nested list for id and update course in that list index
            if item.get("student_id") == student_id:  # checking if id exists before adding course
                course_id = input("What course would you like to add? ")
                for key in db_beta:
                    if key.get("course_id") == course_id:  # ensure input matches key within dictionary

                        db_alpha[ind].update({"course": key.get("course_id"), "balance": key.get(
                            "course_fee")})  # use the update function instead of append so it adds to indexes entry as a key:value pair

                        print("Student ", item.get("student_name"), "is now enrolled in ",
                              key.get("course_name"))  # confirmation messages
                        print("Their new balance is ", item.get("balance"))

                    ind = ind + 1  # increase counter for the next loop.

    def get_total_fee(self):  # function to get total fee of all courses within course dictionary
        db_gamma = Course("", '', 0)  # initialize instance from course
        tot_fee = 0.00
        ind = 0
        for item in db_gamma.course_dict[ind]:
            if item.get(
                    "students_enrolled") > 0:  # this checks if the dictionary has a key with a value greater than zero and adds to it
                tot_fee = tot_fee + (item.get("course_fee") * item.get(
                    "students_enrolled"))  # taking values form the dictionary and totalling them
                ind = ind + 1
            else:
                ind = ind + 1
                continue

        if tot_fee > 0:  # this checks to ensure this variable is more than one and can print information or notify the user
            print("The total amount for enrolled courses are " + str(tot_fee))
        else:
            print("No amount to give as there are no courses with enrolled students")


class RegistrationSystem(Course, Student):  # third class that inherits attributes from classes course and student

    def add_courses(self):  # function to add courses to the course dictionary as a key value pair
        db_delta = self.course_dict["courses"]  # initializing instance of dictionary from the course class

        student_id = input("what is the ID for this course? ")
        course_name = input("what is the name of the course? ")  # seeking user inputs
        course_fee = input("How much is the cost to do this course? ")

        db_delta.append({"course_id": student_id, "course_name": course_name,
                         "course_fee": course_fee})  # adding to the list in course dictionary

        print("Course " + course_name + " added successfully!")  # prompting user of successful entry

    def register_student(self):  # function to add students to the student dictionary as a key value pair
        db_epsilon = self.registry["student"]  # initializing instance of dictionary from the student class

        student = input("what is the student's ID ")
        student_name = input("what is the student's full name ")  # seeking user inputs
        student_email = input("what is the student's Email ")

        db_epsilon.append({"student_id": student, "student_name": student_name,
                           "student_email": student_email})  # adding to the list in the student dictionary

        print("Student " + student_name + " added successfully!")  # prompting user of completed task

    def calculate_payment(self):  # function to calculate student payments based on balance created when enrolling

        student_id = input("what is the student's ID? ")
        payment = float(input("how much are you paying? "))  # variable to hold payment they wish to enter
        ind = 0  # counter

        db_eta = self.registry["student"]  # initialize dictionary instance from student class

        for item in db_eta:
            if item.get("student_id") == student_id:  # nested if to verify student id and calculate registration status
                eligible_amt = float(item.get(
                    "balance")) * .40  # calculate eligible amount for registration and can use this amount to compare later
                if payment >= eligible_amt:
                    db_eta[ind]["balance"] = float(
                        item.get("balance")) - payment  # used index to find the correct item in list and balance
                    print("Student is now registered!")
                    main()
                else:
                    print("payment made however amount was insufficient to meet requirements for registration")
                    db_eta[ind]["balance"] = float(
                        item.get("balance")) - payment  # even if eligible amount is not met balance will be changed
                    print("Your new balance is " + str(item.get("balance")))
                    main()
            else:
                ind = ind + 1
                continue

    def check_student_balance(
            self):  # function to check student balance in student dictionary once a balance is present
        db_theta = self.registry["student"]  # initialize dictionary instance from student class

        student_id = input("what is the student's ID? ")

        for item in db_theta:  # looping through dictionary checking for matching ids
            if item.get("student_id") == student_id:
                print("Student balance is " + str(item.get("balance")))  # display balance if it is available

            else:
                print("no student with that student Id found")

    def show_courses(self):  # function to show courses

        db_iota = self.course_dict["courses"]  # initialize dictionary from course class

        if len(db_iota) != 0:  # check to ensure the dictionary has data to loop through else prompt user of such
            for item in db_iota:  # loop through dictionary to present key values
                print("Course ID: " + str(item.get("course_id")))
                print("Course Name: " + str(item.get("course_name")))
                print("The amount is: " + str(item.get("course_fee")))
        else:
            print("Database is empty!")

    def show_registered_students(self):  # function to show students that are registered

        db_kappa = self.registry["student"]

        if len(db_kappa) != 0:  # check to ensure the dictionary has data to loop through else prompt user of such

            for item in db_kappa:  # loop through dictionary to present key values
                print("Student ID: " + str(item.get("student_id")))
                print("Student Name: " + str(item.get("student_name")))
                print("Student email: " + str(item.get("student_email")))
                print("___*___")  # used to have separation amongst multiple entries
        else:
            print("No Students registered as yet!")

    def show_students_in_courses(self):  # function to show students enrolled in courses
        db_lambda = self.registry["student"]
        ind = 0
        course_id = input("what Course would you like to see the data for, please enter course ID? ")

        try:  # try except used here to ensure that if students aren't present user will be notified
            for item in db_lambda:

                if item.get("course") == course_id:  # loop through dictionary to present key values
                    print("Student ", item.get("student_name"), "is apart of the course ", item.get("course"))
                    ind = ind + 1
                else:
                    print("No student currently enrolled in this course")
        finally:  # notifying user of no data to process
            print("No students registered as yet!")


def by_by_chk():  # function used to check if user wishes to continue
    print("If you wish to continue")
    by_by_chk_1 = input("Press y to continue or anything else to QUIT! ")
    if by_by_chk_1 == "y" or by_by_chk_1 == "Y":
        main()
    else:
        print("Thank you for using the student registration system")


def main():
    archi = RegistrationSystem("", "", "")  # initializing registration class
    socket = True
    print("1.Register Student")
    print("2.Add Course")
    print("3.Show Courses")
    print("4.Enroll in Course")  # menu for user to access program functions
    print("5.Show registered Students")
    print("6.Show Students in a course")
    print("7.Calculate Payment")
    print("8.Check Student Balance")
    print("9.EXIT")

    selection = input("Choose a number to continue: ")  # variable used to decide what case to use in match case method

    while socket:
        match selection:
            case "1":
                archi.register_student()
                break
            case "2":
                archi.add_courses()
                break

            case "3":
                archi.show_courses()
                break
            case "4":
                archi.enroll()  # match case using functions and breaks to allow smoother flow of program
                break
            case "5":
                archi.show_registered_students()
                break
            case "6":
                archi.show_students_in_courses()
                break
            case "7":
                archi.calculate_payment()
                break
            case "8":
                archi.check_student_balance()
                break

            case "9":
                socket = False

            case _:  # default case for match case
                print("incorrect entry please try again!")
                main()  # calls main function after default message is displayed

    by_by_chk()


main()
