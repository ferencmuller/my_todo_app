import streamlit as st
import functions

todos = functions.get_todos("todos.txt")


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My To-Do App")
st.subheader("This is my To-Do App")
st.text("This app is to increace your productivity ")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input("Enter a To-Do:", placeholder="Add new To-Do...",
              on_change=add_todo, key="new_todo")
