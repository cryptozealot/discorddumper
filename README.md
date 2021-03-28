# DiscordDumper 

discorddumper.py is a Proof Of Concept written in Python3.7 showing how easy it is to connect to a service such as Discord with just a JWT Token and dump all sensitive information for the owner of the JWT token.

# Requirements:
Python3.7

# Usage:

* Clone the repo or copy discorddumper.py or download the release
* Execute with python3.7 and 1 command line paramater {JWT-token}

# Examples:

```
python3.7 discorddumper.py {token}
```
```
python3.7 discorddumper.py 123my123.345special345.678token678
```
or send the output to a file

```
python3.7 discorddumper.py 123my123.345special345.678token678 > log.txt
```

# More information:

* MIT License, Please do not do bad stuff with this.
* Feel free to fork or PR and teach me how to write better python code.
* Discord please don't store the JWTs unencrypted.
* Use at your own risk and with a test user
* To Invalidate user's tokens, we can reset the user's password, we are all safe, no reason to worry :)

# TO DO 
# More functionality
* Guild 
* Invite
* Emoji
* User
* Webhook
# Exceptions 
# Formatting for msges
