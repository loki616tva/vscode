# Vacuum Cleaner Reflex Agent

def vaccum_agent(location, status):
    if status == 'Dirty':
        return 'Suck'
    elif location == 'A':
        return 'Right'
    elif location == 'B':
        return 'Down'
    elif location == 'C':
        return 'Up'
    elif location == 'D':
        return 'Left'


# Environment
environment = {
    'A': 'Dirty',
    'B': 'Dirty',
    'C': 'Dirty',
    'D': 'Dirty'
}

location = 'A'

print("Initial environment:", environment)

for i in range(8):
    action = vaccum_agent(location, environment[location])

    if action == 'Suck':
        environment[location] = 'Clean'
    elif action == 'Down':
        location = 'D'
    elif action == 'Up':
        location = 'A'
    elif action == 'Right':
        location = 'B'
    elif action == 'Left':
        location = 'C'

    print(f"Location {location} : {environment[location]}")

print("Updated environment:", environment) 


# # Simple Reflex Agent for Vacuum Cleaner

# def vacuum_agent(location, status):
#     if status == "Dirty":
#         return "Suck"
#     elif location == "A":
#         return "Move Right"
#     else:
#         return "Move Left"


# # Environment
# location = "A"
# A = "Dirty"
# B = "Dirty"

# for i in range(4):
#     status = A if location == "A" else B
#     action = vacuum_agent(location, status)
#     print("Location:", location, "| Status:", status, "| Action:", action)

#     if action == "Suck":
#         if location == "A":
#             A = "Clean"
#         else:
#             B = "Clean"
#     elif action == "Move Right":
#         location = "B"
#     elif action == "Move Left":
#         location = "A"


