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
        answer = num1 / num2
        answer= round(answer)
    
    return num1, num2, operator, answer

# Main Streamlit app
def main():
    st.title("Math Quiz App")

    if "num1" not in st.session_state:
        st.session_state.num1, st.session_state.num2, st.session_state.operator, st.session_state.answer = generate_question()
    
    st.write(f"What is {st.session_state.num1} {st.session_state.operator} {st.session_state.num2}?")
    
    user_answer = st.number_input("Enter your answer:")

    return check()
    

def check():
    st.session_state.user_answer=main()
    if st.button("Check Answer"):
        if user_answer == st.session_state.answer:
            st.success("Correct!")
        else:
            st.error(f"Wrong. The correct answer is {st.session_state.answer}")
        
        st.write(f"The answer was {st.session_state.num1} {st.session_state.operator} {st.session_state.num2} = {st.session_state.answer}")
        st.write("Try the next question!")
        main()

if __name__ == "__main__":
    main()
