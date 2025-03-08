import streamlit as st

# My App Title
st.title("📝 My Todo App")

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Sidebar Heading
st.sidebar.header("Manage Your Task")

# Text input for new task
new_task = st.sidebar.text_input("Add a new task", placeholder="Enter Your Task Here")

if st.sidebar.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task, "completed": False})
        st.sidebar.success("Task Added Successfully")
        st.rerun()  # ✅ Use st.rerun() instead of st.experimental_rerun()
    else:
        st.sidebar.warning("Task is Not Added. Please enter a valid task.")

# Display tasks
st.subheader("Your TO-DO List")

if not st.session_state.tasks:
    st.info("No tasks added yet. Start adding tasks from the sidebar!")
else:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.7, 0.15, 0.15])

        # Mark as Completed
        completed = col1.checkbox(f"**{task['task']}**", task["completed"], key=f'checkbox_{index}')
        if completed != task["completed"]:
            st.session_state.tasks[index]["completed"] = completed
            st.rerun()  # ✅ Use st.rerun()

        # Edit Task
        if col2.button("✏️ Edit", key=f'edit_{index}'):
            st.session_state.edit_index = index  # Store the index of the task being edited

        if "edit_index" in st.session_state and st.session_state.edit_index == index:
            new_task_text = st.text_input("Edit task", task["task"], key=f'new_task_{index}')
            if st.button("💾 Save", key=f'save_{index}'):
                st.session_state.tasks[index]["task"] = new_task_text
                del st.session_state.edit_index  # Remove edit mode
                st.rerun()  # ✅ Use st.rerun()

        # Delete Task
        if col3.button("🗑️ Delete", key=f'delete_{index}'):
            del st.session_state.tasks[index]
            st.rerun()  # ✅ Use st.rerun()

# Clear All Tasks
if st.button("🧹 Clear All Tasks"):
    st.session_state.tasks = []
    st.success("All Tasks Have Been Deleted Successfully")
    st.rerun()  # ✅ Use st.rerun()

# Footer
st.markdown("---")
st.caption("Stay Organized and Productive with this To-Do List")
