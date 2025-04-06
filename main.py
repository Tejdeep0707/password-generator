import streamlit as st
import random
import string

# Page setup
st.set_page_config(page_title="Password Generator", layout="centered")

# Custom CSS for black + coding background
st.markdown("""
    <style>
        .stApp {
            background-color: black;
            background-image: url("https://images.unsplash.com/photo-1590272456521-1bbe160a18ce?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white;
            font-family: 'Courier New', monospace;
        }

        .section {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
            border: 1px solid #444;
        }

        .footer {
            margin-top: 40px;
            text-align: center;
            font-size: 14px;
            color: #bbb;
        }

        h1, h2, h3, h4, label, p, div, span {
            color: #00ffcc !important;
        }

        .important-note {
            background-color: rgba(0, 255, 200, 0.2);
            padding: 10px;
            border-left: 6px solid #00ffaa;
            margin-bottom: 20px;
            border-radius: 8px;
            color: #ffffff;
        }

        .css-1cpxqw2 {  /* code box */
            color: #00ffaa !important;
        }

        a {
            color: #00ffee;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.title("💻 Password Generator")
st.markdown("Secure, customizable passwords — hacker-style.")
st.markdown("</div>", unsafe_allow_html=True)

# Password importance section
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.subheader("🔐 Why strong passwords?")
st.markdown("""
<div class="important-note">
Strong passwords protect your personal data, accounts, and identity. 
Avoid easy ones like `12345`, your name, or birthdays.
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# User options
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.subheader("🛠️ Customize Your Password")

length = st.slider("Password Length", 6, 32, 12)
uppercase = st.checkbox("Include Uppercase Letters (A-Z)", value=True)
lowercase = st.checkbox("Include Lowercase Letters (a-z)", value=True)
numbers = st.checkbox("Include Numbers (0-9)", value=True)
specials = st.checkbox("Include Special Characters (!@#...)", value=True)
st.markdown("</div>", unsafe_allow_html=True)


# Password generation
def generate_password(length, upper, lower, digits, special):
    char_set = ""
    if upper:
        char_set += string.ascii_uppercase
    if lower:
        char_set += string.ascii_lowercase
    if digits:
        char_set += string.digits
    if special:
        char_set += string.punctuation

    if not char_set:
        return "⚠️ Select at least one option."

    return ''.join(random.choice(char_set) for _ in range(length))


# Button & output
st.markdown("<div class='section'>", unsafe_allow_html=True)
if st.button("💥 Generate Password"):
    pwd = generate_password(length, uppercase, lowercase, numbers, specials)
    st.success("Here’s your password:")
    st.code(pwd, language="bash")
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='footer'>
📧 Contact: <a href="mailto:tejdeep0707@gmail.com">tejdeep0707@gmail.com</a><br>
Made with 🖤 by Tejdeep
</div>
""", unsafe_allow_html=True)
