# trigger or continously check for any downloads(preffer trigger so we dont waste as many resources)
#maybe seperate file for functions that store files correctly.
import time
import shutil
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    def __init__(self, source_folder, destination_folder):
        self.source_folder = source_folder
        self.destination_folder = destination_folder

    def on_created(self, event):
        if event.is_directory:
            return
        
        file_path = event.src_path
        file_name = os.path.basename(file_path)
        move_download(file_path, self.destination_folder)
        #destination_path = os.path.join(self.destination_folder, file_name)
        
        #shutil.move(file_path, destination_path)
        #print(f"Moved '{file_name}' to '{self.destination_folder}'")

def move_download(file_path, dest_dir):
    sound_ext = ('.mp3','.m4a','.wav','.wma','.aac')
    video_ext = ('.mp4','.avi','.mov','.wmv','.mkv','.flv')
    zip_ext = ('.zip')
    text_ext = ('.txt','.asc','.doc','.docx','.rtf','.msg','.pdf','.wpd','.wps')
    img_ext = ('.svg', '.jpg','.jpeg','.png','.webp','.jfif',)
    #all other extensions will be put in a folder labeled etc/other
    
    #could just get extension from it
    ext = os.path.splitext(file_path)[-1].lower()
    time.sleep(3)
    try:
        if ext in sound_ext: 
            if not os.path.exists(dest_dir+"\\sound-clips"):
                os.makedirs(dest_dir+"\\sound-clips")
            dest_path = os.path.join(dest_dir,"sound-clips")
            shutil.move(file_path, dest_path)
            print(f"Moved '{file_path}' to '{dest_path}'")
        elif ext in video_ext:
            if not os.path.exists(dest_dir+"\\videos"):
                os.makedirs(dest_dir+"\\videos")
            dest_path = os.path.join(dest_dir,"videos")
            shutil.move(file_path, dest_path)
            print(f"Moved '{file_path}' to '{dest_path}'")
            
        elif ext in zip_ext:
            if not os.path.exists(dest_dir+"\\compressed-files"):
                os.makedirs(dest_dir+"\\compressed-files")
            dest_path = os.path.join(dest_dir,"compressed-files")
            shutil.move(file_path, dest_path)
            print(f"Moved '{file_path}' to '{dest_path}'")
            
        elif ext in text_ext:
            if not os.path.exists(dest_dir+"\documents"):
                os.makedirs(dest_dir+"\documents")
            dest_path = os.path.join(dest_dir,"documents")
            shutil.move(file_path, dest_path)
            print(f"Moved '{file_path}' to '{dest_path}'")
            
        elif ext in img_ext:

            if not os.path.exists(dest_dir+"\images"):
                os.makedirs(dest_dir+"\images")
            #dest_path = os.path.join(dest_dir,"\images", os.path.basename(file_path))
            dest_path = os.path.join(dest_dir,"images")
            #print(f"attempting move '{file_path}' to '{dest_path}'")
            shutil.move(file_path, dest_path)
            print(f"Moved '{file_path}' to '{dest_path}'")
            
        else:
            #every other file
            if not os.path.exists(dest_dir+"\\miscellaneous"):
                os.makedirs(dest_dir+"\\miscellaneous")
            dest_path = os.path.join(dest_dir,"miscellaneous")
            shutil.move(file_path, dest_path)
            print(f"Moved '{file_path}' to '{dest_path}'")
            
    except FileNotFoundError as e:
            #in case file is not found or is still downloading
            print(f"FileNotFoundError: {e} \n")

    pass

def sort_downloads(source, dest):
    event_handler = FileHandler(source_folder, destination_folder)
    observer = Observer()
    observer.schedule(event_handler, source_folder, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


    pass


if __name__ == '__main__':
    source_folder = 'E:\Downloads'
    # we want to seperate depending on extension so dest folder will keep changing so instead i should have
    #the dir path to where all the folders are, so we can check for specific folders and if not then create the folders.

    destination_folder = 'E:\sortedDownloads'
    sort_downloads(source_folder, destination_folder)

