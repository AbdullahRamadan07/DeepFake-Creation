import pyrebase
from RadioButtonScreen import *
import time


return_flag = False
def flag():
  from UploadScreen import add,delete
  if add == True:
     return_flag = True
  else:
     return_flag = False

    
config = {
    "apiKey":[
        {
          "current_key": "AIzaSyAzO03-Mt8Bzy9t4CQVSKsHYCVPVJmLNY8"
        }
      ],
    "authDomain": "interactive-statues-gp.firebaseapp.com",
    "project_id": "interactive-statues-gp",
    "mobilesdk_app_id": "1:937337869004:android:e0054ff3a3aa51999ca869",
    "databaseURL": "https://console.firebase.google.com/u/6/project/interactive-statues-gp/storage/interactive-statues-gp.appspot.com/files/~2FGP_Videos",
    "storageBucket": "interactive-statues-gp.appspot.com",
    "messagingSenderId": "937337869004"
}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

local = "final output.mp4"
new_video_name = data.get()
folder=""
folder = foldername
basecloud = "GP_Videos/"
cloud = ""
if new_video_name.find(".mp4"):
    cloud = basecloud+folder+"/"+new_video_name
else:
    new_video_name = new_video_name+".mp4"
    cloud = basecloud+folder+"/"+new_video_name    

print("choice "+folder,"videoname "+new_video_name,"cloud "+cloud)

# storage.child(cloud).put(local)
# print("added")

if (return_flag == True):
    storage.child(cloud).put(local)
    print("added")
    time.sleep(10)
    subprocess.call(["python", "UploadScreen.py"])
elif (return_flag == False):
    # URL = storage.child(cloud).get_url(None)
    storage.delete(cloud,None)
    print("deleted")
    subprocess.call(["python", "UploadScreen.py"])

# time.sleep(7)
# storage.delete(cloud,None)
# print("deleted")

