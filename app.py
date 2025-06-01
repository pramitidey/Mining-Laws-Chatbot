import streamlit as st
import json

# Load data from the JSON file
def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        st.error("Error: 'data.json' file not found. Ensure it is in the same directory as 'app.py'.")
        return {}

# Get a response based on the query
def get_response(query, data):
    query_lower = query.lower()
    for act, description in data.items():
        if query_lower in act.lower() or query_lower in description.lower():
            return f"### {act}\n{description}"
    return "⚠ *Sorry, I couldn't find any information related to your query. Please try again!*"

# Main chatbot application
def main():
    # Set page configuration
    st.set_page_config(
        page_title="Mining Industry Regulations Chatbot",
        page_icon="⛏",
        layout="centered"
    )

    # Add a title and description
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Mining Industry Regulations Chatbot</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Find information about mining acts, rules, and regulations instantly!</p>", unsafe_allow_html=True)

    # Add a banner image (optional)
    # st.image("images/metals-and-mining.jpg", use_container_width=True)
    # with open("images/metals-and-mining.jpg", "rb") as img_file:
    #     st.image(img_file, use_container_width=True)

  # Use updated parameter

    # Add user input box
    st.markdown("<h3 style='color: #2196F3;'>Ask me about any mining act or regulation:</h3>", unsafe_allow_html=True)
    query = st.text_input("", placeholder="E.g., Mines Act 1952, Environmental Protection Act")

    # Load the data source
    data = load_data()

    # Provide response if query is entered
    if query:
        response = get_response(query, data)
        st.markdown(response, unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <hr>
        <p style='text-align: center; color: grey;'>
            Built with ❤ using Streamlit | Designed for mining professionals and enthusiasts
        </p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":

    main()