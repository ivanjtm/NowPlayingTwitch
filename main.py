from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import time
import requests

print('Running')



def writeDoc(name, text):
    path = '/Users/ivanjtm/Desktop/Output/' + name
    f = open(path, "a")
    f.truncate(0)
    f.write(text)
    f.close()

def downloadPhoto(link):
    image_url = link.replace('https://youtu.be/','https://img.youtube.com/vi/')
    image_url = image_url + '/0.jpg'
    print(image_url)
    img_data = requests.get(image_url).content
    open('/Users/ivanjtm/Desktop/Output/image.jpg', 'wb').truncate(0)
    with open('/Users/ivanjtm/Desktop/Output/image.jpg', 'wb') as handler:
        handler.write(img_data)

class Handler (FileSystemEventHandler):
    def on_modified(self, event):
    
        data = open(inputFile).read().split('|')
        
        if data != ['']:
            print(data)
            writeDoc('title.txt', data[0])
            writeDoc('duration.txt', data[1])
            downloadPhoto(data[2])
            open(inputFile).close()
        

inputFolder = '/Users/ivanjtm/Documents/Nightbot'
inputFile = inputFolder + '/' + 'current_song.txt'

event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, inputFolder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()