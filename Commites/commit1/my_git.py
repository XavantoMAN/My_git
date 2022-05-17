import platform
import os
import shutil

print('OS:', platform.system())
Dir = os.path.dirname(os.path.abspath(__file__))
commit = 0
Flag = True


def init():
    global commit
    command = input(">")
    if command == "init":
        if os.path.exists("my_git"):
            pass
        else:
            os.mkdir("my_git")
        ignore = open('my_git/ignore.txt', 'w')
        ignore.write('ignore.txt\ninit.txt\n*.cmd\n')
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
        f1 = open('my_git/init.txt', 'r')
        f2 = open('my_git/temp.txt', 'r')
        f3 = open('my_git/ignore.txt', 'w')
        f3.write('ignore.txt\ninit.txt\n*.cmd\nmy_git\n.idea\n')
        for i in f1:
            print(i)
            x = f2.readline()
            if x == i:
                f3.write(x)
        f1.close()
        f3.close()
        f1 = open('my_git/init.txt', 'w')
        for i in f2:
            x = f2.readline()
            f1.write(x)
        f1.close()
        f2.close()
        if os.path.exists('my_git/commit.txt'):
            com = open('my_git/commit.txt', 'r')
            commit = int(com.readline())
            com.close()
        else:
            com = open('my_git/commit.txt', 'w')
            commit = 0
            com.write(str(commit))
            com.close()
        commit += 1
        ignore = open('my_git/ignore.txt', 'r')
        list1 = ''
        for i in ignore:
            list1 += i
        list2 = list1.split("\n")
        line = f'Commites/commit{commit}'
        shutil.copytree(f'.', line, ignore=shutil.ignore_patterns('ignore.txt', 'init.txt', '*cmd', 'my_git', '.idea',
                                                                  'Commites', 'bin'))
        f1 = open('my_git/commit.txt', 'w')
        f1.write(str(commit))
        f1.close()

    else:
        print(f"{command} не является командой или оператором")
        init()


def dir_all(dir, f1):
    dirfiles = os.listdir(dir)
    for item in dirfiles:
        path = os.path.join(dir, item)
        if os.path.isfile(path):
            print('File:', item)
            print(path)
            print(os.path.getmtime(path))
            print(str(os.path.getsize(path)) + ' byte')
            print(os.path.dirname(path))
            print(os.path.basename(path))
            f1.write(path + ';' + str(os.path.getmtime(path)))
            f1.write("\n")
            print('---------------------')
        elif os.path.isdir(path):
            print('Directory:', item)
            dir_all(path, f1)


while Flag:
    init()
