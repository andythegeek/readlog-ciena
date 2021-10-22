import json
import collections

#reading file and returning as list of dictionaries
def readFile(filepath):
    f = open(filepath, "r")
    data = json.load(f)
    return data

#with a list of dictionaries as argument, finding unique users and returning as list
def getUsers(data):
    users_unique_counts = collections.Counter(e['who'] for e in data)
    userlist = [str(val) for val in users_unique_counts] 
    return userlist

#with username and list of dictionaries as arguments, returning user log specific to user as list of dictionaries 
def getUserlog(username,data):
    userlist = getUsers(data)
    userloglist = []
    for c in data:
        if c['who'] == username:
            userloglist.append(c)   
        else:
            continue
    return userloglist

#with username and user log as arguments, finding unique actions and their frequencies for user and writing to file
def whatUserDid(user,userlog):
    what_unique_counts = collections.Counter(e['what'] for e in userlog)
    print("\n")
    for val in what_unique_counts:
        print(user + ' performed a ' + val, what_unique_counts[val], 'times')
    
    dict_what = dict(what_unique_counts)
    with open("UserActionReport.txt",'w') as f:
        for key, value in dict_what.items():
            f.write('%s:%s\n' % (key, value))

    print("\n")
    print("View report in UserActionReport.txt")
    print("\n")

#with username and user log as arguments, finding unique locations and their frequencies and writing to file
def userLocations(user,userlog):
    where_unique_counts = collections.Counter(e['where'] for e in userlog)
    print("\n")
    for val in where_unique_counts:
        print(user + ' performed actions at ' + val, where_unique_counts[val], 'times')

    dict_where = dict(where_unique_counts)
    with open("UserLocationReport.txt",'w') as f:
        for key, value in dict_where.items():
            f.write('%s:%s\n' % (key, value))

    print("\n")
    print("View report in UserLocationReport.txt")
    print("\n")


def main():
    file = input('Enter log file path:')   

    data = readFile(file)
    userlist = getUsers(data)

    print('The users found in the log file are:')
    for users in userlist:
        print(users)

    user = input("Enter a username to view user actions and frequency of actions:")
    userlog = getUserlog(user,data)
    whatUserDid(user,userlog)
    

    userlocation = input("Enter username to view locations where user actions were performed:")
    location = userLocations(userlocation,userlog)


if __name__ == "__main__":
    main()






        









