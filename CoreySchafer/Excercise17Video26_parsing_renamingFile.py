import os 
"""
os.chdir('/workspaces/PythonImportantArticles-PythonJourney/Corey Schafer/TestDir')
for f in os.listdir():
    print(f)



os.chdir('/workspaces/PythonImportantArticles-PythonJourney/Corey Schafer/TestDir')
for f in os.listdir():
    print(os.path.splitext(f))


os.chdir('/workspaces/PythonImportantArticles-PythonJourney/Corey Schafer/TestDir')
for f in os.listdir():
    filename, file_extn = os.path.splitext(f)
    print("{}{}".format(filename,file_extn))
    f_title , f_course, f_num =filename.split("_")
    print(f"{f_title}_{f_course}_{f_num}")


"""
# renaming all the files here - basically shortening the name in bulk 
os.chdir('/workspaces/PythonImportantArticles-PythonJourney/Corey Schafer/TestDir')
for f in os.listdir():
    filename, file_extn = os.path.splitext(f)
    #print("{}{}".format(filename,file_extn))
    f_title , f_course, f_num =filename.split("_")

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()

    newName = "{}-{}{}".format(f_num,f_title,file_extn)
    os.rename(f, newName)
    






