import streamlit as st
import string
import random

# Function to generate a random password
def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        st.error("Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit app
def main():
    st.title("Random Strong Password Generator")

    # Password length input
    password_length = st.slider("Password Length", min_value=6, max_value=30, value=12, step=1)

    # Character type selection
    include_uppercase = st.checkbox("Include Uppercase Letters")
    include_lowercase = st.checkbox("Include Lowercase Letters")
    include_numbers = st.checkbox("Include Numbers")
    include_symbols = st.checkbox("Include Special Symbols")

    # Generate password button
    if st.button("Generate Password"):
        password = generate_password(password_length, include_uppercase, include_lowercase, include_numbers, include_symbols)

        if password:
            st.success("Generated Password:")
            st.text(password)

if __name__ == '__main__':
    main()
