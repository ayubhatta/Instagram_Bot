'''
Comment other commands while using one command.
'''


from instabot import Bot

bot = Bot()
bot.login(username="username", password="password")
bot.follow('username')   # give the username of the user you want to follow
bot.unfollow('username') # give the username of the user you want to unfollow

# give the path of the photo you want to upload and type the caption for the photo
bot.upload_photo("path of the photo", caption="caption of the photo")  


# type what you want to send as the message in place of "message".
bot.send_message("message", ['username1', 'username2']) # give the username of the user you want to send message


followers = bot.get_user_followers("username") # give the username of the user whose followers you want to get
for follower in followers:
    print(bot.get_user_info(follower))
    
    
following = bot.get_user_following("username") # give the username of the user whose following you want to get
for follow in following:
    print(bot.get_user_info(follow))