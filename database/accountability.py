import sqlite3
import os
from datetime import datetime

# ==========================================
# Database Path
# ==========================================

PROJECT_ROOT = os.path.dirname(
    os.path.abspath(__file__)
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
# Create Database Table
# ==========================================

def create_table():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS meetings (

            meeting_id INTEGER PRIMARY KEY AUTOINCREMENT,

            meeting TEXT NOT NULL,

            meeting_date TEXT,

            person TEXT,

            task TEXT,

            deadline TEXT,

            status TEXT DEFAULT 'New',

            evidence TEXT,

            source_transcript TEXT

        )
    """)

    connection.commit()
    connection.close()


# ==========================================
# Add Meeting / Action Item
# ==========================================

def add_meeting(
    meeting,
    meeting_date,
    person,
    task,
    deadline,
    status="New",
    evidence="",
    source_transcript=""
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO meetings (
            meeting,
            meeting_date,
            person,
            task,
            deadline,
            status,
            evidence,
            source_transcript
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        meeting,
        meeting_date,
        person,
        task,
        deadline,
        status,
        evidence,
        source_transcript
    ))

    connection.commit()
    connection.close()


# ==========================================
# Get All Meeting Records
# ==========================================

def get_all_records():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            meeting_id,
            meeting,
            meeting_date,
            person,
            task,
            deadline,
            status,
            evidence,
            source_transcript

        FROM meetings

        ORDER BY meeting_id DESC
    """)

    records = cursor.fetchall()

    connection.close()

    return records


# ==========================================
# Display All Records
# ==========================================

def display_records():

    records = get_all_records()

    print()
    print("==========================================")
    print("       MEETING ACCOUNTABILITY")
    print("==========================================")

    if not records:
        print("No meeting records found.")
        return

    for record in records:

        meeting_id = record[0]
        meeting = record[1]
        meeting_date = record[2]
        person = record[3]
        task = record[4]
        deadline = record[5]
        status = record[6]
        evidence = record[7]
        source_transcript = record[8]

        print()
        print("Meeting ID :", meeting_id)
        print("Meeting :", meeting)
        print("Meeting Date :", meeting_date)
        print("Person :", person)
        print("Task :", task)
        print("Deadline :", deadline)
        print("Status :", status)
        print("Evidence :", evidence)
        print("Source Transcript :", source_transcript)

        print("------------------------------------------")


# ==========================================
# Find Tasks by Person
# ==========================================

def find_tasks_by_person(person):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            meeting_id,
            meeting,
            meeting_date,
            person,
            task,
            deadline,
            status,
            evidence,
            source_transcript

        FROM meetings

        WHERE person = ?

        ORDER BY meeting_id DESC
    """, (person,))

    records = cursor.fetchall()

    connection.close()

    return records


# ==========================================
# Display Tasks by Person
# ==========================================

def display_tasks_by_person(person):

    records = find_tasks_by_person(person)

    print()
    print("==========================================")
    print("             PERSON TASKS")
    print("==========================================")

    print("Person:", person)

    if not records:
        print("No tasks found.")
        return

    for record in records:

        print()
        print("Meeting ID :", record[0])
        print("Meeting :", record[1])
        print("Meeting Date :", record[2])
        print("Person :", record[3])
        print("Task :", record[4])
        print("Deadline :", record[5])
        print("Status :", record[6])
        print("Evidence :", record[7])
        print("Source Transcript :", record[8])


# ==========================================
# Find Tasks by Meeting
# ==========================================

def find_tasks_by_meeting(meeting):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            meeting_id,
            meeting,
            meeting_date,
            person,
            task,
            deadline,
            status,
            evidence,
            source_transcript

        FROM meetings

        WHERE meeting = ?

        ORDER BY meeting_id DESC
    """, (meeting,))

    records = cursor.fetchall()

    connection.close()

    return records


# ==========================================
# Display Tasks by Meeting
# ==========================================

def display_tasks_by_meeting(meeting):

    records = find_tasks_by_meeting(meeting)

    print()
    print("==========================================")
    print("             MEETING TASKS")
    print("==========================================")

    print("Meeting:", meeting)

    if not records:
        print("No tasks found.")
        return

    for record in records:

        print()
        print("Meeting ID :", record[0])
        print("Meeting Date :", record[2])
        print("Person :", record[3])
        print("Task :", record[4])
        print("Deadline :", record[5])
        print("Status :", record[6])
        print("Evidence :", record[7])
        print("Source Transcript :", record[8])


# ==========================================
# Check Deadline
# ==========================================

def check_deadline(deadline):

    if not deadline:
        return "No deadline"

    try:

        deadline_date = datetime.strptime(
            deadline,
            "%Y-%m-%d"
        ).date()

        today = datetime.today().date()

        if deadline_date < today:
            return "Overdue"

        elif deadline_date == today:
            return "Due Today"

        else:
            return "Upcoming"

    except ValueError:

        return "Invalid Date"


# ==========================================
# Display Deadline Information
# ==========================================

def display_deadlines():

    records = get_all_records()

    print()
    print("==========================================")
    print("             DEADLINE TRACKER")
    print("==========================================")

    if not records:
        print("No meeting records found.")
        return

    for record in records:

        meeting = record[1]
        person = record[3]
        task = record[4]
        deadline = record[5]
        status = record[6]

        deadline_status = check_deadline(deadline)

        print()
        print("Meeting :", meeting)
        print("Person :", person)
        print("Task :", task)
        print("Deadline :", deadline)
        print("Action Status :", status)
        print("Deadline Status :", deadline_status)


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
# Get Total People
# ==========================================

def get_total_people():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(DISTINCT person)
        FROM meetings
        WHERE person IS NOT NULL
        AND person != ''
    """)

    total = cursor.fetchone()[0]

    connection.close()

    return total


# ==========================================
# Get Overdue Tasks
# ==========================================

def get_overdue_tasks():

    records = get_all_records()

    overdue = 0

    for record in records:

        deadline = record[5]

        if check_deadline(deadline) == "Overdue":
            overdue += 1

    return overdue


# ==========================================
# Get Upcoming Tasks
# ==========================================

def get_upcoming_tasks():

    records = get_all_records()

    upcoming = 0

    for record in records:

        deadline = record[5]

        if check_deadline(deadline) == "Upcoming":
            upcoming += 1

    return upcoming


# ==========================================
# Get Completed Tasks
# ==========================================

def get_completed_tasks():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM meetings
        WHERE status = 'Completed'
    """)

    total = cursor.fetchone()[0]

    connection.close()

    return total


# ==========================================
# Get Carried Over Tasks
# ==========================================

def get_carried_over_tasks():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM meetings
        WHERE status = 'Carried Over'
    """)

    total = cursor.fetchone()[0]

    connection.close()

    return total


# ==========================================
# Get Unresolved Tasks
# ==========================================

def get_unresolved_tasks():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM meetings
        WHERE status = 'Unresolved'
    """)

    total = cursor.fetchone()[0]

    connection.close()

    return total


# ==========================================
# Accountability Summary
# ==========================================

def get_accountability_summary():

    summary = {

        "total_meetings": get_total_meetings(),

        "total_tasks": get_total_tasks(),

        "total_people": get_total_people(),

        "completed_tasks": get_completed_tasks(),

        "overdue_tasks": get_overdue_tasks(),

        "upcoming_tasks": get_upcoming_tasks(),

        "carried_over_tasks": get_carried_over_tasks(),

        "unresolved_tasks": get_unresolved_tasks()

    }

    return summary


# ==========================================
# Display Accountability Summary
# ==========================================

def display_summary():

    summary = get_accountability_summary()

    print()
    print("==========================================")
    print("        ACCOUNTABILITY SUMMARY")
    print("==========================================")

    print(
        "Total Meetings :",
        summary["total_meetings"]
    )

    print(
        "Total Tasks :",
        summary["total_tasks"]
    )

    print(
        "Total People :",
        summary["total_people"]
    )

    print(
        "Completed Tasks :",
        summary["completed_tasks"]
    )

    print(
        "Overdue Tasks :",
        summary["overdue_tasks"]
    )

    print(
        "Upcoming Tasks :",
        summary["upcoming_tasks"]
    )

    print(
        "Carried Over Tasks :",
        summary["carried_over_tasks"]
    )

    print(
        "Unresolved Tasks :",
        summary["unresolved_tasks"]
    )


# ==========================================
# Main Program
# ==========================================

if __name__ == "__main__":

    # Create database table
    create_table()

    # Display all records
    display_records()

    # Display summary
    display_summary()

    # Display deadline information
    display_deadlines()