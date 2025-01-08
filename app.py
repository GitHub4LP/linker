import os
import subprocess

def main():
    print("添加执行权限...")
    subprocess.run(["chmod", "777", "linker"])
    print("Starting the app...")
    # 运行当前目录下的 linker 文件
    subprocess.run(["./linker"])

if __name__ == "__main__":
    main()