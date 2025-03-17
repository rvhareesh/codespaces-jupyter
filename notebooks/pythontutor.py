import streamlit as st
from gtts import gTTS
import os
import tempfile
import sys
from io import StringIO
import contextlib
import random

class ProgramGenerator:
    def __init__(self):
        self.templates = {
            'basic_math': [
                "def {func_name}(a, b):\n    return a {operator} b",
                "result = {num1} {operator} {num2}",
                "{var1} = float(input('Enter {prompt}: '))\n{var2} = float(input('Enter {prompt}: '))\nresult = {var1} {operator} {var2}"
            ],
            'loops': [
                "for i in range({range}):\n    print(i)",
                "while {condition}:\n    {action}\n    {update}",
                "[x {operation} for x in range({range}) if {condition}]"
            ],
            'strings': [
                "text = '{sample_text}'\nprint(text.{string_method}())",
                "name = input('Enter name: ')\nprint(f'Hello, {name}!')",
                "''.join([char.{string_method}() for char in '{sample_text}'])"
            ],
            'functions': [
                "def {func_name}({params}):\n    {body}\n    return {return_value}",
                "lambda {params}: {expression}",
                "@{decorator}\ndef {func_name}({params}):\n    {body}"
            ]
        }
        
        self.sample_data = {
            'operators': ['+', '-', '*', '/', '//', '%', '**'],
            'names': ['calculate', 'process', 'compute', 'analyze', 'transform'],
            'string_methods': ['upper', 'lower', 'title', 'strip', 'replace'],
            'sample_texts': ['Hello World', 'Python Programming', 'Learn to Code']
        }

    def generate_example(self, concept, complexity=1):
        """Generate a programming example based on concept and complexity level"""
        if concept == 'basic_math':
            return self._generate_math_example(complexity)
        elif concept == 'loops':
            return self._generate_loop_example(complexity)
        elif concept == 'strings':
            return self._generate_string_example(complexity)
        elif concept == 'functions':
            return self._generate_function_example(complexity)
        return "# Example not available for this concept"

    def _generate_math_example(self, complexity):
        if complexity == 1:
            nums = [random.randint(1, 10) for _ in range(2)]
            op = random.choice(self.sample_data['operators'])
            return f"# Simple math operation\nresult = {nums[0]} {op} {nums[1]}\nprint(result)"
        else:
            func_name = random.choice(self.sample_data['names'])
            ops = random.sample(self.sample_data['operators'], 2)
            return f"""# Complex math operation
def {func_name}(x, y, z):
    result = (x {ops[0]} y) {ops[1]} z
    return result

# Test the function
print({func_name}({random.randint(1,10)}, {random.randint(1,10)}, {random.randint(1,10)}))"""

    def _generate_loop_example(self, complexity):
        if complexity == 1:
            return f"""# Simple loop
for i in range({random.randint(5,10)}):
    print(f"Iteration {{i}}")"""
        else:
            return f"""# Nested loop with condition
for i in range({random.randint(3,6)}):
    for j in range({random.randint(2,4)}):
        if (i + j) % 2 == 0:
            print(f"i: {{i}}, j: {{j}}")"""

class PythonTutor:
    def __init__(self):
        self.topics = {
            # Basic Topics
            'introduction': 'Introduction to Python',
            'variables': 'Variables & Data Types',
            'operators': 'Basic Operators',
            'strings': 'String Operations',
            'control_flow': 'Control Flow (if/else)',
            'loops': 'Loops (for/while)',
            'lists': 'Lists and Arrays',
            'tuples': 'Tuples',
            'sets': 'Sets',
            'dictionaries': 'Dictionaries',
            'functions': 'Functions',
            
            # Intermediate Topics
            'modules': 'Modules and Packages',
            'file_handling': 'File Handling',
            'exceptions': 'Exception Handling',
            'oop_basics': 'OOP Basics',
            'classes': 'Classes and Objects',
            
            # Advanced Topics
            'inheritance': 'Inheritance and Polymorphism',
            'decorators': 'Decorators',
            'generators': 'Generators and Iterators',
            'context_managers': 'Context Managers',
            'lambda': 'Lambda Functions',
            'comprehensions': 'List/Dict Comprehensions',
            'threading': 'Threading and Multiprocessing',
            'regex': 'Regular Expressions',
            'testing': 'Unit Testing',
            'debugging': 'Debugging Techniques'
        }
        
        # Expanded quiz questions
        self.quizzes = {
            'introduction': [
                {
                    'question': 'What function is used to display output in Python?',
                    'options': ['print()', 'display()', 'show()', 'output()'],
                    'correct': 'print()'
                },
                {
                    'question': 'Which symbol is used for single-line comments in Python?',
                    'options': ['//', '#', '--', '/*'],
                    'correct': '#'
                },
                {
                    'question': 'What function is used to get input from the user?',
                    'options': ['input()', 'get()', 'read()', 'scanf()'],
                    'correct': 'input()'
                }
            ],
            'variables': [
                {
                    'question': 'Which of these is a valid variable name?',
                    'options': ['1st_name', '_name', 'my-name', 'class'],
                    'correct': '_name'
                },
                {
                    'question': 'What is the data type of x in x = 5.0?',
                    'options': ['int', 'float', 'string', 'boolean'],
                    'correct': 'float'
                },
                {
                    'question': 'What will be the value of x after: x = 5; x += 3?',
                    'options': ['5', '3', '8', '53'],
                    'correct': '8'
                },
                {
                    'question': 'What is the type of None in Python?',
                    'options': ['NoneType', 'null', 'void', 'undefined'],
                    'correct': 'NoneType'
                }
            ],
            'operators': [
                {
                    'question': 'What is the result of 7 // 2?',
                    'options': ['3.5', '3', '4', '2'],
                    'correct': '3'
                },
                {
                    'question': 'What is the result of 5 ** 2?',
                    'options': ['7', '10', '25', '52'],
                    'correct': '25'
                },
                {
                    'question': 'What is the result of True and False?',
                    'options': ['True', 'False', '1', '0'],
                    'correct': 'False'
                },
                {
                    'question': 'What does the "in" operator do?',
                    'options': [
                        'Checks membership in a sequence',
                        'Performs multiplication',
                        'Checks equality',
                        'Assigns values'
                    ],
                    'correct': 'Checks membership in a sequence'
                }
            ]
        }

        # Add new lessons for advanced topics
        self.lessons = {
            'basic_programs': {
                'content': """Basic Python Programming Examples (1-25)""",
                'examples': [
                    ('1. Number Operations', '''
# Basic calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Floor Division: {num1 // num2}")
print(f"Power: {num1 ** num2}")'''),

                    ('2. Temperature Converter', '''
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"{celsius}°C = {fahrenheit}°F")
print(f"{celsius}°C = {kelvin}K")'''),

                    ('3. Area Calculator', '''
import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

# Test the functions
print(f"Circle area (r=5): {calculate_circle_area(5):.2f}")
print(f"Rectangle area (l=4, w=6): {calculate_rectangle_area(4, 6)}")
print(f"Triangle area (b=3, h=8): {calculate_triangle_area(3, 8)}")'''),

                    ('4. Grade Calculator', '''
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Test with different scores
scores = [95, 88, 72, 65, 45]
for score in scores:
    print(f"Score {score}: Grade {calculate_grade(score)}")'''),

                    ('5. Prime Number Checker', '''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test numbers from 1 to 20
for num in range(1, 21):
    print(f"{num} is {'prime' if is_prime(num) else 'not prime'}")'''),

                    ('6. Fibonacci Sequence', '''
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Generate first 10 Fibonacci numbers
print("First 10 Fibonacci numbers:")
print(fibonacci(10))'''),

                    ('7. Password Generator', '''
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate 5 different passwords
for i in range(5):
    print(f"Password {i+1}: {generate_password()}")'''),

                    ('8. Word Counter', '''
def count_words(text):
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower().strip('.,!?')
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Test the function
sample_text = "The quick brown fox jumps over the lazy dog. The dog sleeps."
result = count_words(sample_text)
for word, count in result.items():
    print(f"'{word}': {count} times")'''),

                    ('9. BMI Calculator', '''
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

# Test with sample data
weight = 70  # kg
height = 1.75  # meters
bmi, category = calculate_bmi(weight, height)
print(f"BMI: {bmi:.1f}")
print(f"Category: {category}")'''),

                    ('10. Simple Banking System', '''
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount"

# Test the banking system
account = BankAccount(1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(2000))  # Should fail
print(f"Final balance: ${account.balance}")''')
                ]
            },
            
            'intermediate_programs': {
                'content': """Intermediate Python Programming Examples (26-50)""",
                'examples': [
                    ('26. File Handler', '''
# Writing and reading files
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test file operations
filename = "test.txt"
content = "Hello, this is a test file.\nPython is awesome!"

write_to_file(filename, content)
print("File contents:")
print(read_from_file(filename))

# Clean up
import os
os.remove(filename)'''),

                    # ... (continue with more examples)
                ]
            }
        }

        # Add new quizzes for advanced topics
        self.quizzes.update({
            'inheritance': [
                {
                    'question': 'What is the purpose of the super() function?',
                    'options': [
                        'To call methods from the parent class',
                        'To create a new instance',
                        'To delete an object',
                        'To override a method'
                    ],
                    'correct': 'To call methods from the parent class'
                }
            ],
            'decorators': [
                {
                    'question': 'What is a decorator in Python?',
                    'options': [
                        'A function that takes another function as argument',
                        'A class method',
                        'A type of loop',
                        'A built-in function'
                    ],
                    'correct': 'A function that takes another function as argument'
                }
            ]
        })

        self.program_generator = ProgramGenerator()

    def text_to_speech(self, text):
        try:
            # Create a temporary file for the audio
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(temp_file.name)
            
            # Play the audio using streamlit
            st.audio(temp_file.name)
            
            # Clean up
            temp_file.close()
            os.unlink(temp_file.name)
        except Exception as e:
            st.error(f"Error in text-to-speech: {str(e)}")

    def run_code(self, code):
        output = StringIO()
        with contextlib.redirect_stdout(output):
            try:
                exec(code)
                return output.getvalue()
            except Exception as e:
                return f"Error: {str(e)}"

    def generate_examples(self, topic, num_examples=5):
        """Generate multiple examples for a given topic"""
        examples = []
        for i in range(num_examples):
            complexity = (i // 2) + 1  # Increase complexity gradually
            example = self.program_generator.generate_example(topic, complexity)
            examples.append((f"Example {i+1}", example))
        return examples

    def show_lesson(self, topic):
        st.write("### " + self.topics[topic])
        
        # Generate dynamic examples
        if topic in ['basic_math', 'loops', 'strings', 'functions']:
            st.write("### Generated Examples:")
            examples = self.generate_examples(topic)
            for title, code in examples:
                with st.expander(title):
                    st.code(code, language='python')
                    if st.button(f"Run {title}"):
                        st.write("Output:")
                        output = self.run_code(code)
                        st.code(output)

        # Show static examples if available
        if topic in self.lessons:
            lesson = self.lessons[topic]
            st.write(lesson['content'])
            
            if st.button(f"Listen to {self.topics[topic]}"):
                self.text_to_speech(lesson['content'])
            
            st.write("### Pre-defined Examples:")
            for title, code in lesson['examples']:
                with st.expander(title):
                    st.code(code, language='python')
                    if st.button(f"Run {title}"):
                        st.write("Output:")
                        output = self.run_code(code)
                        st.code(output)

        # Show quiz if available
        if topic in self.quizzes:
            self.show_quiz(topic)

    def show_quiz(self, topic):
        st.write("### Quiz")
        for i, quiz in enumerate(self.quizzes[topic]):
            st.write(f"**Q{i+1}: {quiz['question']}**")
            answer = st.radio(f"Select your answer for Q{i+1}:", 
                            quiz['options'],
                            key=f"quiz_{topic}_{i}")
            if st.button(f"Check Answer {i+1}"):
                if answer == quiz['correct']:
                    st.success("Correct! 🎉")
                else:
                    st.error(f"Wrong! The correct answer is: {quiz['correct']}")

def main():
    st.set_page_config(page_title="Python Tutor", layout="wide")
    st.title("Interactive Python Tutor")
    
    # Initialize tutor
    tutor = PythonTutor()
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    selected_topic = st.sidebar.selectbox(
        "Choose a topic:",
        list(tutor.topics.keys()),
        format_func=lambda x: tutor.topics[x]
    )
    
    # Display selected lesson
    tutor.show_lesson(selected_topic)
    
    # Practice section
    st.markdown("---")
    st.header("Practice Section")
    user_code = st.text_area(
        "Write your Python code here:",
        height=150,
        help="Type your Python code and click 'Run Code' to see the output"
    )
    
    if st.button("Run Code"):
        if user_code.strip():
            st.write("Output:")
            output = tutor.run_code(user_code)
            st.code(output)
        else:
            st.warning("Please enter some code to run")
    
    # Help section in sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    ### How to use:
    1. Select a topic from the menu
    2. Read the lesson content
    3. Click 'Listen' to hear the explanation
    4. Try the example code
    5. Take the quiz to test your knowledge
    6. Practice in the code editor
    """)

if __name__ == "__main__":
    main() 