import platform
import os
import shutil
import re

print('OS:', platform.system())
Dir = os.path.dirname(os.path.abspath(__file__))
Flag = True
lines = []
newDir = ''


def init():
    command = input(">")
    if command == "init":
        if os.path.exists("my_git"):
            pass
        else:
            os.mkdir("my_git")
        ignore = open('my_git/ignore.txt', 'w')
        ignore.write('.git\n.vs\n.idea\nignore.txt\ninit.txt\n*.cmd\nmy_git\nCommites\nbin\n')
        ignore.close()
        with open('my_git/init.txt', 'w') as f1:
            dir_all(Dir, f1)
    elif command == "exit":
        global Flag
        Flag = False
    elif command == "commit":
        temp = open('my_git/temp.txt', 'w')
        dir_all(Dir, temp)
        temp.close()
        file1 = open('my_git/init.txt', 'r')
        f2 = open('my_git/temp.txt', 'r')
        f3 = open('my_git/ignore.txt', 'w')
        f3.write('.git\n.vs\n.idea\nignore.txt\ninit.txt\n*.cmd\nmy_git\nCommites\nbin\n')
        for i in file1:
            x = f2.readline()
            #print('i=' + i)
            #print('X=' + x + '-----')
            if x == i:
                line2 = x.split(';')
                f3.write(line2[0] + '\n')
        file1.close()
        f2.close()
        f3.close()
        ignore = open('my_git/ignore.txt', 'r')
        global lines
        while True:
            s = ignore.readline()
            line1 = re.sub('\n', '', s)
            if not line1:
                break
            #print(line1)
            lines.append(line1)

        ignore.close()
        with open('my_git/init.txt', 'w') as f1:
            dir_all(Dir, f1)
        name_commit = input("Введите название коммита:")
        com_dir = os.path.join(Dir, 'Commites', name_commit)
        if not os.path.exists(com_dir):
            os.mkdir(com_dir)
            commit_tree(Dir, com_dir)
            init()
        else:
            print('Commit exists!')

    else:
        print(f"{command} не является командой или оператором")
        init()


def ignore(f):
    global lines
    for item in lines:
        if f == item:
            return True
            
    return False


def dir_all(Dir, f1):
    dirfiles = os.listdir(Dir)
    for item in dirfiles:
        path = os.path.join(Dir, item)
        if os.path.isfile(path):
            f1.write(os.path.basename(path) + ';' + str(os.path.getmtime(path)))
            f1.write("\n")
        elif os.path.isdir(path):
            dir_all(path, f1)


def fill_dirs(Dir, line):
    dirfiles = os.listdir(Dir)
    for item in dirfiles:
        if ignore(item):
            continue

        path = os.path.join(Dir, item)
        if os.path.isfile(path):
            shutil.copy(path, line)
        elif os.path.isdir(path):
            print('Directory:', item)
            newDir = os.path.join(line, item)
            os.mkdir(newDir)
            commit_tree(path, line)


def commit_tree(Dir, line):
    global newDir
    dirfiles = os.listdir(Dir)
    for item in dirfiles:
        #print(item)
        if ignore(item):
            continue

        path = os.path.join(Dir, item)
        if os.path.isfile(path):
            shutil.copy(path, line)
        elif os.path.isdir(path):
            continue

    for item in dirfiles:
        if ignore(item):
            continue

        path = os.path.join(Dir, item)
        if os.path.isfile(path):
            continue
        elif os.path.isdir(path):
            print('Directory:', item)
            newDir = os.path.join(line, item)
            os.mkdir(newDir)
            fill_dirs(path, newDir)


while Flag:
    init()
