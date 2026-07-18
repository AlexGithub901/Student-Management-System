import json

students = {}

def add_student(student_id, name, grade):
    if student_id in students:
        return False
    students[student_id] = {'name': name, 'grade': grade}
    return True

def remove_student(student_id):
    if student_id in students:
        del students[student_id]
        return True
    return False

def search_student(query):
    results = []
    query_lower = query.lower()
    for sid, info in students.items():
        if query_lower in sid.lower() or query_lower in info['name'].lower():
            results.append({'id': sid, 'name': info['name'], 'grade': info['grade']})
    return results

def update_student(student_id, name=None, grade=None):
    if student_id not in students:
        return False
    if name is not None:
        students[student_id]['name'] = name
    if grade is not None:
        students[student_id]['grade'] = grade
    return True

def export_students(format='csv'):
    if format == 'json':
        return json.dumps(students, indent=2)
    
    lines = ["ID,Name,Grade"]
    for sid, info in students.items():
        lines.append(f"{sid},{info['name']},{info['grade']}")
    return "\n".join(lines)

def export_students_csv():
    return export_students(format='csv')

def export_students_json():
    return export_students(format='json')
