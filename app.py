import streamlit as st
import re
import secrets
import string

# Sets Page Configuration
st.set_page_config(page_title="Password Checker & Generator", page_icon="🗝")

# Page Title
st.title("🔐 Password Checker & Generator")
st.subheader("Check your password strength")

# User password input
password = st.text_input("Enter Password:", help="💝")

# Function to estimate time to crack password
def estimate_crack_time(password):
    chars = string.ascii_letters + string.digits + "@#$%&!?"
    total_combinations = len(chars) ** len(password)
    crack_time_seconds = total_combinations // 1e9  # 1 billion guesses/sec
    crack_time_minutes = crack_time_seconds // 60
    crack_time_hours = crack_time_minutes // 60
    crack_time_days = crack_time_hours // 24
    crack_time_years = crack_time_days // 365

    if crack_time_seconds < 1:
        return "⚠️ Instantly cracked 😟"
    elif crack_time_minutes < 1:
        return "⏳ Crack time: A few seconds."
    elif crack_time_hours < 1:
        return "⏳ Crack time: A few minutes."
    elif crack_time_days < 1:
        return "🕒 Crack time: A few hours."
    elif crack_time_years < 1:
        return f"🛡️ Crack time: {int(crack_time_days)} days."
    else:
        return f"🔒 Crack time: {int(crack_time_years)} years."

# Password Strength Check
if password:
    if len(password) < 8:
        message = "❌ Password must be at least **8 characters long**."
        strength = "Weak"
    elif not re.search(r"[A-Z]", password):
        message = "❌ Password must contain **at least one uppercase letter**."
        strength = "Weak"
    elif not re.search(r"[a-z]", password):
        message = "❌ Password must contain **at least one lowercase letter**."
        strength = "Weak"
    elif not re.search(r"\d", password):
        message = "❌ Password must contain **at least one digit**."
        strength = "Weak"
    elif not re.search(r"[@#$%&!?]", password):
        message = "❌ Password must contain **at least one special character (@#$%&!?)**."
        strength = "Weak"
    else:
        message = f"## ✅ Your password is **strong**! 🎉"
        strength = "Strong"

    st.markdown(message)

    # Estimate cracking time for user input password
    st.info(estimate_crack_time(password))

# Generate a strong password
st.subheader("Generate a Strong Password")

length = st.slider("Select Length:", 8, 20, 12)

# Generate button
if st.button("Generate Password"):
    if length < 8:
        st.warning("⚠️ Length must be at least 8 characters.")
    else:
        chars = string.ascii_letters + string.digits + "@#$%&!?"
        new_password = ''.join(secrets.choice(chars) for _ in range(length))

        st.markdown(f"## 🔑 Generated Password: `{new_password}`")
        st.info(estimate_crack_time(new_password))
