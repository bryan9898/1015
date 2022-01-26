"use strict";

const functions = require("firebase-functions").region("asia-southeast1");

const admin = require("firebase-admin");

const firebaseConfig = {
  apiKey: "AIzaSyDOrevelnl1E7SOE29ZH4DWsZGqAm386TA",
  authDomain: "aesthetic-frame-338708.firebaseapp.com",
  databaseURL: "https://aesthetic-frame-338708-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "aesthetic-frame-338708",
  storageBucket: "aesthetic-frame-338708.appspot.com",
  messagingSenderId: "63138128578",
  appId: "1:63138128578:web:45ec29462111bd1c93515b",
  measurementId: "G-3LCM63ZEMK"
};

const app = admin.initializeApp(firebaseConfig);

const db = admin.firestore();
const cors = require("cors");
const { user } = require("firebase-functions/v1/auth");

//all users
exports.users = functions.https.onRequest(async (req, resp)=>{
  cors()(req, resp, () => {
    db.collection("users").get()
        .then(function(querySnapshot) {
          querySnapshot.forEach(function(doc) {
          console.log(doc.id, " => ", doc.data());
          resp.send(doc.id + " => " + doc.data());
          });
        });
  });
});

//get Indiviual 
//https://asia-southeast1-aesthetic-frame-338708.cloudfunctions.net/getUser
exports.getUser = functions.https.onRequest(async (req, resp)=>{
  var key = req.body['key'];
  var user = req.body['user'];
  if(key == "c97bf909e33a824add3f88ff89b57e319e200993f0d1134f7f9c0bd677755247"){
    var a = await db.collection("users").doc(user).get();
    if (!a.exists) {
      resp.send("No such Username!!!");
    } else {
      resp.send("Password for " + user + " is : " + a.data().password);
    }
  } else {
    resp.send("Wrong key!!!");
  }
});

//add user
//https://asia-southeast1-aesthetic-frame-338708.cloudfunctions.net/addUser
exports.addUser = functions.https.onRequest(async (req, resp) => {
  var key = req.body['key'];
  var user = req.body['user'];
  var password1 = req.body['pass'];
  
  if(key == "c97bf909e33a824add3f88ff89b57e319e200993f0d1134f7f9c0bd677755247"){
    var check = await db.collection("users").doc(user).get();
    if (check.exists) {
      resp.send("user EXIST ALRDY !!");
      return;
    }
    var a = await db.collection("users").doc(user).set({password:password1});
    resp.send("User : " + user + " has been added!");
  } else {
    resp.send("Wrong key!!!");
  }
});

//update user
//https://asia-southeast1-aesthetic-frame-338708.cloudfunctions.net/updatePass
exports.updatePass = functions.https.onRequest(async (req, resp) => {

  var key = req.body['key'];
  var user = req.body['user'];
  var oldPassword = req.body['oldPass'];
  var newPassword = req.body['newPass'];
  
  if(key == "c97bf909e33a824add3f88ff89b57e319e200993f0d1134f7f9c0bd677755247"){
    var a = await db.collection("users").doc(user).get();
    if (newPassword == a.data().password || oldPassword != a.data().password ){
      resp.send("same Password or Wrong Old Password!");
      return;
    }
    var check = await db.collection("users").doc(user).update({
      "password": newPassword
    });
    resp.send("user : " + user + "'s password has been updated!");
  } else {
    resp.send("Wrong key!!!");
  }
  
});

//delete User
exports.delUser = functions.https.onRequest(async (req, resp) => {
  var key = req.body['key'];
  var user = req.body['user'];
  
  if(key == "c97bf909e33a824add3f88ff89b57e319e200993f0d1134f7f9c0bd677755247"){
    var check = db.collection("users").doc(user).delete();
    resp.send("user : " + user + " has been deleted!");
  } else {
    resp.send("Wrong key!!!");
  }
});

