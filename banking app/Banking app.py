# Function to load user data from a file and return it as a list of dictionaries
def load_data(filename):
    users = []  # List to hold user dictionaries
    with open(filename, 'r') as file:
        for line in file:
            # Split the line by commas into username, password, full_name, balance
            data = line.strip().split(',')
            user = {
                'username': data[0],
                'password': data[1],
                'full_name': data[2],
                'balance': float(data[3])  # Convert balance to a float
            }
            users.append(user)
    return users

# Function to authenticate a user based on username and password
def login(users, username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user  # Return the user dictionary if login is successful
    return None  # Return None if username or password is incorrect

# Function to display user's full name and balance
def display_user_info(user):
    return f"Name: {user['full_name']}\nBalance: {user['balance']}"

# Main function to run the program
def main():
    # Load the data from the file
    users = load_data('data.txt')
    
    # Get username and password from the user
    username = input("Enter Name: ")
    password = input("Enter password: ")
    
    # Try to login
    user = login(users, username, password)
    
    # If user is found, display their information
    if user:
        print(display_user_info(user))
    else:
        print("User name and password not found")

# Call the main function to run the program
if __name__ == "__main__":
    main()
