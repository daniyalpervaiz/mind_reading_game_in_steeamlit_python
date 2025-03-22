import streamlit as st


# For the sidebar with bold and larger font
st.sidebar.markdown("<h2 style='font-size: 20px; font-weight: bold;'>Note: This game is played by 2 persons. One is you, and the other is Player. Player knows the trick of this game.</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='font-size: 18px; font-weight: bold; color:blue;'>How to play this game:</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h4 style='font-size: 16px; font-weight: bold;'>Step 1: Enter the number which you are thinking.</h4>", unsafe_allow_html=True)
st.sidebar.markdown("<h4 style='font-size: 16px; font-weight: bold;'>Step 2: Enter the same number of your friend which you are thinking for yourself.</h4>", unsafe_allow_html=True)
st.sidebar.markdown("<h4 style='font-size: 16px; font-weight: bold;'>Step 3: Ask a number to the player who is in front of you.</h4>", unsafe_allow_html=True)
st.sidebar.markdown("<h4 style='font-size: 16px; font-weight: bold;'>Step 4: After this, ask the player which number you finally got.</h4>", unsafe_allow_html=True)

# Main content with larger and bold text
st.markdown("<h2 style='font-size: 24px; font-weight: bold;'>Welcome to the game!</h2>", unsafe_allow_html=True)





# Add a title and some introductory text with emojis
st.title("🎲 **Mind Reading Game** 🧠")
st.markdown("Welcome to the **Mind Reading Game**! 🤯 Let me guide you through a fun and magical trick. Follow the instructions at Sidebar,and I'll reveal the number you've got ! ✨")

# Input fields for the user, friend, and "my" numbers
user_number = st.number_input("🤔 **Think of a number between 1 to 20 (don't tell this number to the player)**", min_value=1, max_value=20)
user_friend_number = st.number_input("🤫 **Think of the same number as your friend's (don't tell this number to the player)**", min_value=1, max_value=20)
player_number = st.number_input("👤 **Now, take another player's number (which is in front of you) (the player knows the trick of the game)**", min_value=1, max_value=20)

# Ask the user to sum the numbers
st.write("🔢 **Now, sum your number, your friend's number, and the player's number.**")
answer_sum_number = st.selectbox("✅ **Have you summed these numbers?**", ["---", "Yes", "No"])

if answer_sum_number == "Yes":
    sum_all_number = user_number + user_friend_number + player_number
    st.write(f"📊 **Your sum of all numbers is**: {sum_all_number}")
else:
    st.write("❗ **Please enter 'Yes' when you've summed the numbers.**")

# Ask if they've divided the sum by 2
st.write("➗ **Now, divide this number by 2.**")
answer_divide_number = st.selectbox("✅ **Have you divided this number by 2?**", ["---", "Yes", "No"])

if answer_divide_number == "Yes":
    divide_these_number_by_2 = sum_all_number / 2
    st.write(f"💡 **You got the number**: {divide_these_number_by_2}")
else:
    st.write("❗ **Please divide the number by 2.**")

# Ask if they've returned the number to their friend
st.write("🔄 **Now return the number to your friend.**")
answer_return_number = st.selectbox("✅ **Have you returned the number to your friend?**", ["---", "Yes", "No"])

if answer_return_number == "Yes":
    retur_to_your_friend = divide_these_number_by_2 - user_friend_number
    st.success(f"🎉 **You got**: {retur_to_your_friend} 🧩. Hide this number from the player and ask them, 'What number did I get?'")
