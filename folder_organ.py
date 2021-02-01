import os
import shutil

extension_files = {
    'doc' : ['.doc', '.docx', '.pdf', '.html', '.htm', '.xml', '.txt', '.odt', '.xls', '.xlsx', '.ods', '.ppt', '.pptx'] ,
    'img' : ['.png', '.gif', '.jpg', '.jpeg', '.tiff', '.raw'],
    'compressed' : ['.zip', '.rar'],
    'application' : ['.exe']
}

# changing directory
dir1 = str(input())
os.chdir(dir1)

files = os.listdir(dir1)
for file in files:
    name , ext = os.path.splitext(file)
    try : 
        for key, value in extension_files.items():
            if  ext in value :
                filename = key
                if not os.path.isdir(os.path.join(dir1, filename)): 
                    os.mkdir(os.path.join(dir1, filename))
                    shutil.move(os.path.join(dir1, file), os.path.join(dir1, filename))
                else:   
                    shutil.move(os.path.join(dir1, file), os.path.join(dir1, filename))
                break
    except Exception as e :
        pass