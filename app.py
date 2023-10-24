import streamlit as st
import random

# Function to generate a random math question
def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*', '/'])

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        # Avoid division by zero
        num2 = random.randint(1, 100)
        answer = round(num1 / num2, 2)

    return num1, num2, operator, answer

# Main Streamlit app
def main():
    st.title("Math Quiz App")
    num1, num2, operator, answer = generate_question()
    st.write(f"What is {num1} {operator} {num2}?")

    user_answer = st.number_input("Enter your answer:")

    if st.button("Check Answer"):
        if user_answer == answer:
            st.success("Correct!")
        else:
            st.error(f"Wrong. The correct answer is {answer}")
        st.write(f"The answer was {num1} {operator} {num2} = {answer}")

    if st.button("Restart"):
        # Restart by regenerating a new question
        main()

if __name__ == "__main__":
    main()
