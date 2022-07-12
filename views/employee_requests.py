EMPLOYEES = [
        {
            "id": 1,
            "name": "Joe Smith"
        },
        {
            "id": 2,
            "name": "Jane Smith"
        },
        {
            "id": 3,
            "name": "Jack Jackson"
        }
    
]

# function to return all locations
def get_all_employees():
    return EMPLOYEES

def get_single_employee():
    # Variable to hold the employee
    requested_employee = None
    
    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    # Get the id value of the last animal in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    employee["id"] = new_id

    # Add the animal dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee