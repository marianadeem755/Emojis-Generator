import streamlit as st
import random

# Set the title of the app
st.title("🎨 Emojis Generator")
st.markdown("Welcome to the Emoji Generator App! Here, you can create your own emojis and have fun!")

# Add an introductory description
st.write("Choose an emoji category from below and click 'Generate Emoji' to see your random emoji!")

# Define emoji categories
categories = {
    "Smileys & Emotion": ["😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇", "🙂", "🙃"],
    "Animals & Nature": ["🐶", "🐱", "🐭", "🐹", "🐰", "🐻", "🐼", "🦊", "🐯", "🦄", "🐸", "🦓"],
    "Food & Drink": ["🍏", "🍔", "🍕", "🍟", "🍣", "🍜", "🍩", "🍪", "🍫", "🍷", "🍹", "🍾"],
    "Travel & Places": ["🏠", "🏢", "🏞️", "🏖️", "⛷️", "🏕️", "⛴️", "🛳️", "🌍", "🗺️", "🚀", "🛸"],
    "Objects": ["📱", "💻", "⌚", "🖱️", "📷", "🎧", "📺", "🧳", "🎮", "🖼️", "🔑", "🛋️"],
    "Symbols": ["❤️", "💔", "💯", "✅", "⚠️", "🔴", "🔵", "🟢", "🟠", "🟣", "🟡", "🟤"],
}

# Sidebar for category selection
st.sidebar.header("Choose Emoji Category")
category_choice = st.sidebar.selectbox("Select Category", list(categories.keys()))

# Add profile links to the sidebar
st.sidebar.markdown("## 🔗 Connect With Me")
st.sidebar.markdown("""
<a href="https://github.com/marianadeem755" target="_blank">🌐 GitHub</a><br>
<a href="https://www.kaggle.com/marianadeem755" target="_blank">📊 Kaggle</a><br>
<a href="mailto:marianadeem755@gmail.com">📧 Email</a><br>
<a href="https://huggingface.co/maria355" target="_blank">🤗 Hugging Face</a>
""", unsafe_allow_html=True)

# Function to generate a random emoji from the selected category
def generate_emoji(category):
    return random.choice(categories[category])

# Button to generate emoji
if st.button("Generate Emoji"):
    emoji = generate_emoji(category_choice)
    st.subheader(f"Your Emojis: {emoji}")
    st.write(f"Category: {category_choice}")
    st.balloons()  # Celebrate with balloons!

    # Display all emojis from the selected category for copying
    st.subheader("All Emojis in This Category:")
    all_emojis = " ".join(categories[category_choice])
    st.text_area("Copy all emojis from this category:", all_emojis, height=3)

    # Download all emojis as a text file
    st.download_button(
        label="Download All Emojis",
        data=all_emojis.encode("utf-8"),
        file_name=f"{category_choice}_emojis.txt",
        mime="text/plain",
    )

st.markdown(
    """
    <style>
    /* Main app background */
    .stApp {
        background-image: url('https://marketplace.canva.com/EAE90fimAU8/1/0/1600w/canva-yellow-dan-orange-simple-minimalist-shape-linktree-background-Sscj5IZDNaE.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Sidebar background */
    section[data-testid="stSidebar"] > div:first-child {
        background-image: url('https://img.freepik.com/free-vector/hand-drawn-minimal-background_23-2149000980.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
