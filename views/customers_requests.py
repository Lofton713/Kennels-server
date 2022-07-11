CUSTOMERS = [
    [
        {
            "id": 1,
            "name": "Dan Danson"
        },
        {
            "id": 2,
            "name": "Bob Bobson"
        },
        {
            "id": 3,
            "name": "Jill Jillson"
        }
    ]
]

# function to return all locations
def get_all_customers():
    return CUSTOMERS

def get_single_customer():
    # Variable to hold the employee
    requested_customer = None
    
    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer