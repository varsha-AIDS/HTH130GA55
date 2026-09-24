import sys
import os

# Project folder path
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(0, PROJECT_ROOT)

from database.db import (
    create_tables,
    add_meeting,
    add_action_item
)

# Create database tables
create_tables()


# =========================
# Meeting 1
# =========================

meeting1 = add_meeting(
    "Project Planning Meeting",
    "2026-09-22"
)

add_action_item(
    meeting1,
    "Design database",
    "Pooja",
    "2026-09-23",
    "High"
)

add_action_item(
    meeting1,
    "Prepare UI design",
    "Sujitha",
    "2026-09-24",
    "Medium"
)


# =========================
# Meeting 2
# =========================

meeting2 = add_meeting(
    "Progress Review Meeting",
    "2026-09-24"
)

add_action_item(
    meeting2,
    "Design database",
    "Pooja",
    "2026-09-27",
    "High"
)

add_action_item(
    meeting2,
    "Complete AI extraction",
    "Varsha",
    "2026-09-28",
    "High"
)


# =========================
# Output
# =========================

print()
print("Sample data added successfully!")
print("Meeting 1 ID:", meeting1)
print("Meeting 2 ID:", meeting2)