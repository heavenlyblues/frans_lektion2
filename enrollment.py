data = {            # data is dictionary with two keys: "studenter" and "kurser"
    "studenter": [  # "studenter" is a list of tuples; each tuple represents a student 
                    # each tuple contains a string (student name) and a dictionary with 3 keys: int, tuple, bool
        ("Alice", {"ålder": 25, "ämnen": ("Matematik", "Fysik"), "aktiv": True}),
        ("Bob", {"ålder": 22, "ämnen": ("Biologi",), "aktiv": False}),
        ("Charlie", {"ålder": 23, "ämnen": ("Matematik", "Biologi"), "aktiv": True}),
        ("Diana", {"ålder": 24, "ämnen": ("Fysik",), "aktiv": False}),
        ("Eve", {"ålder": 21, "ämnen": ("Matematik", "Fysik", "Biologi"), "aktiv": True}),
    ],
    "kurser": {     # "kurser" is a dictionary where each key is a course name and each value is another dictionary
        "Matematik": {"studenter": {"Alice", "Charlie", "Eve"}},   
        "Fysik": {"studenter": {"Alice", "Diana", "Eve"}},        # each course dictionary contains a "studenter" key
        "Biologi": {"studenter": {"Bob", "Charlie", "Eve"}},      # "studenter" holds a set of student names enrolled in the course
    }     
}


# Function creates a tuple of unique names of active students
def get_active_students(data):
    return tuple(
    name for name, info in data["studenter"] if info["aktiv"] 
)

# Creates a set of unique subjects currently active students are studying
def get_unique_subjects(data):
    return {
        subject
        for name, info in data["studenter"]
        if info["aktiv"]
        for subject in info["ämnen"]
    }

# Create a dict with course key and a value of number of student actively enrolled
def get_active_enrollment(data):
    return {
        subject: sum(
            1 for student in info["studenter"]
            if any(name == student and details ["aktiv"] for name, details in data["studenter"])
        )
        for subject, info in data["kurser"].items()
    }

active_students = get_active_students(data)
unique_subjects = get_unique_subjects(data)
active_enrollment = get_active_enrollment(data)

print(f", ".join(active_students))
print(f", ".join(unique_subjects))
print(", ".join(f"{subject}: {count}" for subject, count in active_enrollment.items()))