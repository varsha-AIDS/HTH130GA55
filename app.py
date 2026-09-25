import streamlit as st
import pandas as pd
import os

from transcriber import transcribe_audio
from diarization import diarize_audio


# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="MeetTrack AI",
    page_icon="🎙️",
    layout="wide"
)


# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

.stButton > button {
    border-radius: 8px;
    font-weight: 600;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.title {
    font-size: 32px;
    font-weight: bold;
}

.subtitle {
    font-size: 18px;
    color: #666;
}

</style>
""", unsafe_allow_html=True)


# =====================================
# SESSION STATE
# =====================================

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "meetings" not in st.session_state:
    st.session_state.meetings = []


# =====================================
# SIGN IN PAGE
# =====================================

def sign_in():

    st.title("🎙️ MeetTrack AI")

    st.subheader("Sign In")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Sign In"):

        if username and password:

            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.page = "Dashboard"

            st.rerun()

        else:

            st.error(
                "Please enter username and password."
            )

    st.divider()

    if st.button("Create New Account"):

        st.session_state.page = "Sign Up"

        st.rerun()


# =====================================
# SIGN UP PAGE
# =====================================

def sign_up():

    st.title("🎙️ MeetTrack AI")

    st.subheader("Create Account")

    username = st.text_input("Username")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button("Create Account"):

        if not username or not email or not password:

            st.error(
                "Please fill all fields."
            )

        elif password != confirm_password:

            st.error(
                "Passwords do not match."
            )

        else:

            st.success(
                "Account created successfully!"
            )

            st.session_state.page = "Sign In"

            st.rerun()

    if st.button("Back to Sign In"):

        st.session_state.page = "Sign In"

        st.rerun()


# =====================================
# SIDEBAR
# =====================================

def sidebar():

    st.sidebar.title("🎙️ MeetTrack AI")

    st.sidebar.write(
        f"Welcome, {st.session_state.username}"
    )

    st.sidebar.divider()

    if st.sidebar.button("🏠 Dashboard"):

        st.session_state.page = "Dashboard"

        st.rerun()

    if st.sidebar.button("➕ New Meeting"):

        st.session_state.page = "New Meeting"

        st.rerun()

    if st.sidebar.button("📄 Transcript"):

        st.session_state.page = "Transcript"

        st.rerun()

    if st.sidebar.button("📊 Analysis"):

        st.session_state.page = "Analysis"

        st.rerun()

    if st.sidebar.button("✅ Action Items"):

        st.session_state.page = "Action Items"

        st.rerun()

    if st.sidebar.button("🕒 Meeting History"):

        st.session_state.page = "Meeting History"

        st.rerun()

    st.sidebar.divider()

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.page = "Sign In"

        st.rerun()


# =====================================
# DASHBOARD
# =====================================

def dashboard():

    st.title("🏠 Dashboard")

    st.write(
        "AI-powered meeting accountability system"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Total Meetings",
            5
        )

    with col2:

        st.metric(
            "Action Items",
            12
        )

    with col3:

        st.metric(
            "Completed",
            7
        )

    with col4:

        st.metric(
            "Overdue",
            3
        )

    st.divider()

    st.subheader(
        "📌 Recent Action Items"
    )

    data = {

        "Task": [
            "Complete database",
            "Finish dashboard",
            "Test system"
        ],

        "Owner": [
            "Pooja",
            "Prathiksha",
            "Not decided"
        ],

        "Deadline": [
            "Today",
            "Tomorrow evening",
            "Next meeting"
        ],

        "Status": [
            "New",
            "New",
            "Carried-over"
        ]

    }

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True
    )


# =====================================
# NEW MEETING
# =====================================

def new_meeting():

    st.title("➕ New Meeting")

    st.write(
        "Upload your meeting recording."
    )

    file = st.file_uploader(
        "Upload Meeting Recording",
        type=[
            "mp4",
            "mp3",
            "wav",
            "m4a"
        ]
    )

    if file:

        st.success(
            f"File uploaded: {file.name}"
        )

        if st.button(
            "🎙️ Generate Transcript"
        ):

            with st.spinner(
                "Transcribing audio..."
            ):

                transcript = transcribe_audio(file)

            st.subheader(
                "📝 Transcript"
            )

            st.text_area(
                "Transcript",
                transcript,
                height=300
            )

            # =====================================
            # SPEAKER DIARIZATION
            # =====================================

            file.seek(0)

            speaker_segments = diarize_audio(file)

            st.subheader(
                "🎙️ Speaker Diarization"
            )

            for segment in speaker_segments:

                st.write(
                    f"{segment['speaker']} : "
                    f"{segment['start']:.2f}s - "
                    f"{segment['end']:.2f}s"
                )


# =====================================
# TRANSCRIPT PAGE
# =====================================

def transcript_page():

    st.title("📄 Meeting Transcript")

    transcript_folder = "transcripts"

    if os.path.exists(transcript_folder):

        files = [
            file
            for file in os.listdir(transcript_folder)
            if file.endswith(".txt")
        ]

        if files:

            selected_file = st.selectbox(
                "Select Transcript",
                files
            )

            file_path = os.path.join(
                transcript_folder,
                selected_file
            )

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as f:

                transcript = f.read()

            st.text_area(
                "Transcript",
                transcript,
                height=500
            )

        else:

            st.info(
                "No transcripts available."
            )

    else:

        st.info(
            "Transcript folder not found."
        )


# =====================================
# ANALYSIS PAGE
# =====================================

def analysis():

    st.title("📊 Meeting Analysis")

    st.subheader(
        "Extracted Information"
    )

    data = {

        "Task": [
            "Work on database",
            "Work on dashboard",
            "Track unfinished tasks"
        ],

        "Owner": [
            "Pooja",
            "Prathiksha",
            "Not decided"
        ],

        "Deadline": [
            "Today",
            "Tomorrow evening",
            "Next meeting"
        ],

        "Evidence": [
            "I will work on the database.",
            "I will work on the dashboard.",
            "We should also track unfinished tasks."
        ]

    }

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True
    )


# =====================================
# ACTION ITEMS PAGE
# =====================================

def action_items():

    st.title("✅ Action Items")

    data = {

        "Task": [
            "Complete database",
            "Finish dashboard",
            "Track unfinished tasks"
        ],

        "Owner": [
            "Pooja",
            "Prathiksha",
            "Not decided"
        ],

        "Deadline": [
            "Today",
            "Tomorrow evening",
            "Next meeting"
        ],

        "Status": [
            "New",
            "New",
            "Carried-over"
        ]

    }

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True
    )


# =====================================
# MEETING HISTORY
# =====================================

def meeting_history():

    st.title("🕒 Meeting History")

    data = {

        "Meeting": [
            "Project Meeting 1",
            "Project Meeting 2",
            "Project Meeting 3"
        ],

        "Date": [
            "Today",
            "Yesterday",
            "2 days ago"
        ],

        "Action Items": [
            5,
            4,
            3
        ]

    }

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True
    )


# =====================================
# MAIN APPLICATION
# =====================================

if not st.session_state.logged_in:

    if st.session_state.page == "Sign Up":

        sign_up()

    else:

        sign_in()

else:

    sidebar()

    if st.session_state.page == "Dashboard":

        dashboard()

    elif st.session_state.page == "New Meeting":

        new_meeting()

    elif st.session_state.page == "Transcript":

        transcript_page()

    elif st.session_state.page == "Analysis":

        analysis()

    elif st.session_state.page == "Action Items":

        action_items()

    elif st.session_state.page == "Meeting History":

        meeting_history()
        