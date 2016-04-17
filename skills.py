"""Skills Assessment - Object Orientation"""


"""Part 1: Discussion
1. The three main design advantages that object orientation can provide are:
    Abstraction - Hides details that we do not need to know regarding methods
    Encapsulation - Keeps data and methods close together
    Polymorphism - Interchangeability of components

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
        user_answer = raw_input(self.question + " > ")
        # print user_answer == self.correct_answer
        return user_answer == self.correct_answer


class Exam(Question):
    """Exam"""
    questions = []

    def __init__(self, name):
        """Initialize exam"""
        self.name = name

    def add_question(self, question, correct_answer):
        super(Exam, self).__init__(question, correct_answer)
        self.questions.append(question)

    def administer(self):
        score = 0

        for self.question in self.questions:
            if self.ask_and_evaluate() is True:
                score += 1

        return score


"""Part 4: Create an actual exam!"""
