import requests
import hashlib

key = "8596348A"
pw_hash = hashlib.sha256(key.encode()).hexdigest()
username = "hello"
dadw
#Update Pass
def updatePass():

    oldPass = "54364"
    oldHash =  hashlib.sha256(oldPass.encode()).hexdigest()
    newPass = "543631234"
    newHash =  hashlib.sha256(newPass.encode()).hexdigest()

    url = 'https://asia-southeast1-aesthetic-frame-338708.cloudfunctions.net/updatePass'
    myobj = {'key':pw_hash,'user': username,'oldPass': oldHash , 'newPass' : newHash}
    x = requests.post(url, data = myobj)
    print(x.text)
dwadw
#get user
def getUser():
    url = 'https://asia-southeast1-aesthetic-frame-338708.cloudfunctions.net/getUser'
    myobj = {'key':pw_hash,'user': username}
    x = requests.post(url, data = myobj)
    print(x.text)

#add new user
def addUser():
    password1 = "12345"
    passHash =  hashlib.sha256(password1.encode()).hexdigest()
    url = 'https://asia-southeast1-aesthetic-frame-338708.cloudfunctions.net/addUser'
    myobj = {'key':pw_hash,'user': username,'pass' : passHash}
    x = requests.post(url, data = myobj)
    print(x.text)

#delete user
def deleteUser():
    url = 'https://asia-southeast1-aesthetic-frame-338708.cloudfunctions.net/delUser'
    myobj = {'key':pw_hash,'user': username}
    x = requests.post(url, data = myobj)
    print(x.text)

def main():
    addUser()
    #updatePass()
    #getUser()
    #deleteUser()




if __name__ == "__main__":
    main()