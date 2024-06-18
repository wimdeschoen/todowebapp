import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")

st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")
keynr = 1
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=str(index+1) +": " + todo )
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[str(index+1) +": " + todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo", on_change=add_todo, key="new_todo")
#to show the session state off the text from input
st.session_state

#to run type streamlit run web.py
