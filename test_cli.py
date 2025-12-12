#!/usr/bin/env python3
"""
Interactive test of the CLI - demonstrates all employee functions work correctly
"""

import subprocess
import sys

def test_cli_function(option, inputs, description):
    """Test a CLI function with given inputs"""
    print(f"\n{'='*70}")
    print(f"Testing: {description}")
    print(f"{'='*70}")
    
    # Prepare input for the CLI
    all_inputs = [option] + inputs + ["0"]  # Add 0 to exit
    input_string = "\n".join(all_inputs) + "\n"
    
    # Run the CLI
    result = subprocess.run(
        ["/home/linda-jerop/Development/code/se-prep/phase-3/python-p3-v2-cli-orm-lab/.venv/bin/python", "lib/cli.py"],
        input=input_string,
        capture_output=True,
        text=True,
        cwd="/home/linda-jerop/Development/code/se-prep/phase-3/python-p3-v2-cli-orm-lab"
    )
    
    # Display relevant output (skip menu displays)
    lines = result.stdout.split('\n')
    output_started = False
    for line in lines:
        if line.strip().startswith('>') or output_started:
            output_started = True
            if not line.startswith('Please select') and not line.startswith('0.') and not line.startswith('Goodbye'):
                print(line)
    
    return result.returncode == 0

# Reseed database first
print("Reseeding database...")
subprocess.run(
    ["/home/linda-jerop/Development/code/se-prep/phase-3/python-p3-v2-cli-orm-lab/.venv/bin/python", "lib/seed.py"],
    cwd="/home/linda-jerop/Development/code/se-prep/phase-3/python-p3-v2-cli-orm-lab"
)

# Test 7: List all employees
test_cli_function("7", [], "Option 7 - List all employees")

# Test 8: Find employee by name (success)
test_cli_function("8", ["Dani"], "Option 8 - Find employee by name (Dani)")

# Test 8: Find employee by name (failure)
test_cli_function("8", ["Fred"], "Option 8 - Find employee by name (Fred - not found)")

# Test 9: Find employee by id (success)
test_cli_function("9", ["2"], "Option 9 - Find employee by id (2)")

# Test 9: Find employee by id (failure)
test_cli_function("9", ["99"], "Option 9 - Find employee by id (99 - not found)")

# Test 10: Create employee (success)
test_cli_function("10", ["Ira", "Manager", "1", "7"], 
                 "Option 10 - Create employee (Ira) and list to verify")

# Test 10: Create employee (invalid name)
test_cli_function("10", ["", "Programmer", "1"], 
                 "Option 10 - Create employee with empty name (should fail)")

# Test 10: Create employee (invalid department id)
test_cli_function("10", ["Jani", "Accountant", "99"], 
                 "Option 10 - Create employee with invalid department_id (should fail)")

# Test 11: Update employee (success)
test_cli_function("11", ["3", "Charles", "Director", "1", "7"], 
                 "Option 11 - Update employee 3 and list to verify")

# Test 11: Update employee (invalid id)
test_cli_function("11", ["99"], 
                 "Option 11 - Update employee with invalid id (should fail)")

# Test 13: List department employees
test_cli_function("13", ["1"], "Option 13 - List employees in department 1")
test_cli_function("13", ["2"], "Option 13 - List employees in department 2")
test_cli_function("13", ["99"], "Option 13 - List employees in invalid department (should fail)")

# Test 12: Delete employee
test_cli_function("12", ["1", "7"], 
                 "Option 12 - Delete employee 1 and list to verify")

# Test 12: Delete employee (invalid id)
test_cli_function("12", ["99"], 
                 "Option 12 - Delete employee with invalid id (should fail)")

print(f"\n{'='*70}")
print("All CLI tests completed!")
print(f"{'='*70}")

# Reseed database to restore original state
print("\nReseeding database to restore original state...")
subprocess.run(
    ["/home/linda-jerop/Development/code/se-prep/phase-3/python-p3-v2-cli-orm-lab/.venv/bin/python", "lib/seed.py"],
    cwd="/home/linda-jerop/Development/code/se-prep/phase-3/python-p3-v2-cli-orm-lab"
)
print("Database restored!")
