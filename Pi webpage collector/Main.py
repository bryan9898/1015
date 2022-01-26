from flask import Flask ,session, render_template, request, redirect, Response , jsonify , url_for , g , send_file

import random,json
import sys
#import MySQLdb
import pymysql
import pyshark
import os
import signal
import subprocess
from subprocess import Popen, PIPE

import hashlib
#import dpkt
#, pcap
import time
from flask_login import LoginManager
from flask_login import UserMixin , current_user, login_user

app=Flask(__name__ , static_folder='static', static_url_path='/static')
app.secret_key = os.urandom(24)
db=pymysql.connect(host='34.124.188.111',user='root',password='70nz8wpFxdDJ5ty0',database='Loghub', autocommit=True)
computerState = 0
networkState = 0
out_string = ""
i = 1




@app.route('/')
def loginPage():
    
    return render_template('mainPage.html')

@app.route('/return-files/')
def return_files_tut():
	try:
		return send_file('/home/pi/Desktop/Project/Logs/logs.pcap', as_attachment=True,attachment_filename='logs.pcap')
	except Exception as e:
		return str(e)
	    
@app.route('/return-text/')
def return_txt():
	try:
		return send_file('/home/pi/Desktop/Project/Logs/logs.txt', as_attachment=True,attachment_filename='logs.txt')
	except Exception as e:
		return str(e)


@app.route('/home')
def collectLog():
    print("running")
    computerState = 0
    networkState = 0
    
    return render_template('index.html', computerState = 1, networkState = 1 )

    
    #return redirect(url_for('loginPage'))  
     


@app.route('/hostapd' , methods=['GET', 'POST'])
def hostapd():
    print("hostapd Running")
    if request.method == 'POST':
        outString2 = ""
        print("hostapd Running Post")
        rf=request.get_json()
        userName = rf['userName']
        password = rf['password']
        print(userName)
        print(password)
        #os.system("sudo systemctl stop hostapd")
        #import os
        #stopService = os.system("sudo /etc/init.d/hostapd stop")
        #import subprocess
        #stopService = subprocess.call('sudo /etc/init.d/hostapd stop', shell=True)
        time.sleep(2)
        
        out_file = open("../../../../etc/hostapd/hostapd.conf", "w")
        outString2 += "interface=wlan1\nbridge=br0\n#driver=nl80211\nssid="
        outString2 += userName
        outString2 += "\nhw_mode=g\nchannel=7\nwmm_enabled=0\nmacaddr_acl=0\nauth_algs=1\nignore_broadcast_ssid=0\nwpa=2\nwpa_passphrase="
        outString2 += password
        outString2 += "\nwpa_key_mgmt=WPA-PSK\nwpa_pairwise=TKIP\nrsn_pairwise=CCMP"
        out_file.write(outString2)
        print(outString2)
        #time.sleep(5)
        #import subprocess
        #startService = subprocess.call('sudo /etc/init.d/hostapd start', shell=True)
        #startService = os.system("sudo /etc/init.d/hostapd start")
        #import os
        #os.system("sudo /etc/init.d/hostapd start restart")
        #time.sleep(5)
        #stopService2 = subprocess.call('sudo /etc/init.d/hostapd stop', shell=True)
        #time.sleep(20)
        
        #import os
        
        #os.system('sudo shutdown -r -t 30')
        #stopService2 = subprocess.call('sudo sudo shutdown -r +1', shell=True)
        #startService2= subprocess.call('sudo /etc/init.d/hostapd start', shell=True)
    #startService2= 
    return startProcess() #subprocess.Popen(["python", "Shutdown.py"])
        
        #os.system("sudo systemctl start hostapd")
       
def startProcess():
    subprocess.Popen(["python", "/home/pi/Desktop/Project/Shutdown.py"])



@app.route('/login' , methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userName = request.form['userName']
        password = request.form['password']
        session.pop('user', None)
   
        dbPassword = ""  
        hash_object =  hashlib.sha512(password.encode())
        hex_dig = hash_object.hexdigest()
        print(hex_dig)
        print("login Running")
        curs=db.cursor()
        print(userName)
        rows_count = curs.execute("SELECT * FROM userAccount WHERE username= '%s'" % (userName))
        print(rows_count)
        if rows_count > 0:
            for row in curs:
                dbPassword  = row[1]
    
      
      
          
        curs.close()
    
        if(dbPassword == hex_dig):
            print("run redirect")
            session['user'] = request.form['userName'] 
            return redirect(url_for('collectLog'))   
     
    
        return redirect(url_for('loginPage'))  





@app.route('/logout' ,methods=['GET', 'POST'])
def logout():
    session.pop('user', None)
    return redirect(url_for('loginPage')) 

if __name__  == '__main__':
	app.run(host='0.0.0.0')


