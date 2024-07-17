from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authenticate
google_auth = GoogleAuth()
google_auth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication
drive_app = GoogleDrive(google_auth)

# Make sure files are in your root directory
upload_list = ['test.png', 'test.jpg']

# Replace 'FOLDER_ID_FROM_GOOGLE_DRIVE' with your actual folder ID
folder_id = '1qrUCegGQzCMf1ineV322Ovm_ls9vI__p'

for file_to_upload in upload_list:
    # Create GoogleDriveFile instance with metadata
    file = drive_app.CreateFile({
        'parents': [{'id': folder_id}]
    })

    # Set content of the file
    file.SetContentFile(file_to_upload)

    # Set the title of the file on Google Drive to match the local filename
    file['title'] = file_to_upload

    # Upload the file
    file.Upload()

    print(f"Uploaded {file_to_upload}")

print("All files uploaded successfully")