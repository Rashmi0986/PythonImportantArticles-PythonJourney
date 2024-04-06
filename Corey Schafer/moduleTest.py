#import my_module

#import my_module as mm 
from datetime import datetime
import sys
from my_module import find_index,test
courses = ["History", "Arts", "biology", "geology"]
#index = my_module.find_index(courses,'Math')
#index = mm.find_index(courses,'Math')

index = find_index(courses,'biology')
print(index)
print(test)

print(sys.path)
#today = datetime.today
print(datetime.today())
import os
print(os.getcwd())


