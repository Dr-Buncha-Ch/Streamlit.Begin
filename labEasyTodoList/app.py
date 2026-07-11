import streamlit as st
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Student Task Manager",
    page_icon="📋",
    layout="wide"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.main{
    padding-top:20px;
}

h1{
    color:#1f77b4;
}

.stButton>button{
    width:100%;
    border-radius:8px;
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# INITIAL DATA
# =====================================================


def init_data():

    if "tasks" not in st.session_state:

        st.session_state.tasks = []

    if "next_id" not in st.session_state:

        st.session_state.next_id = 1

# =====================================================
# CREATE
# =====================================================

def add_task(title, status):

    task = {
        "ID": st.session_state.next_id,
        "Task": title,
        "Status": status
    }

    st.session_state.tasks.append(task)

    st.session_state.next_id += 1

# =====================================================
# READ
# =====================================================

def get_dataframe():

    return pd.DataFrame(st.session_state.tasks)

# =====================================================
# UPDATE
# =====================================================

def update_task(task_id, title, status):

    for task in st.session_state.tasks:

        if task["ID"] == task_id:

            task["Task"] = title
            task["Status"] = status
            break

# =====================================================
# DELETE
# =====================================================

def delete_task(task_id):

    st.session_state.tasks = [

        task

        for task in st.session_state.tasks

        if task["ID"] != task_id

    ]




# =====================================================
# MAIN
# =====================================================

# =====================================================
#    ส่วนที่ 1 สร้างข้อมูล
# =====================================================

init_data()

st.title("📋 Student Task Manager (Memory Version)")

st.write(
    "ข้อมูลทั้งหมดถูกเก็บใน **Session Memory** "
    "เมื่อปิดโปรแกรมข้อมูลจะหาย"
)

st.divider()


# Check Point 001
#"""  เริ่มคอมเม้นต์ใหญ่ ทั้งหมด


# =====================================================
#    ส่วนที่ 2 สร้าง Form
# =====================================================


# =====================================================
# CREATE FORM
# =====================================================

st.header("➕ Add Task")

col1, col2 = st.columns([3, 1])

with col1:

    title = st.text_input("Task Name")

with col2:

    status = st.selectbox(
        "Status",
        ["Pending", "Done"]
    )

if st.button("Save Task"):

    if title.strip() == "":

        st.warning("Please enter task name")

    else:

        add_task(title, status)

        st.success("Task Added")

        st.rerun()

st.divider()


# Check Point 002
#"""  เริ่มคอมเม้นต์ใหญ่ ทั้งหมด


# =====================================================
# READ TABLE
# =====================================================

st.header("📋 Task List")

df = get_dataframe()

# -----------------------
# SEARCH
# -----------------------

search = st.text_input("🔍 Search")

if not df.empty:

    if search:

        df = df[
            df["Task"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

# -----------------------
# SORT
# -----------------------

sort = st.selectbox(

    "Sort By",

    ["ID", "Task", "Status"]

)

if not df.empty:

    df = df.sort_values(sort)

st.dataframe(

    df,

    use_container_width=True,

    hide_index=True

)

st.divider()


# Check Point 003
#"""  เริ่มคอมเม้นต์ใหญ่ ทั้งหมด


# =====================================================
# UPDATE / DELETE
# =====================================================

st.header("✏️ Update / Delete")

if len(st.session_state.tasks) == 0:

    st.info("No Task")

else:

    for task in st.session_state.tasks:

        with st.expander(

            f"#{task['ID']} : {task['Task']}"

        ):

            new_title = st.text_input(

                "Task",

                value=task["Task"],

                key=f"title_{task['ID']}"

            )

            new_status = st.selectbox(

                "Status",

                ["Pending", "Done"],

                index=0 if task["Status"] == "Pending" else 1,

                key=f"status_{task['ID']}"

            )

            c1, c2 = st.columns(2)

            with c1:

                if st.button(

                    "💾 Update",

                    key=f"update_{task['ID']}"

                ):

                    update_task(

                        task["ID"],

                        new_title,

                        new_status

                    )

                    st.success("Updated")

                    st.rerun()

            with c2:

                confirm = st.checkbox(

                    "Confirm Delete",

                    key=f"confirm_{task['ID']}"

                )

                if confirm:

                    if st.button(

                        "🗑 Delete",

                        key=f"delete_{task['ID']}"

                    ):

                        delete_task(task["ID"])

                        st.success("Deleted")

                        st.rerun()

# Check Point 003
#"""  เริ่มคอมเม้นต์ใหญ่ ทั้งหมด

#"""  #ปิดคอมเม้นต์ ใหญ่ ทั้งหมด         

st.divider()

# =====================================================
# DEBUG (ใช้สอน)
# =====================================================

with st.expander("📦 Session State (สำหรับการเรียนรู้)"):

    st.write(st.session_state)
