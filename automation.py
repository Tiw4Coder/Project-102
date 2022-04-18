import os
import shutil
import time
import dropbox


def main():

    uploaded_folders_count = 0
    uploaded_files_count = 0

    path = input("/PATH_TO_UPLOAD")

    days = 30

    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):
        
        for root_folder,folders,files in os.walk(path):

            if seconds >= get_file_or_folder_age(root_folder):
                upload_file(root_folder)
                uploaded_folders_count += 1

                break 

            else:

                for folder in folders:

                    folder_path = os.path.jion(root_folder,folder)

                    if seconds >= get_file_or_folder_age(folder_path):

                        upload_file(folder_path)
                        uploaded_folders_count += 1

                for file in files:
                    
                    file_path = os.path.jion(root_folder,file)

                    if seconds >= get_file_or_folder_age(file_path):

                        upload_file(file_path)
                        uploaded_files_count += 1

        else:

            if seconds >= get_file_or_folder_age(path):
                upload_file(path)
                uploaded_files_count += 1


    else:

        print(f'"{path}" is not found')
        uploaded_files_count += 1


    print(f"Total folders deleted:{uploaded_folders_count}")
    print(f"Total files deleted:{uploaded_files_count}")

def upload_file(path): 
    access_token = "riWLfXRAxhMAAAAAAAAAAc80Zo1srkFRq8TjLv4rZcUbV53JYUVvUoiM093jl-G4" 
    file = path 
    file_from = file 
    file_to="/newFolder/"+(path) 
    dbx = dropbox.Dropbox(access_token) 

    with open(file_from, 'rb') as f: 
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite) 
        print("file uploaded")

def get_file_or_folder_age(path):

    ctime = os.stat(path).st_ctime

    return ctime

if __name__ == '__main__':
    main()