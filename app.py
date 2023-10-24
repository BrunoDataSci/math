import streamlit as st
import random


st.title("Math Quiz App")
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
operator = random.choice(['+', '-', '*', '/'])

if operator == '+':
    answer = num1 + num2
    answer=round(answer)
elif operator == '-':
    answer = num1 - num2
    answer=round(answer)
elif operator == '*':
    answer = num1 * num2
    answer=round(answer)
else:
    num2 = random.randint(1, 100)
    answer = round(num1 / num2)

st.write(f"What is {num1} {operator} {num2}?")

user_answer = st.number_input("Enter your answer:")
if st.button("Check"):
    if user_answer != None:
        if user_answer == answer:
            st.success("Correct!")
        else:
            st.error("Wrong")
    st.write(f'The correct answer is {answer}')
st.empty()
