#!/usr/bin/python3.7
#
# MIT License, use at your own risk, don't do bad stuff please.
#
# DiscordDumper 0.4.0 - This is a crude Python API Wrapper for Discord, that dumps user information from JWT token as command line argument.
# Current functionality - writes to variables and displays: User Info, Friends, Servers, Message Contents
#
# I know this is unoptimized and crude code, and could probably be written in less than 10 lines.
# Feel free to fork and PR.
#
# Requirements: python3.7
#
# Usage: python3.7 discorddumper.py {token}
# Usage: python3.7 discorddumper.py 123testuser123.jwt456.token78987 > log.txt
#
# https://requests.readthedocs.io/en/latest/user/advanced/
# https://docs.python.org/3/library/json.html
# https://discord.com/developers/docs/reference

import json
import requests
import time
import sys
from pprint import pprint


# The User class definition for the JWT owner, keep it tidy, add more if needed and use that class
class User:
    def __init__(self, userInfo, guilds, relationships, channels):
        self.userInfo = userInfo
        self.guilds = guilds
        self.relationships = relationships
        self.channels = channels


# Make 4 GET Requests and Instantiate a global variable "currentUser", we are using this variable in other functions, such as get_all_messages()
def create_user_class():
    try:
        global currentUser
        print(" --- Pulling User object...")
        currentUser = User(get_endpoint("users/@me"), get_endpoint("users/@me/guilds"), get_endpoint("users/@me/relationships"), get_endpoint("users/@me/channels"))

    except:
        print("Exception in create_user_array function")


# API Request Function Definitions - GET Request
def get_endpoint(endpoint=None):
    try:
        head = {'Content-Type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Authorization': token}
        url = f'https://discordapp.com/api/v6/{endpoint}'
        r = requests.get(url=url, headers=head)
        return r.json()
    except:
        print("Exception in get_endpoint(endpoint)")
        print(r.status_code)
        print(r.headers)
        print(r.encoding)
        print(r.text)
        print(url)
        pass


# API Request Function Definitions - PATCH Request
def patch(guildid=None, userid=None, object=None):
    try:
        head = {'Content-Type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Authorization': token}
        url = f'https://discordapp.com/api/v6/guilds/{guildid}/members/{userid}'
        print(" --- Sending PATCH Request...")
        r = requests.patch(url=url, data=json.dumps(object), headers=head)
        print(r) # One-liner print
        print("success, check if response code is 204")
    except:
        print("Exception in patch function")
        print(r.status_code)
        print(r.headers)
        print(r.encoding)
        print(r.text)
        print(url)
        pass


# API Request Function Definitions - POST Request
def post(endpoint=None, data_object=None):
    try:
        head = {'Content-Type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Authorization': token}
        url = f'https://discordapp.com/api/v6/{endpoint}'
        print(" --- Sending POST Request...")
        r = requests.post(url=url, data=data_object, headers=head)
        response=(r.json())
        #print(json.dumps(response, sort_keys=True, indent=4)) # Beauty Print
        print(response) # One-liner print
    except:
        print("Exception in post function")
        print(r.status_code)
        print(r.headers)
        print(r.encoding)
        print(r.text)
        print(url)
        pass


# API Request Function Definitions - PUT Request
def put(endpoint=None, roles_object=None): #NOT TESTED
    try:
        head = {'Content-Type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Authorization': token}
        url = f'https://discordapp.com/api/v6/{endpoint}'
        print(" --- Sending PUT Request...")
        r = requests.put(url=url, data=roles_object, headers=head)
        response=(r.json())
        #print(json.dumps(response, sort_keys=True, indent=4)) # Beauty Print
        print(response) # One-liner print
    except:
        print("Exception in put function")
        print(r.status_code)
        print(r.headers)
        print(r.encoding)
        print(r.text)
        print(url)
        pass


# Print User objects single line
def print_user_class():
    try:
        print(" --- User ---")
        print("currentUser.userInfo")
        print(type(currentUser.userInfo))
        print(currentUser.userInfo)
        print('\n')

        print("currentUser.guilds")
        print(type(currentUser.guilds))
        print(currentUser.guilds)
        print('\n')

        print("currentUser.relationships")
        print(type(currentUser.relationships))
        print(currentUser.relationships)
        print('\n')

        print("currentUser.channels")
        print(type(currentUser.channels))
        print(currentUser.channels)
        print(" --- End of User ---")
        print('\n')
    except:
        print("Exception in print_user_array")


# Print Guilds, formatted
def print_guilds():
    try:
        print(" --- Guilds / Servers:")
        for guild in currentUser.guilds:
            print(guild['id'] + " - " + guild['name'])
        print('\n')
    except:
        print("Exception in print_guilds()")


# Print Relationships, formatted
def print_relationships():
    try:
        print(" --- Relationships / Friends:")
        for relationship in currentUser.relationships:
            print(relationship['id'] + " - " + str(relationship['user']))
        print('\n')
    except:
        print("Exception in print_relationships()")


# Print Channels, formatted
def print_channels():
    try:
        print(" --- Channels / Private Messages / Conversations:")
        for channel in currentUser.channels:
            print(channel['id'] + " - " + str(channel['recipients']))
        print('\n')

    except:
        print("Exception in print_channels()")


# here we store all message objects, use that if you need to do some other stuff with messages
messages=[]


# Get all messages for all known channels, there are some debugging lines still left
def get_all_messages():
    try:
        global messages
        print(" --- Getting all messages...")
        for channel in currentUser.channels:
            messages.append(get_endpoint(f"channels/{channel['id']}/messages"))
            #print(channel)
        for conversation in messages:
            print('\n')
            print(conversation[0]['channel_id'])
            #print(conversation)
            for msglog in conversation:
                #print(msglog['timestamp'])
                print(str(msglog['author']['username']) + " - " + str(msglog['content']))
                #print(msglog['author']['username'])
    except:
        print("Exception in get_all_messages()")


# Spam a msg to all friends - OFF by default
def spam_all_channels(content, delayinseconds):
    try:
        print(" --- Spamming All Friends in progress...")
        for channel in currentUser.channels:
            post(f"channels/{channel['id']}/messages", content) #channel['id']
            time.sleep(delayinseconds)
        print("Complete")
    except:
        print("Exception in spam_all_channels()")


# main function - here we exec all functions from above, keep it tidy, comment and uncomment as needed
def main():
    try:
        # Create the User Class for the user who is owner of the token, this sends 4 API requests
        create_user_class()
        # Print the current user class
        print_user_class()

        print(" ------ Main Information:")
        print('\n')
        print_guilds()
        print_relationships()
        print_channels()
        get_all_messages()

        # Spam function - spams all friends with "test" and 10 sec delay - OFF by default
        #spam_all_channels('{"content": "test"}', 10)

        # uncomment below to dump vars
        #pprint(globals())
        #pprint(locals())
    except:
        print("exception in main()")


# Set token as first command line argument and exec main function
token = sys.argv[1]
main()


# STATIC EXAMPLES, just for manual testing, ids are obfuscated:

# GET - use inside print() function
#
#print(get_endpoint("guilds/11111111111111111/roles"))
#print(get_endpoint("channels/22222222222222222/messages"))
#print(get_endpoint("guilds/11111111111111111/members/22222222222222222"))


# POST
#
# send msg to group
#post("channels/11111111111111111/messages",'{"content": "Buy Bitcoin!"}')


# PATCH
#
# PATCH Request Example - Set Roles of (guildid, userid, Data) -
#patch("11111111111111111","22222222222222222",{'roles': ["11111111111111111", "22222222222222222", "12111111111111121", "11111111121111111"]})
#patch("11111111111111111","22222222222222222",{'roles': ["11111111111111111"]})


# PUT
#
# TO DO
