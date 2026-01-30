import streamlit as st
import functions

def add_todo():
    todo=st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


todos=functions.get_todos()

st.title("Welcome to To-do App")
st.subheader("track all my activities")
st.write("This is a simple web application built with Streamlit.")
st.write("You can add more features and functionalities as needed.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"todo_{index}"]
        st.rerun()




st.text_input(
    label="add todo",
    placeholder="Add a new to-do...",
    key="new_todo",
    on_change=add_todo,
    label_visibility="collapsed"
)


