import json
# JSON data as a string
student_json = '''
{
    "name": "Sadanand", "age": 24,"skills": ["Python", "SQL"],"active": true
}'''

student = json.loads(student_json)          # JSON → Python

print("Name:", student["name"])
print("Skills:", student["skills"])

student["age"] = 26                          # Update age
student["skills"].append("Git")              # Add a skill

updated_json = json.dumps(student)       # Python → JSON

print("Updated JSON:")
print(updated_json)