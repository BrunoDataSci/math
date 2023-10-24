import streamlit as st
import random


if st.button("Check Answer"):
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
        answer = num1 / num2

    st.title("Math Quiz App")
        
    st.write(f"What is {st.num1} {st.operator} {st.num2}?")
    
    user_answer = st.number_input("Enter your answer:", key="user_input")

    if user_answer == st.answer:
        st.success("Correct!")
    else:
        st.error(f"Wrong. The correct answer is {st.answer}")
    
    st.write(f"The answer was {st.num1} {st.operator} {st.num2} = {st.answer}")

else:
    None
