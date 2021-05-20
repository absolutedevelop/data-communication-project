import pyrebase

config = {
  "apiKey": "AIzaSyAYWh0vRFJlHH0gRpefrvhpgvYUHp5noiI",
  "authDomain": "data-com-4536a.firebaseapp.com",
  "projectId": "data-com-4536a",
  "storageBucket": "data-com-4536a.appspot.com",
  "messagingSenderId": "42603225736",
  "appId": "1:42603225736:web:d3f8c3fce291badafe353d",
  "measurementId": "G-B28QGFWPM6",
  "databaseURL": ""
}

firebase  = pyrebase.initialize_app(config)
storage = firebase.storage()

path_on_cloud = "team1/test.zip"
path_local = "test.zip"

#storage.child(path_on_cloud).put(path_local)

storage.child(path_on_cloud).download("test_on_download.zip")





