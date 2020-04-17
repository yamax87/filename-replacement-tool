import shutil
import os
import sys

root_folder = input('Enter the folder location containing the files to be renamed.\n')

try:
    os.listdir(root_folder)
except FileNotFoundError:
    print('\nSorry, this folder does not exist.')
    sys.exit()
if len(os.listdir(root_folder)) == 0:
    print('\nSorry, this folder appears to be empty. ')
    sys.exit()

target_nameText = input('\nEnter the text in each name that you want to replace.\n')

replacement_nameText = input('\nEnter the replacement name text.\n')

invalid_chars = ['//','\\',':','*','?','"','<','>','|']

for i in invalid_chars:
    if i in replacement_nameText:
        print('\nSorry, that symbol is not allowed.')
        sys.exit()

rename_files_in_subfolders = input('\nDo you want to change files in subfolders within this folder? (y/n) \n')
rename_files_in_subfolders = rename_files_in_subfolders.lower()
if (rename_files_in_subfolders != 'y') and (rename_files_in_subfolders != 'n'):
    print('\nSorry, that\'s not a valid input.')
    sys.exit()

print('\n')


not_renamed_files_Total = 0
renamed_files_Total = 0

if rename_files_in_subfolders == 'n':
    for folderTitle, childFolder, listOfFiles in os.walk(root_folder):
        if folderTitle == root_folder:
            print('\n')
            for eachFile in listOfFiles:
                print('Found file: ' + eachFile)
                oldFilePath = os.path.join(folderTitle,eachFile)
                
                eachFile = eachFile.replace(target_nameText , replacement_nameText)
                newFilePath = os.path.join(folderTitle,eachFile)
                shutil.move(oldFilePath, newFilePath)
                
                if oldFilePath == newFilePath:
                    print('Text to be replaced is not present in this file. No changes made to this file\'s name.\n')
                    not_renamed_files_Total += 1
                else:
                    print('File ' + eachFile + ' renamed successfully.\n')
                    renamed_files_Total += 1

if rename_files_in_subfolders == 'y':
    for folderTitle, childFolder, listOfFiles in os.walk(root_folder):
        print('\n')
        for eachFile in listOfFiles:
            print('Found file: ' + eachFile)
            oldFilePath = os.path.join(folderTitle,eachFile)
            
            eachFile = eachFile.replace(target_nameText , replacement_nameText)
            newFilePath = os.path.join(folderTitle,eachFile)
            shutil.move(oldFilePath, newFilePath)
            
            if oldFilePath == newFilePath:
                print('Text to be replaced is not present in this file. No changes made to this file\'s name.\n')
                not_renamed_files_Total += 1
            else:
                print('File ' + eachFile + ' renamed successfully.\n')
                renamed_files_Total += 1


print('-'*50)
if not_renamed_files_Total + renamed_files_Total > 0:    
    print('\nTotal files found: ' + str(not_renamed_files_Total + renamed_files_Total))
    print('Filenames changed: ' + str(renamed_files_Total))
    print('Filenames not changed: ' + str(not_renamed_files_Total))
else:
    print('No files were found in this directory.')
print('-'*50)

print('\n####### PROCESS COMPLETED #######')
        

