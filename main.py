from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import time

print('Running')

def writeDoc(name, text):
    path = '/Users/ivanjtm/Desktop/Output/' + name
    f = open(path, "a")
    f.write(text)
    f.close()

class Handler (FileSystemEventHandler):
    def on_modified(self, event):
        data = open(inputFile).read().split('|')
        writeDoc('doc0.txt', data[0])
        writeDoc('doc1.txt', data[1])
        writeDoc('doc2.txt', data[2])
        open(inputFile).close()
        print(data)

inputFolder = 'folder'
inputFile = inputFolder + '/' + 'input.txt'

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