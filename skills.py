"""Skills Assessment - Object Orientation"""


"""Part 1: Discussion
1. The three main design advantages that object orientation can provide are:
    Abstraction - Hides details that we do not need to know regarding methods
    Encapsulation - Keeps data and methods close together
    Polymorphism - Interchangeability of components

    *** NEED MORE CLARIFICATION ON THESE CONCEPTS ***

2. A class is a type of thing, either defined by Python (i.e. String, File) or by the user (i.e. Pet).

3. An instance attribute is an attribute specific to the instance/object.

4. A method is a function defined on a class that takes the instance itself, 'self' as its first parameter.

5. An instance in object orientation, is an individual instance/object of a class. For examples, there may be many instances of Dog, such as fido, arfy, barky, sparky, etc. which are different from each other but are generalized as being a Dog.

6. A class attribute is applicable to all instances, but an instance attribute is specific to that instance. For example, a class attribute for the class Dog could be number of legs. Dogs generally have 4 legs. However, an instance of Dog, such as fido, may have been born with 3 legs, so it would have an instance attribute of 3 legs. This way, when we look up number of legs for fido, we look to its instance attribute first and if a value is found, we would not look for the class attribute.

"""


"""Part 2: Classes and Init Methods + Part 3: Methods"""


class Student(object):
    """Student"""

    def __init__(self, first_name, last_name, address):
        """Initialize student"""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Question"""

    def __init__(self, question, correct_answer):
        """Initialize question"""

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Prompt user for an answer to the question and return True/False"""

        user_answer = raw_input(self.question + " > ")
        # print user_answer == self.correct_answer
        return user_answer == self.correct_answer


class Exam(object):
    """Exam"""

    def __init__(self, name):
        """Initialize exam"""

        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Make a question for the exam and add to list of questions"""

        # Instantiate a Question and append to list of Question objects
        self.questions.append(Question(question, correct_answer))

    def administer(self):
        """Administer all of the exam's questions and return score"""

        score = 0

        # Loop through each object in the instance's list of Question objects and call ask_and_evaluate() method on the object
        for question in self.questions:
            if question.ask_and_evaluate() is True:
                score += 1
            # print score

        return score

# # Below lines of code are for testing
# exam = Exam("midterm")
# exam.add_question("Who is Ubermelon's competition?", "Sqysh")
# exam.add_question("What is the method for adding an element to a set?", ".add()")
# exam.administer()


"""Part 4: Create an actual exam!"""


def take_test(exam, student):
    """Administer the exam for a student and assign score to student"""

    student.score = exam.administer()
    return student.score


# # Below lines of code are for testing
# jasmine = Student("Jasmine", "Debugger", "0101 Computer Street")
# take_test(exam, jasmine)


# Not sure if did this function correctly based on instructions provided
def example(exam_name, student_first_name, student_last_name, student_address):
    example_exam = Exam(exam_name)
    example_exam.add_question("What is the capital of Alberta?", "Edmonton")
    example_exam.add_question("Who is the author of Python?", "Guido Van Rossum")
    example_exam.add_question("What is Balloonicorn's favorite color?", "Sparkles")
    example_student = Student(student_first_name, student_last_name, student_address)
    print take_test(example_exam, example_student)


"""Part 5: Inheritance"""


class Quiz(Exam):
    """Quiz

    Quiz is pass/fail
    Pass if at least half of the questions are answered correctly
    """

    def administer(self):
        """Administer all of the quiz's questions and returns True/False for Pass/Fail"""

        if super(Quiz, self).administer() < (len(self.questions)/2):
            return False
        else:
            return True

# # Below lines of code are for testing
# quiz = Quiz("first quiz")
# quiz.add_question("Who is Ubermelon's competition?", "Sqysh")
# quiz.add_question("What is the method for adding an element to a set?", ".add()")
