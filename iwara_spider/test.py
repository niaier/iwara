import os

def countVideo():
#     os.chdir("/root/iwara_all_linux/filedir/")
#     os.system('ls -l | grep "^d" | wc -l')
#     os.system('dir')
    with os.popen("dir","r") as p:
        r = p.read()
        print("========r=========\n",)
        print("========r=========\n")

countVideo()



