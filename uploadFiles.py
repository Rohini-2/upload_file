from os import access
import cv2
import dropbox
import time
import random
starttime=time.time()
def takesnaps():
    videoObject=cv2.VideoCapture(0)
    number=random.randint(0,100)
    result=True
    while(result):
        ret,frame=videoObject.read()
        image_name="img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        starttime=time.time
        result=False
    return image_name
    print("phototaken")    
    videoObject.release()
    cv2.destroyAllWindows()
def uploadfile(image_name):
    files=image_name
    accessTken="35r6VdDyMtgAAAAAAAAAARHPT50ex5fTL1FjZZlWyMaBuvqVruxmxPp4b5yYSM7y"
    destination="/uploadFiles/"+image_name
    db=dropbox.Dropbox(accessTken)
    with open(files,"rb")as f:
        db.files_upload(f.read(),destination,mode=dropbox.files.WriteMode.overwrite)
def main():
    while(True):
        if(time.time()-starttime>=5):
            name=takesnaps()
            uploadfile(name)
main()            