import streamlit as st
import pandas as pd
import os


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="MeetTrack AI",
    page_icon="🎯",
    layout="wide"
)


# =========================================================
# SESSION STATE
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

if "files_uploaded" not in st.session_state:
    st.session_state.files_uploaded = False


# =========================================================
# CSS DESIGN
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #eaf4ff,
        #f8fbff,
        #dceeff
    );
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1 {
    color: #0b3d91 !important;
}

h2 {
    color: #0b3d91 !important;
}

h3 {
    color: #1769d2 !important;
}

.stButton > button {
    width: 100%;
    min-height: 45px;

    background: linear-gradient(
        135deg,
        #1769d2,
        #0b3d91
    );

    color: white !important;

    border: none;
    border-radius: 10px;

    font-weight: 600;
    font-size: 15px;
}

.stButton > button:hover {
    background: linear-gradient(
        135deg,
        #0b3d91,
        #1769d2
    );

    color: white !important;
}

.stTextInput input {
    min-height: 42px;
    border-radius: 9px;
    border: 1px solid #b8d4f5;
    background-color: white;
}

[data-testid="stFileUploader"] {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #d5e5f7;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0b3d91,
        #1769d2
    );
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.metric-box {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    border-top: 5px solid #1769d2;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}

.info-box {
    background-color: white;
    padding: 22px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    border-left: 5px solid #1769d2;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIGN IN PAGE
# =========================================================

def signin_page():

    st.write("")

    left, center, right = st.columns([1, 1.4, 1])

    with center:

        st.info(
            "🎯  MeetTrack AI\n\n"
            "AI Meeting-to-Accountability System\n\n"
            "✨ Capture  •  📋 Track  •  🎯 Achieve"
        )

        st.write("")

        st.markdown("## 👋 Welcome Back!")

        st.write(
            "Sign in to continue to your dashboard."
        )

        st.write("")

        username = st.text_input(
            "Username",
            placeholder="Enter your username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password"
        )

        st.write("")

        if st.button(
            "🔐 Sign In",
            use_container_width=True
        ):

            if username and password:

                st.session_state.logged_in = True
                st.session_state.page = "Dashboard"

                st.rerun()

            else:

                st.error(
                    "Please enter username and password."
                )

        st.write("")

        st.divider()

        st.write(
            "Don't have an account?"
        )

        if st.button(
            "✨ Create New Account",
            use_container_width=True
        ):

            st.session_state.show_signup = True

            st.rerun()

        st.caption(
            "🔒 Your meeting information is organized "
            "and tracked securely."
        )


# =========================================================
# SIGN UP PAGE
# =========================================================

def signup_page():

    st.write("")

    left, center, right = st.columns([1, 1.4, 1])

    with center:

        st.info(
            "🎯  MeetTrack AI\n\n"
            "Create your account"
        )

        st.write("")

        st.markdown("## ✨ Create Account")

        st.write(
            "Enter your details below."
        )

        st.write("")

        name = st.text_input(
            "Full Name",
            placeholder="Enter your full name"
        )

        email = st.text_input(
            "Email",
            placeholder="Enter your email"
        )

        username = st.text_input(
            "Username",
            placeholder="Create a username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Create a password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            placeholder="Enter password again"
        )

        st.write("")

        if st.button(
            "✨ Create Account",
            use_container_width=True
        ):

            if not name:

                st.error(
                    "Please enter your name."
                )

            elif not email:

                st.error(
                    "Please enter your email."
                )

            elif not username:

                st.error(
                    "Please create a username."
                )

            elif not password:

                st.error(
                    "Please create a password."
                )

            elif password != confirm_password:

                st.error(
                    "Passwords do not match."
                )

            else:

                st.success(
                    "Account created successfully!"
                )

                st.info(
                    "Please go back to Sign In."
                )

        st.write("")

        if st.button(
            "← Back to Sign In",
            use_container_width=True
        ):

            st.session_state.show_signup = False

            st.rerun()


# =========================================================
# SIDEBAR
# =========================================================

def sidebar():

    st.sidebar.title(
        "🎯 MeetTrack AI"
    )

    st.sidebar.write(
        "Meeting Accountability System"
    )

    st.sidebar.divider()

    if st.sidebar.button(
        "🏠 Dashboard",
        use_container_width=True
    ):

        st.session_state.page = "Dashboard"

        st.rerun()

    if st.sidebar.button(
        "🎙️ New Meeting",
        use_container_width=True
    ):

        st.session_state.page = "New Meeting"

        st.rerun()

    if st.sidebar.button(
        "📝 Transcript",
        use_container_width=True
    ):

        st.session_state.page = "Transcript"

        st.rerun()

    if st.sidebar.button(
        "🤖 Analysis",
        use_container_width=True
    ):

        st.session_state.page = "Analysis"

        st.rerun()

    if st.sidebar.button(
        "📋 Action Items",
        use_container_width=True
    ):

        st.session_state.page = "Action Items"

        st.rerun()

    if st.sidebar.button(
        "📜 Meeting History",
        use_container_width=True
    ):

        st.session_state.page = "History"

        st.rerun()

    st.sidebar.divider()

    if st.sidebar.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False

        st.session_state.page = "Dashboard"

        st.rerun()


# =========================================================
# DASHBOARD
# =========================================================

def dashboard():

    st.title(
        "🎯 MeetTrack AI"
    )

    st.subheader(
        "Welcome to your Meeting Accountability Dashboard"
    )

    st.write(
        "Track meetings, tasks, owners and deadlines in one place."
    )

    st.write("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "📅 Total Meetings",
            "5"
        )

    with col2:

        st.metric(
            "📋 Action Items",
            "12"
        )

    with col3:

        st.metric(
            "✅ Completed",
            "7"
        )

    with col4:

        st.metric(
            "⚠️ Overdue",
            "3"
        )

    st.write("")

    st.info(
        "🎙️ Start a New Meeting\n\n"
        "Upload your meeting recordings and "
        "let MeetTrack AI identify tasks, "
        "owners and deadlines."
    )

    if st.button(
        "🎙️ Start New Meeting",
        use_container_width=True
    ):

        st.session_state.page = "New Meeting"

        st.rerun()

    st.write("")

    st.subheader(
        "📌 Recent Action Items"
    )

    data = {

        "Task": [
            "Complete database",
            "Complete dashboard",
            "Test the system"
        ],

        "Owner": [
            "Pooja",
            "Prathiksha",
            "Not decided"
        ],

        "Deadline": [
            "Today",
            "Tomorrow evening",
            "Not decided"
        ],

        "Status": [
            "New",
            "New",
            "Unresolved"
        ]
    }

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# NEW MEETING PAGE
# =========================================================

def new_meeting():

    st.title(
        "🎙️ New Meeting"
    )

    st.subheader(
        "Upload your 26 conversation recordings"
    )

    st.info(
        "Use this filename format:\n\n"
        "01_HR.mp4\n"
        "02_POOJA.mp4\n"
        "03_PRATHIKSHA.mp4\n"
        "04_POOJA.mp4\n"
        "05_HR.mp4\n"
        "... and so on"
    )

    uploaded_files = st.file_uploader(
        "Upload Meeting Audio Files",
        type=[
            "mp4",
            "mp3",
            "wav",
            "m4a"
        ],
        accept_multiple_files=True
    )

    if uploaded_files:

        uploaded_files = sorted(
            uploaded_files,
            key=lambda file: file.name
        )

        st.session_state.files_uploaded = True

        st.success(
            f"{len(uploaded_files)} audio files uploaded."
        )

        st.subheader(
            "🎧 Conversation Order"
        )

        for file in uploaded_files:

            filename = file.name.upper()

            if "_HR" in filename:

                speaker = "HR"

            elif "_POOJA" in filename:

                speaker = "Pooja"

            elif "_PRATHIKSHA" in filename:

                speaker = "Prathiksha"

            else:

                speaker = "Unknown"

            st.write(
                f"🎙️ **{speaker}** — {file.name}"
            )

        st.write("")

        # =================================================
        # STEP 1
        # =================================================

        st.subheader(
            "🎙️ Step 1: Generate Transcript"
        )

        if st.button(
            "🎙️ Generate Transcript",
            use_container_width=True
        ):

            st.info(
                "⏳ Transcript generation will be connected "
                "to Member 3's transcription module."
            )

            st.write(
                "The uploaded recordings are ready. "
                "Member 3's transcription code will be "
                "connected to this button."
            )

        st.write("")

        # =================================================
        # STEP 2
        # =================================================

        st.subheader(
            "📝 Step 2: View Transcript"
        )

        if st.button(
            "📝 View Transcript",
            use_container_width=True
        ):

            st.session_state.page = "Transcript"

            st.rerun()

        st.write("")

        # =================================================
        # STEP 3
        # =================================================

        st.subheader(
            "🤖 Step 3: Analyse Meeting"
        )

        if st.button(
            "🤖 Analyse Meeting",
            use_container_width=True
        ):

            st.session_state.page = "Analysis"

            st.rerun()


# =========================================================
# TRANSCRIPT PAGE
# =========================================================

def transcript_page():

    st.title(
        "📝 Meeting Transcript"
    )

    st.write(
        "View and manage the transcript generated "
        "from your meeting recordings."
    )

    st.write("")

    # =====================================================
    # BUTTONS
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🎙️ Generate Transcript",
            use_container_width=True
        ):

            st.info(
                "⏳ Transcript generation will be connected "
                "to Member 3's transcription module."
            )

            st.write(
                "Once Member 3 completes the transcription "
                "module, it will generate the transcript here."
            )

    with col2:

        if st.button(
            "📝 View Transcript",
            use_container_width=True
        ):

            st.success(
                "You are already on the Transcript page."
            )

    st.write("")

    st.divider()

    # =====================================================
    # TRANSCRIPT FOLDER
    # =====================================================

    transcript_folder = "transcripts"

    # =====================================================
    # CHECK FOLDER
    # =====================================================

    if not os.path.exists(
        transcript_folder
    ):

        st.warning(
            "⚠️ No transcripts found yet."
        )

        st.info(
            "Member 3's transcription module will "
            "generate the transcript files here."
        )

        st.write("")

        st.subheader(
            "📂 Expected Folder"
        )

        st.code(
            "transcripts/",
            language="text"
        )

        st.write("")

        st.subheader(
            "🔄 Current Status"
        )

        st.write(
            "🎙️ Meeting recordings → Waiting"
        )

        st.write(
            "📝 Transcript → Waiting for Member 3"
        )

        st.write(
            "🤖 AI Analysis → Ready after transcript"
        )

        return

    # =====================================================
    # FIND TXT FILES
    # =====================================================

    transcript_files = [

        file

        for file in os.listdir(
            transcript_folder
        )

        if file.lower().endswith(".txt")
    ]

    transcript_files.sort()

    # =====================================================
    # IF EMPTY
    # =====================================================

    if len(transcript_files) == 0:

        st.warning(
            "⚠️ The transcripts folder is currently empty."
        )

        st.info(
            "Waiting for Member 3's transcription output."
        )

        st.write("")

        st.subheader(
            "🔄 Processing Status"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "🎙️ Recordings",
                "26"
            )

        with col2:

            st.metric(
                "📝 Transcripts",
                "0"
            )

        with col3:

            st.metric(
                "🤖 Analysis",
                "Waiting"
            )

        return

    # =====================================================
    # TRANSCRIPTS FOUND
    # =====================================================

    st.success(
        f"✅ {len(transcript_files)} transcript files found."
    )

    st.write("")

    selected_file = st.selectbox(
        "Select a transcript to view",
        transcript_files
    )

    st.write("")

    selected_path = os.path.join(
        transcript_folder,
        selected_file
    )

    # =====================================================
    # READ TRANSCRIPT
    # =====================================================

    try:

        with open(
            selected_path,
            "r",
            encoding="utf-8"
        ) as file:

            transcript_text = file.read()

        st.subheader(
            f"🎙️ {selected_file}"
        )

        if transcript_text.strip():

            st.text_area(
                "Transcript",
                transcript_text,
                height=400
            )

        else:

            st.warning(
                "This transcript is empty."
            )

    except Exception as error:

        st.error(
            f"Unable to read transcript: {error}"
        )

    st.write("")

    # =====================================================
    # ALL TRANSCRIPTS
    # =====================================================

    st.subheader(
        "📚 All Transcripts"
    )

    for file in transcript_files:

        file_path = os.path.join(
            transcript_folder,
            file
        )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            text = f.read()

        with st.expander(
            f"🎙️ {file}"
        ):

            if text.strip():

                st.write(text)

            else:

                st.write(
                    "No transcript available."
                )

    st.write("")

    # =====================================================
    # CONTINUE TO ANALYSIS
    # =====================================================

    if st.button(
        "🤖 Continue to Analysis",
        use_container_width=True
    ):

        st.session_state.page = "Analysis"

        st.rerun()


# =========================================================
# ANALYSIS PAGE
# =========================================================

def analysis():

    st.title(
        "🤖 Meeting Analysis"
    )

    st.subheader(
        "AI analysis of the complete meeting"
    )

    st.write("")

    st.info(
        "This section will be connected to the "
        "GenAI extraction module after the transcript "
        "is available."
    )

    st.write("")

    st.success(
        "✅ Transcript processing ready"
    )

    st.success(
        "✅ Action item extraction ready"
    )

    st.success(
        "✅ Owner detection ready"
    )

    st.success(
        "✅ Deadline detection ready"
    )

    st.warning(
        "⚠️ Unresolved issues will be identified "
        "by the AI module."
    )

    st.write("")

    st.subheader(
        "📋 Extracted Action Items"
    )

    data = {

        "Action Item": [
            "Complete database",
            "Complete dashboard",
            "Test the system"
        ],

        "Owner": [
            "Pooja",
            "Prathiksha",
            "Not decided"
        ],

        "Deadline": [
            "Today",
            "Tomorrow evening",
            "Not decided"
        ],

        "Status": [
            "New",
            "New",
            "Unresolved"
        ]
    }

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.subheader(
        "🔎 Evidence from Conversation"
    )

    st.info(
        'Pooja: "I can finish it today."'
    )

    st.info(
        'Prathiksha: '
        '"I can finish it by tomorrow evening."'
    )

    st.warning(
        "Testing owner has not been decided."
    )

    st.write("")

    if st.button(
        "📋 View Action Items",
        use_container_width=True
    ):

        st.session_state.page = "Action Items"

        st.rerun()


# =========================================================
# ACTION ITEMS PAGE
# =========================================================

def action_items():

    st.title(
        "📋 Action Item Tracker"
    )

    st.write(
        "Track all tasks from your meetings."
    )

    data = {

        "Task": [
            "Complete database",
            "Complete dashboard",
            "Test the system",
            "Review meeting tasks"
        ],

        "Owner": [
            "Pooja",
            "Prathiksha",
            "Not decided",
            "HR"
        ],

        "Deadline": [
            "Today",
            "Tomorrow evening",
            "Not decided",
            "Next meeting"
        ],

        "Status": [
            "New",
            "New",
            "Unresolved",
            "Carried Over"
        ]
    }

    df = pd.DataFrame(data)

    selected_status = st.selectbox(
        "Filter by Status",
        [
            "All",
            "New",
            "In Progress",
            "Completed",
            "Carried Over",
            "Overdue",
            "Unresolved"
        ]
    )

    if selected_status != "All":

        df = df[
            df["Status"] == selected_status
        ]

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# MEETING HISTORY
# =========================================================

def history():

    st.title(
        "📜 Meeting History"
    )

    st.write(
        "Previous meetings and their action items."
    )

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
            3,
            5,
            4
        ],

        "Status": [
            "In Progress",
            "Completed",
            "In Progress"
        ]
    }

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# MAIN PROGRAM
# =========================================================

if not st.session_state.logged_in:

    if st.session_state.show_signup:

        signup_page()

    else:

        signin_page()

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

    elif st.session_state.page == "History":

        history()