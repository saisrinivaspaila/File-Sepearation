import os 
import pathlib
import shutil
folderPath = "SelectedFolder" #Copy relative Path
for files in pathlib.Path(folderPath).iterdir():
    
    if os.path.isdir(str(files)):
        continue

    fileName = ""
    for counter in str(files)[::-1]:
        if counter=="/":
            break
        fileName = counter+fileName

    dirName = ""
    files = str(files)[::-1]
    print(fileName,dirName)
    for counter in files:
        if counter==".":
            break
        dirName = counter + dirName
    dirName = "Files " + dirName
    
    try:
        os.mkdir(folderPath+"/"+dirName)
    except:
        pass 
    shutil.move(folderPath+"/"+fileName,folderPath+"/"+dirName+"/"+fileName)