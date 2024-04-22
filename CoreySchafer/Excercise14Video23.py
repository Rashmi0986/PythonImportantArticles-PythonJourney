import os
from datetime import datetime

cwd = "/workspaces/PythonImportantArticles-PythonJourney/Corey Schafer"
for dirpath , dirnames , filenames in os.walk(cwd):
    print(f'Current Path: {dirpath}')
    print(f'Current dirname: {dirnames}')
    print(f'Current filenames: {filenames}')

#os.path.splitext('/tmp/test.txt')

    
