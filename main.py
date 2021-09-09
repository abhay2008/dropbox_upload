import dropbox

class TransferData:
  def __init__(self, access_token):
    self.access_token = access_token
    
  def upload_file(self, file_from, file_to):
    dbx = dropbox.Dropbox(self.access_token)
    
    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), file_to)
    

def main():
  access_token = 'C0TQsTBkOnMAAAAAAAAAATc0fw5O_GytKpGsgY8WAhEP-T_u4Qa_xDHNIVWEd_A6'
  transferData = TransferData(access_token)
  
  file_from = input("Enter the file path to transfer:-  ")
  file_to = input("enter the full path to upload to dropbox:-  ") # The full path to upload the file to , including the name which will be called once uploaded.
  
  # API v2
  transferData.upload_file(file_from, file_to)
  print("file has been moved!!!")
  
main()