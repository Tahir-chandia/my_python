import streamlit as st
# My App Title
st.title("My Todo App")
# Installation for session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []
# Sidebar Heading
st.sidebar.header("Manage Your Task")

# Text_Input
new_task =st.sidebar.text_input("Add a new task",placeholder="Enter Your Task Here")

if st.sidebar.button("Add Task"):
  if new_task.strip():
    st.session_state.task.append({"task":new_task,"completed":False})
    st.success("Task Added Successfully")
else:
  st.warning("Task is Not Added")

# display tasks
st.subheader("Your TO-DO list")
if not st.session_state.tasks:
  st.info("No Task Added Start Adding by Sidebar!")
else:
  for index , task in enumerate(st.session_state.tasks):
        col,col2,col3 = st.columns([0.7,0.15,0.15])

# Mark it as Completed
completed = col.checkbox(f"**{task['tasks']}**",task["completed"],key=f'edit{index}')
if completed != task["completed"]:
  st.session_state.tasks[index]["completed"] = completed

# Update Task
if col2.button("Edit",key=f'edit_{index}'):
  new_task = st.text_input("edit task",task["task"],key=f'edit_{index}')
  if new_task and st.button("save", key =f'save_{index}'):
    st.session_state.tasks[index]["task"] =new_task
    st.experimental_rerun()



# Delete Task
if col3.button("Delete",key=f'delete_{index}'):
  del st.session_state.tasks[index]
  st.experimental_rerun()


# Clear All Task
if st.button("Clear All Task"):
  st.session_state.tasks = []
  st.success = ("All Tasks Has Been Deleted Successfully")

# Footer
st.markdown("---")
st.caption("Stay Organised and Prodductive with this To-Do list")