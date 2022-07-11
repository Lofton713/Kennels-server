EMPLOYEES = [
    [
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