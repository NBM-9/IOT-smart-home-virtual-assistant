devices = {
    "light": False,
    "fan": False,
    "door": "unlocked",
    "ac": False
}

def assistant(command):
    command = command.lower()
    if "turn on" in command:
        if "light" in command:
            devices["light"] = True
            return "Light turned on."
        elif "fan" in command:
            devices["fan"] = True
            return "Fan turned on."
        elif "ac" in command:
            devices["ac"] = True
            return "AC turned on."
    elif "turn off" in command:
        if "light" in command:
            devices["light"] = False
            return "Light turned off."
        elif "fan" in command:
            devices["fan"] = False
            return "Fan turned off."
        elif "ac" in command:
            devices["ac"] = False
            return "AC turned off."
    elif "lock" in command:
        devices["door"] = "locked"
        return "Door locked."
    elif "unlock" in command:
        devices["door"] = "unlocked"
        return "Door unlocked."
    else:
        return "Sorry, I didn't understand that command."

# Sample simulation
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = assistant(user_input)
    print("Assistant:", response)
