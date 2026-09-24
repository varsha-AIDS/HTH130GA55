import sqlite3
import os


# ==========================================
# Database Path
# ==========================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATABASE_PATH = os.path.join(
    PROJECT_ROOT,
    "meeting_accountability.db"
)


# ==========================================
# Database Connection
# ==========================================

def get_connection():
    return sqlite3.connect(DATABASE_PATH)


# ==========================================
# Create Tables
# ==========================================

def create_tables():

    connection = get_connection()
    cursor = connection.cursor()

    # Users Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    """)

    # Meetings Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS meetings (
            meeting_id INTEGER PRIMARY KEY AUTOINCREMENT,
            meeting TEXT NOT NULL,
            person TEXT,
            task TEXT NOT NULL,
            deadline TEXT,
            status TEXT,
            evidence TEXT
        )
    """)

    connection.commit()
    connection.close()

    print("Database created successfully!")
    print("Tables created successfully!")


# ==========================================
# Add User
# ==========================================

def add_user(username, password):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute("""
            INSERT INTO users
            (username, password)
            VALUES (?, ?)
        """, (
            username,
            password
        ))

        connection.commit()
        connection.close()

        return True

    except sqlite3.IntegrityError:

        connection.close()

        return False


# ==========================================
# Check Login
# ==========================================

def check_login(username, password):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT username
        FROM users
        WHERE username = ?
        AND password = ?
    """, (
        username,
        password
    ))

    user = cursor.fetchone()

    connection.close()

    return user


# ==========================================
# Add Meeting
# ==========================================

def add_meeting(
    meeting,
    person,
    task,
    deadline,
    status,
    evidence
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO meetings
        (
            meeting,
            person,
            task,
            deadline,
            status,
            evidence
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        meeting,
        person,
        task,
        deadline,
        status,
        evidence
    ))

    connection.commit()
    connection.close()


# ==========================================
# Get All Meetings
# ==========================================

def get_meetings():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            meeting,
            person,
            task,
            deadline,
            status,
            evidence
        FROM meetings
        ORDER BY meeting_id DESC
    """)

    meetings = cursor.fetchall()

    connection.close()

    return meetings


# ==========================================
# Get Total Meetings
# ==========================================

def get_total_meetings():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(DISTINCT meeting)
        FROM meetings
    """)

    total = cursor.fetchone()[0]

    connection.close()

    return total


# ==========================================
# Get Total Tasks
# ==========================================

def get_total_tasks():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM meetings
    """)

    total = cursor.fetchone()[0]

    connection.close()

    return total


# ==========================================
# Get Tasks by Person
# ==========================================

def get_tasks_by_person(person):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            meeting,
            person,
            task,
            deadline,
            status,
            evidence
        FROM meetings
        WHERE person = ?
        ORDER BY meeting_id DESC
    """, (person,))

    tasks = cursor.fetchall()

    connection.close()

    return tasks


# ==========================================
# Get Tasks by Meeting
# ==========================================

def get_tasks_by_meeting(meeting):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            meeting,
            person,
            task,
            deadline,
            status,
            evidence
        FROM meetings
        WHERE meeting = ?
        ORDER BY meeting_id DESC
    """, (meeting,))

    tasks = cursor.fetchall()

    connection.close()

    return tasks


# ==========================================
# Update Task Status
# ==========================================

def update_status(meeting_id, status):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE meetings
        SET status = ?
        WHERE meeting_id = ?
    """, (
        status,
        meeting_id
    ))

    connection.commit()
    connection.close()


# ==========================================
# Update Evidence
# ==========================================

def update_evidence(meeting_id, evidence):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE meetings
        SET evidence = ?
        WHERE meeting_id = ?
    """, (
        evidence,
        meeting_id
    ))

    connection.commit()
    connection.close()


# ==========================================
# Run Database
# ==========================================

if __name__ == "__main__":

    create_tables()

    print()
    print("Database is ready!")