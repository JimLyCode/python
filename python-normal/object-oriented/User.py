class User:
    userCount = 0

    def __init__(self, userName, sex):
        self.userName = userName
        self.sex = sex
        User.userCount += 1

    def showCount(self):
        print("Total user %d" %User.userCount)

    def showUser(self):
        print("userName:", self.userName, ", sex:", self.sex)


user = User("answer", 21)
user.showCount()
user.showUser()