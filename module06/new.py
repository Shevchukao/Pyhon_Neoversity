import sys


def connect(serv):
    pass


args = tuple(sys.argv)
print(args)
# python module06\new.py --name main --user admin -l -a
user = None
passwd = None
server = "localhost"
for i in range(len(args)):
    if args[i] == "--user":
        user = args[i + 1]
    if args[i] == "--password":
        passwd = args[i + 1]
    if args[i] == "--server":
        server = args[i + 1]
connect(server)
print(f"Logged in user {user} with password {passwd}, server {server}")

# python module06\new.py --user admin --password god
# Result: Logged in user admin with password god
