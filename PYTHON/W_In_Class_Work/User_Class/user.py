class User:
    def __init__(self, fname, lname, email, password):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password

    def display_user_info(self):
        print("--- Here is your user info ---")
        print(f"First Name: {self.fname}")
        print(f"Last Name: {self.lname}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        return self


user1 = User("John", "Doe", "ychag@example.com", "123")
user2 = User("Jane", "Snow", "lolok@example.com", "123")
user3 = User("Fred", "Joe", "joe@example.com", "123")
user4 = User("Bob", "Crow", "crow@example.com", "123")

user1.display_user_info()
