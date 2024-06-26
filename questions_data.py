api_response = [
    {
        "question": "Explain the concept of polymorphism in object-oriented programming.",
        "choices": [
            "It allows a class to have multiple methods with the same name but different parameters.",
            "It allows a class to inherit from multiple parent classes.",
            "It allows a class to have only one method with a unique name.",
            "It allows a class to hide its implementation details."
        ],
        "correct_answer": "It allows a class to have multiple methods with the same name but different parameters."
    },
    {
        "question": "Solve the integral: ∫(2x^2 + 3x + 1) dx.",
        "choices": [
            "(2/3)x^3 + (3/2)x^2 + x + C",
            "(1/2)x^3 + (3/2)x^2 + x + C",
            "(2/3)x^3 + (3/2)x^2 + C",
            "(1/2)x^3 + (3/2)x^2 + C"
        ],
        "correct_answer": "(2/3)x^3 + (3/2)x^2 + x + C"
    },
    {
        "question": "Identify the time complexity of the quicksort algorithm.",
        "choices": [
            "O(n)",
            "O(n log n)",
            "O(n^2)",
            "O(2^n)"
        ],
        "correct_answer": "O(n log n)"
    },
    {
        "question": "Solve the system of equations: 2x + y = 5, 3x - 2y = 8.",
        "choices": [
            "x = 2, y = 1",
            "x = 1, y = 2",
            "x = 3, y = -1",
            "x = -1, y = 3"
        ],
        "correct_answer": "x = 3, y = -1"
    },
    {
        "question": "What is the purpose of a pointer in programming?",
        "choices": [
            "To store the memory address of a variable.",
            "To perform arithmetic operations on variables.",
            "To access the value of a variable directly.",
            "To declare dynamic arrays."
        ],
        "correct_answer": "To store the memory address of a variable."
    },
    {
        "question": "Find the derivative of f(x) = 3x^4 - 2x^3 + 5x^2 - 7 with respect to x.",
        "choices": [
            "12x^3 - 6x^2 + 10x",
            "9x^3 - 6x^2 + 10x",
            "12x^3 - 6x^2 + 5x",
            "9x^3 - 6x^2 + 5x"
        ],
        "correct_answer": "12x^3 - 6x^2 + 10x"
    },
    {
        "question": "In C++, what is the difference between 'delete' and 'delete[]' when deallocating memory?",
        "choices": [
            "'delete' is used for single variables, and 'delete[]' is used for arrays.",
            "'delete[]' is used for single variables, and 'delete' is used for arrays.",
            "Both 'delete' and 'delete[]' can be used interchangeably.",
            "Neither 'delete' nor 'delete[]' is used for memory deallocation."
        ],
        "correct_answer": "'delete' is used for single variables, and 'delete[]' is used for arrays."
    },
    {
        "question": "Evaluate the limit lim(x -> 0) (sin(x)/x).",
        "choices": [
            "1",
            "0",
            "π",
            "Undefined"
        ],
        "correct_answer": "1"
    },
    {
        "question": "What is the primary purpose of the 'volatile' keyword in C programming?",
        "choices": [
            "To declare a variable that cannot be modified.",
            "To indicate that a variable may be changed at any time outside the program's control.",
            "To optimize the performance of a loop.",
            "To declare a constant variable."
        ],
        "correct_answer": "To indicate that a variable may be changed at any time outside the program's control."
    },
    {
        "question": "If a matrix has dimensions 3x4, what is the total number of elements in the matrix?",
        "choices": [
            "7",
            "12",
            "24",
            "36"
        ],
        "correct_answer": "12"
    },
    {
        "question": "Identify the correct way to declare a static method in Java.",
        "choices": [
            "static void method() {}",
            "void static method() {}",
            "void method() static {}",
            "method static void {}"
        ],
        "correct_answer": "static void method() {}"
    },
    {
        "question": "Simplify the expression: log₂(8) + log₂(2).",
        "choices": [
            "3",
            "2",
            "4",
            "1"
        ],
        "correct_answer": "3"
    },
    {
        "question": "What is the Big O notation for a binary search algorithm?",
        "choices": [
            "O(log n)",
            "O(n)",
            "O(n^2)",
            "O(2^n)"
        ],
        "correct_answer": "O(log n)"
    },
    {
        "question": "Which design pattern is used to ensure a class has only one instance and provides a global point of access to it?",
        "choices": [
            "Singleton Pattern",
            "Factory Pattern",
            "Observer Pattern",
            "Decorator Pattern"
        ],
        "correct_answer": "Singleton Pattern"
    },
    {
        "question": "Evaluate the definite integral: ∫(0 to π) sin(x) dx.",
        "choices": [
            "0",
            "1",
            "π",
            "2π"
        ],
        "correct_answer": "2"
    },
    {
        "question": "What is the purpose of the 'decltype' keyword in C++?",
        "choices": [
            "To declare a variable type.",
            "To determine the type of an expression at compile time.",
            "To define a constant variable.",
            "To create a pointer to a variable."
        ],
        "correct_answer": "To determine the type of an expression at compile time."
    },
    {
        "question": "If a and b are integers, what is the result of the expression (a++ * b--) + (--a * ++b)?",
        "choices": [
            "ab",
            "a + b",
            "a - b",
            "a * b"
        ],
        "correct_answer": "ab"
    },
    {
        "question": "Identify the correct usage of the word 'ubiquitous' in a sentence.",
        "choices": [
            "The problem was ubiquitous to solve.",
            "Her ubiquitous presence made everyone comfortable.",
            "He ubiquitously avoided the meeting.",
            "Ubiquitous, she walked into the room."
        ],
        "correct_answer": "Her ubiquitous presence made everyone comfortable."
    },
    {
        "question": "What is the purpose of the 'volatile' keyword in Java?",
        "choices": [
            "To indicate that a variable may be changed by multiple threads at the same time.",
            "To declare a variable that cannot be modified.",
            "To optimize the performance of a loop.",
            "To specify the scope of a variable."
        ],
        "correct_answer": "To indicate that a variable may be changed by multiple threads at the same time."
    },
    {
        "question": "In Python, what is the difference between 'append()' and 'extend()' methods in the list?",
        "choices": [
            "'append()' adds a single element to the end, while 'extend()' adds elements of an iterable to the end.",
            "'extend()' adds a single element to the end, while 'append()' adds elements of an iterable to the end.",
            "Both 'append()' and 'extend()' add a single element to the end.",
            "Neither 'append()' nor 'extend()' can be used to add elements to a list."
        ],
        "correct_answer": "'append()' adds a single element to the end, while 'extend()' adds elements of an iterable to the end."
    }
]


# import requests
#
# url = "https://opentdb.com/api.php?amount=20&category=18&difficulty=medium&type=multiple"
# data = requests.get(url)
# temp = data.json()
# original_data = temp["results"]
# formatted_questions = []
#
# for question_data in original_data:
#     formatted_question = {
#         "question": question_data['question'],
#         "choices": [
#             question_data['correct_answer'],
#             *question_data['incorrect_answers']
#         ],
#         "correct_answer": question_data['correct_answer']
#     }
#     formatted_questions.append(formatted_question)
