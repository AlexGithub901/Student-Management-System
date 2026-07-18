import pytest
import json
from student import add_student, remove_student, search_student, update_student, students, export_students, export_students_csv, export_students_json

@pytest.fixture(autouse=True)
def reset_students():
    students.clear()
    students['101'] = {'name': 'Alice', 'grade': 'A'}
    students['102'] = {'name': 'Bob', 'grade': 'B'}

def test_add_student_new():
    assert add_student('103', 'Charlie', 'C') == True
    assert students['103'] == {'name': 'Charlie', 'grade': 'C'}

def test_add_student_duplicate():
    assert add_student('101', 'Alice2', 'A+') == False
    assert students['101']['name'] == 'Alice'

def test_remove_student_existing():
    assert remove_student('101') == True
    assert '101' not in students

def test_remove_student_not_found():
    assert remove_student('999') == False

def test_search_by_id_exact():
    results = search_student('101')
    assert len(results) == 1
    assert results[0]['id'] == '101'
    assert results[0]['name'] == 'Alice'

def test_search_by_name_partial():
    results = search_student('ali')
    assert len(results) == 1
    assert results[0]['id'] == '101'

def test_search_case_insensitive():
    results = search_student('ALICE')
    assert len(results) == 1

def test_search_no_match():
    results = search_student('xyz')
    assert len(results) == 0

def test_update_student_name():
    assert update_student('101', name='Alicia') == True
    assert students['101']['name'] == 'Alicia'

def test_update_student_grade():
    assert update_student('102', grade='A') == True
    assert students['102']['grade'] == 'A'

def test_update_student_not_found():
    assert update_student('999', name='John') == False

def test_update_student_multiple_fields():
    assert update_student('101', name='Alice Updated', grade='A+') == True
    assert students['101']['name'] == 'Alice Updated'
    assert students['101']['grade'] == 'A+'

def test_export_students_csv():
    result = export_students()
    assert "ID,Name,Grade" in result
    assert "101,Alice,A" in result
    assert "102,Bob,B" in result

def test_export_students_csv_format():
    result = export_students(format='csv')
    assert "ID,Name,Grade" in result
    assert "101,Alice,A" in result
    assert "102,Bob,B" in result

def test_export_students_json():
    result = export_students(format='json')
    data = json.loads(result)
    assert '101' in data
    assert data['101']['name'] == 'Alice'
    assert data['101']['grade'] == 'A'
    assert data['102']['name'] == 'Bob'
    assert data['102']['grade'] == 'B'

def test_export_students_csv_helper():
    result = export_students_csv()
    assert "ID,Name,Grade" in result

def test_export_students_json_helper():
    result = export_students_json()
    data = json.loads(result)
    assert '101' in data
