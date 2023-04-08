import streamlit as st

def find_largest(a, b, c):
    return max(a, b, c)

st.title("Find the Largest Number")
st.write("Enter three numbers below to find the largest among them.")

a = st.number_input("Enter the first number:")
b = st.number_input("Enter the second number:")
c = st.number_input("Enter the third number:")

if st.button("Find Largest"):
    result = find_largest(a, b, c)
    st.write(f"The largest number is: {result}")
