import streamlit as st

st.set_page_config(page_title="Task Manager", page_icon="📝", layout="centered")

# ---------- Custom Dark Theme ----------
st.markdown("""
<style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .task-card {
        background-color: #1c1f26;
        padding: 12px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 1px solid #2a2f3a;
    }
    .stTextInput > div > div > input {
        background-color: #0e1117;
        color: white;
    }
    .stButton > button {
        background-color: #262730;
        color: white;
        border-radius: 8px;
        border: none;
    }
    .stButton > button:hover {
        background-color: #3a3f4b;
    }
</style>
""", unsafe_allow_html=True)

st.title("📝 Task Management System")

# ---------- Session State ----------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ---------- Add Task ----------
st.subheader("➕ Add New Task")

new_task = st.text_input("Task name", placeholder="Enter your task here")

if st.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task, "done": False})
        st.success("Task added!")
    else:
        st.warning("Task cannot be empty")

st.divider()

# ---------- Task List ----------
st.subheader("📋 Your Tasks")

if not st.session_state.tasks:
    st.info("No tasks yet. Add one above ☝️")
else:
    for i, item in enumerate(st.session_state.tasks):
        st.markdown('<div class="task-card">', unsafe_allow_html=True)

        col1, col2, col3 = st.columns([6, 1.5, 1.5])

        # Task Name
        with col1:
            if item["done"]:
                st.markdown(f"~~{item['task']}~~")
            else:
                st.markdown(item["task"])

        # Done Button
        with col2:
            if st.button("✅ Done", key=f"done_{i}"):
                st.session_state.tasks[i]["done"] = not item["done"]
                st.rerun()

        # Delete Button
        with col3:
            if st.button("🗑 Delete", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)
