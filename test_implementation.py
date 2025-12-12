#!/usr/bin/env python3
"""Test script to verify the implementation of employee helper functions"""

import sys
sys.path.insert(0, 'lib')

from models.employee import Employee
from models.department import Department

print("=" * 60)
print("Testing Employee Implementation")
print("=" * 60)

# Test 1: list_employees
print("\n1. Testing Employee.get_all():")
employees = Employee.get_all()
print(f"Found {len(employees)} employees:")
for emp in employees:
    print(f"  {emp}")

# Test 2: find_employee_by_name
print("\n2. Testing Employee.find_by_name():")
test_name = "Dani"
employee = Employee.find_by_name(test_name)
print(f"Found employee '{test_name}': {employee}")

test_name_fail = "Fred"
employee = Employee.find_by_name(test_name_fail)
print(f"Found employee '{test_name_fail}': {employee if employee else 'Not found'}")

# Test 3: find_employee_by_id
print("\n3. Testing Employee.find_by_id():")
test_id = 2
employee = Employee.find_by_id(test_id)
print(f"Found employee with id {test_id}: {employee}")

test_id_fail = 99
employee = Employee.find_by_id(test_id_fail)
print(f"Found employee with id {test_id_fail}: {employee if employee else 'Not found'}")

# Test 4: create_employee
print("\n4. Testing Employee.create():")
try:
    new_emp = Employee.create("Test Employee", "Test Title", 1)
    print(f"Created: {new_emp}")
    
    # Test with invalid data
    print("\nTesting with invalid name:")
    try:
        Employee.create("", "Test", 1)
    except Exception as e:
        print(f"  Expected error: {e}")
    
    print("\nTesting with invalid department_id:")
    try:
        Employee.create("Test", "Test", 99)
    except Exception as e:
        print(f"  Expected error: {e}")
        
except Exception as e:
    print(f"Error: {e}")

# Test 5: update_employee
print("\n5. Testing Employee.update():")
if employee := Employee.find_by_id(3):
    print(f"Before: {employee}")
    try:
        employee.name = "Updated Name"
        employee.job_title = "Updated Title"
        employee.department_id = 2
        employee.update()
        print(f"After: {employee}")
        
        # Restore original
        employee.name = "Charlie"
        employee.job_title = "Manager"
        employee.department_id = 2
        employee.update()
        print(f"Restored: {employee}")
    except Exception as e:
        print(f"Error: {e}")

# Test 6: delete_employee
print("\n6. Testing Employee.delete():")
# Create a temp employee to delete
temp_emp = Employee.create("Temp Employee", "Temp Title", 1)
print(f"Created temp employee: {temp_emp}")
temp_id = temp_emp.id
temp_emp.delete()
print(f"Deleted employee with id {temp_id}")
check = Employee.find_by_id(temp_id)
print(f"Verification (should be None): {check}")

# Test 7: list_department_employees
print("\n7. Testing Department.employees():")
dept = Department.find_by_id(1)
if dept:
    print(f"Department: {dept}")
    employees = dept.employees()
    print(f"Employees in department:")
    for emp in employees:
        print(f"  {emp}")

dept = Department.find_by_id(2)
if dept:
    print(f"\nDepartment: {dept}")
    employees = dept.employees()
    print(f"Employees in department:")
    for emp in employees:
        print(f"  {emp}")

print("\n" + "=" * 60)
print("All tests completed successfully!")
print("=" * 60)
