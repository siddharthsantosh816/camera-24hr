import cv2
import dropbox
import time

startTime=time.time()
count=1
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
            
def snapshot():
    global count
    videoObject=cv2.VideoCapture(0)
    result=True

    while(result):
        reb,frame=videoObject.read()
        name='Image'+str(count)+'.jpg'
        cv2.imwrite(name,frame)
        count=count+1
        result=False

    videoObject.release()
    cv2.destroyAllWindows()
    return name



def main():
    access_token = 'sl.BFy43S3nuwIZCxhb6wPnhvgEEGbe8_hfkJKsUndkh6z4_lIXApE_TGbgbHZEF0qFLIwaM_RHD2gDbuPyt-Gc2ZW5dl1J3oHSSZVplu8BIOlYfmerc5wBkvmbxj-gm1ZH1d-04WKx'
    transferData = TransferData(access_token)
    name=snapshot()
    file_from = 'C:/Users/w/Desktop/Python/Basics'+'/'+name
    file_to = '/screenshot/'+name  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)


while(True):
    if(time.time()-startTime>=86400):
        main()
        startTime=time.time()

