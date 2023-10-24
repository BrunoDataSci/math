import streamlit as st
import random

y=0
while y==0:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*', '/'])
    
    st.title("Math Quiz App")
        
    st.write(f"What is {num1} {operator} {num2}?")
    
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
        answer=round(answer,2)
    
    user_answer = st.number_input("Enter your answer:", key="user_input")
    
    if st.button("Check Answer"):
      
        if user_answer == answer:
            st.success("Correct!")
            y=1
            if st.button("Restart"):
               y=0
        else:
            st.error(f"Wrong. The correct answer is {answer}")
            st.write(f"The answer was {num1} {operator} {num2} = {answer}")
            y=1
           if st.button("Restart"):
               y=0
    else:
        st.button("Restart"):
        y=0
