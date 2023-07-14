import streamlit as st 

def display_text():
    title = st.text_input('Movie title', 'Life of Pie')
    result = st.write('The current movie title is', title)
    return result

    

if __name__ == "__main__":
    display_text()    