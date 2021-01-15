import watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

print('a')

class Handler (FileSystemEventHandler):
    def on_modified(self, event):
        data = open(inputFile).read().split('|')
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