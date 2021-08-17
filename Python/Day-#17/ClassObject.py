# PascalCase - 1st letter of every word is capital
# camelCase - first letter is smaller and then it's pascalcase 
# snake_case - "_" between the words
class User:
    # Constructor - what happens when we construct an objects
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name =  user_name
        self.following = 0
        self.followers = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# variable attached to the class is called attribute
# user_1 = User()
# user_1.id = "001"
# user_1.username = "NandishaKrishna"
user_1 = User(1, "Nandisha")
user_2 = User(2, "RoyNuz")
# print(user_1) # <__main__.User object at 0x00B573E8>
print(f"UserID: {user_1.user_id} UserName: {user_1.user_name}")
print(f"UserID: {user_2.user_id} UserName: {user_2.user_name}")
user_1.follow(user_2)
print(f"UserName: {user_1.user_name:10} Followers: {user_1.followers} Following: {user_1.followers}") # BUG 
print(f"UserName: {user_2.user_name:10} Followers: {user_2.followers} Following: {user_2.followers}")