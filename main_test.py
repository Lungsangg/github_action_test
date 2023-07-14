import streamlit as st 

def test_display_text():
    title = st.text_input('Movie title', 'Life of Pie')
    result = st.write('The current movie title is', title)
    return result

    

if __name__ == "__main__":
    test_display_text()    