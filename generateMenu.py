import os
from natsort import natsorted

MD_EXTENSIONS = ['.md', '.markdown']
BASE_DIR = '.'

IGNORED_FOLDERS = ['.git', '.vscode', '.idea', 'docs', '_image', '_attachment']
IGNORED_MD_FILES = ['README', '_sidebar']     # do NOT include file extensions


def removeSpaces(filepath):
    if ' ' in filepath:
        new_filepath = filepath.replace(' ', '')
        print("[removeSpaces] rename", filepath, "to", new_filepath)
        os.rename(filepath, new_filepath)
        return new_filepath
    else:
        return filepath


menu = "* [**Home**](/)\n"
def generateMenuItem(filepath, level):
    global menu
    basename = os.path.basename(filepath)
    spaces = ' '*(level-1)*4
    # isdir
    if os.path.isdir(filepath):
        menu += '\n' + spaces + '* ' + basename + '\n'
    # isfile
    else:
        fileNameWithoutExt, _ = os.path.splitext(basename)
        menu += spaces + "- [%s](%s)" % (fileNameWithoutExt, filepath) + '\n'


def walk(root, level):
    root = removeSpaces(root)
    basename = os.path.basename(root)
    # isdir
    if os.path.isdir(root):
        if basename in IGNORED_FOLDERS: return
        # TODO: do something with the folder
        print("[level=%d] Dir: %s" % (level, root))
        generateMenuItem(root, level)
        # sort and walk every file in this folder
        fileList = os.listdir(root)
        # fileList.sort()
        fileList = natsorted(fileList)
        for file in fileList:
            filepath = os.path.join(root, file)
            walk(filepath, level+1)
    # isfile
    else:
        fileNameWithoutExt, ext = os.path.splitext(basename)
        if (ext not in MD_EXTENSIONS) or (fileNameWithoutExt in IGNORED_MD_FILES): return
        # TODO: do something with the file
        print("[level=%d] File: %s" % (level, root))
        generateMenuItem(root, level)


def walkSubdirs(root, level):
    fileList = os.listdir(root)
    # fileList.sort()
    fileList = natsorted(fileList)
    for file in fileList:
        filepath = os.path.join(root, file)
        if os.path.isdir(filepath):
            walk(filepath, level+1)


def generateMenu():
    """Generate menu and write to '_sidebar.md'
    """
    # walk(BASE_DIR, 0)        # walk including BASE_DIR
    walkSubdirs(BASE_DIR, 0)   # walk without BASE_DIR itself

    global menu
    # print("---------- Menu --------------")   
    # print(menu)
    with open(os.path.join(BASE_DIR, '_sidebar.md'), 'w') as f:
        f.write(menu)


generateMenu()
