AUTHOR: Terrence Dunn

DATE CREATED: December 14, 2024

COURSE: ITT103

GIT URL : https://github.com/tdunnfromUCC/MajorProject_ITT103

PURPOSE OF THE PROGRAM

This code was a final coding project for a course at UCC. The code is to test my ability to design and produce
a working code with the aim of developing a menu-driven Python application to:-
1. Register students and manage their details.
2. Add courses with unique identifiers and fees.
3. Allow students to enroll in courses while tracking their balance.
4. Accept partial payments (minimum 40% of the balance) and update the outstanding balance.
5. Provide administrators with tools to view enrolled students, course details, and individual student
balances.
6. Implement error handling to ensure the system is robust and user-friendly.

HOW TO RUN

This code has clear menu-driven instructions on how to use it, however measures were put in place to handle incorrect input and allow the user to recover
from any bad input.

ASSUMPTIONS

-This code was designed as a concept for a staged environment.

-Some functions required in the documentation were designed for concept.

-Inheritance of classes and attributes were recommended.

-functions and class names were provided and as such used to direct design and development on own understanding

-Must include aspects of course work learned : Loops, Lists,indentation and correct spacing, Dictionaries, Functions,documentation and classes.

LIMITATIONS

-This code was designed as a concept and for a staged environment, enterprise use is highly discouraged.

-One function 'get_total_fee()' designed was flawed and was not used in design of menu or for use instead concept was the intention of its development.

-Expected input is strings and casting of datatypes is done on necessary input, however input of incorrect datatypes for those variables will cause unintended results.

-Certain use of menu choices requires data to already be there to compared. if no data is present sufficient warning and error handling is done to appease that.

-Use of try except method or error handling used to show proof of concept and instead resorted to using if statements for most error handling.

-Use of dictionaries with nested lists was intended to prevent duplication of records however lack of scope of this datatype has resulted in mishandling or erroneous use of the data, however some success was achieved.

-Function 'enroll_in_course()' was recommended in the design however i found now use for it as another function 'enroll()' performs the same role albeit in a different class.

-Function 'show_students_in_course(course_id)' was designed and has some success however it is a weakpoint in the program on how to use nested dictionaries to accurately track data.
