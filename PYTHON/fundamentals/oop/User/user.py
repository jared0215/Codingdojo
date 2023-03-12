# Creating User Class

class User():
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    # Methods
    def display_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Your Email:", self.email)
        print("Age:", self.age)
        print("Member Status", self.is_rewards_member)
        print("Gold Card Points:", self.gold_card_points)
        print("\n")

    def enroll(self):
        if self.is_rewards_member == True:
            print("You already a member", self.first_name, self.last_name)
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200

    def spend_points(self, amount):
        if amount <= 0:        # Checks if the amount inputted is negative
            print('Please enter a valid amount, ' + self.first_name + '.')
            return
        if self.gold_card_points < amount:        # Checks if the amount is enough to spend
            print('Sorry ' + self.first_name + ",",
                  'you do not have enough points to redeem this reward. :(')
        else:
            self.gold_card_points -= amount        # Decreases specified amount of points
            print('Thank you for redeeming your points ' +
                  self.first_name + "!", 'Enjoy your Reward! :)')
        print("\n")


user_jared = User('Jared', 'Campos', 'jared0215@hotmail.com', '24')
user_jared.enroll()
user_jared.spend_points(100)
user_jared.display_info()

user_paul = User('Paul', 'Giampiccolo', 'yankeekid413@yahoo.com', '32')
user_paul.enroll()
user_paul.spend_points(300)
user_paul.display_info()

user_nathan = User('Nathan', 'Mirkov', 'nathmirk@gmail.com', '27')
user_nathan.enroll()
user_nathan.spend_points(40)
user_nathan.display_info()

user_tom = User('Thomas', 'Koerkel', 'tkoerkel3@gmail.com', '84')
user_tom.enroll()
user_tom.spend_points(-300)
user_tom.display_info()

user_james = User('James', 'Fiorillo', 'JapeFiorillo4@gmail.com', '25')
user_james.enroll()
user_james.spend_points(0)
user_james.display_info()


user_jared.enroll()
user_nathan.enroll()
user_paul.enroll()
user_james.enroll()
user_tom.enroll()
