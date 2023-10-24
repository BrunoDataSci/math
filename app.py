import streamlit as st
import random

# Function to generate random math questions
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        # Avoid division by zero
        num2 = random.randint(1, 10)
        answer = num1 / num2
    
    return num1, num2, operator, answer

# Main Streamlit app
def main():
    st.title("Math Quiz App")

    # Generate the first question
    num1, num2, operator, answer = generate_question()

    user_answer = st.number_input("Enter your answer:", key="user_input")
    
    if st.button("Check Answer"):
        if user_answer == answer:
            st.success("Correct!")
        else:
            st.error(f"Wrong. The correct answer is {answer}")
        
        st.write(f"The answer was {num1} {operator} {num2} = {answer}")
        
        st.write("Try the next question!")
        
        # Generate a new question
        num1, num2, operator, answer = generate_question()

if __name__ == "__main__":
    main()
