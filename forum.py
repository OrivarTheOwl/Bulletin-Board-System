logged_in = False
users = {}
current_user = ""
all_posts = []


# Function to initialize test user and their posts
def initialize_test_user(users, all_posts):
    current_user = "abc"
    logged_in = True

    # Ensure a clean slate for posts
    users[current_user] = {"password": "123", "posts": []}

    # Populate posts using the function's expected format
    for post_content in ["msg1", "msg2", "msg3", "msg4", "msg5", "msg6", "msg7", "msg8", "msg9", "msg10", "msg11", "msg12"]:
        users[current_user]["posts"].append(f"{current_user}: {post_content}")
        all_posts.append(f"{current_user}: {post_content}")

    return current_user, logged_in, users, all_posts

# Uncomment the line below to initialize the test user when needed
current_user, logged_in, users, all_posts = initialize_test_user(users, all_posts)


# Creates a user account
def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    if username == "" or password == "":
        print()
        print("Fields cannot be left blank")
    elif username not in users:
        users[username] = {"password": password, "posts": []}
        print()
        print("Account created successfully!")
    elif username in users:
        print()
        print("Username already registered")


# Logs the user in
def login():
    login_username = input("Enter your username: ")
    login_password = input("Enter your password: ")

    if login_username in users and users[login_username]["password"] == login_password:
        print()
        print(f"Successfully logged in as {login_username}!")
        logged_in = True
        return login_username, logged_in
    else:
        print()
        print("Login details do not match - login unsuccessful")
        logged_in = False
        return "", logged_in
    

# Logs the user out
def logout():
    print("Successfully logged out!")
    logged_in = False
    return "", logged_in


# Allows the user to create a post
def create_post(current_user):
    user_post = input("Type your message here, press Enter to post: ")

    users[current_user]["posts"].append(f"{current_user}: {user_post}")
    all_posts.append(f"{current_user}: {user_post}")

    return all_posts


# Allows users to view 5 of their own posts at a time
def view_user_posts(current_user):
    increment = 0
    user_posts = users[current_user]["posts"]
    while True:

        if increment < 0:
            increment = 0
        elif increment > len(user_posts):
            increment = len(user_posts) - len(user_posts) % 5

        if increment == 0:
            print("[ - - Start of messages - - ]")
            print()
        for post in user_posts[increment:increment+5]:
            print(post)
        if increment == len(user_posts) - len(user_posts) % 5:
            print()
            print("[ - - End of messages - - ]")

        print()
        print("1 - Go back 5 posts")
        print("2 - Go forward 5 posts")
        print("3 - Stop viewing posts")
        print()
        selection_string = (input("Selection: "))
        if selection_string.isdigit():
            selection = int(selection_string)

            print()

            if selection == 1:
                increment -= 5
            elif selection == 2:
                increment += 5
            elif selection == 3:
                break
        else:
            print("Invalid input")
            print()


# Allows users to view 5 of all posts at a time
def view_all_posts(all_posts):
    increment = 0
    while True:

        if increment < 0:
            increment = 0
        elif increment > len(all_posts):
            increment = len(all_posts) - len(all_posts) % 5

        if increment == 0:
            print("[ - - Start of messages - - ]")
            print()

        for post in all_posts[increment:increment+5]:
            print(post)

        if increment == len(all_posts) - len(all_posts) % 5:
            print()
            print("[ - - End of messages - - ]")

        print()
        print("1 - Go back 5 posts")
        print("2 - Go forward 5 posts")
        print("3 - Stop viewing posts")
        print()
        selection_string = (input("Selection: "))
        if selection_string.isdigit():
            selection = int(selection_string)
            
            print()

            if selection == 1:
                increment -= 5
            elif selection == 2:
                increment += 5
            elif selection == 3:
                break

        else:
            print("Invalid input")
            print()


# Deletes a user's selected post
def delete_post(current_user, all_posts):
    increment = 1
    for post in users[current_user]["posts"]:
        plain_string = post[(len(current_user) + 2):]
        print(f"{increment} - {plain_string}")
        increment += 1
    print()
    
    selection_string = (input("Select which number post you would like to be deleted, or press 0 to cancel: "))
    if selection_string.isdigit():
        selection = int(selection_string)
        if selection == 0:
            return
        else:
            post_string = users[current_user]["posts"][selection-1]

        users[current_user]["posts"].pop(selection-1)
        all_posts.remove(post_string)
    else:
        print("Invalid input")
    

# Main function
def main(current_user, logged_in, all_posts):

    while True:

        if logged_in == False:

            print()
            print("[ - - - - - Welcome! - - - - - ]")
            print("1 - Create an account")
            print("2 - Login to an account")
            print("3 - Exit the program")
            print()

            user_input = input("Please select an option: ")
            print()

            if user_input == "1":
                register()

            elif user_input == "2":
                current_user, logged_in = login()

            elif user_input == "3":
                print("Shutting down...")
                break
            else:
                print("Invalid input")
        

        elif logged_in == True:

            print()
            print(f"[ - - - - - Hello, {current_user}! - - - - - ]")
            print("1 - Create a new post")
            print("2 - View your posts")
            print("3 - View all posts")
            print("4 - Delete a post")
            print("5 - Log out")
            print()

            user_input = input("Please select an option: ")
            print()

            if user_input == "1":
                all_posts = create_post(current_user)
            elif user_input == "2":
                view_user_posts(current_user)
            elif user_input == "3":
                view_all_posts(all_posts)
            elif user_input == "4":
                delete_post(current_user, all_posts)
            elif user_input == "5":
                current_user, logged_in = logout()
            else:
                print("Invalid input")

main(current_user, logged_in, all_posts)