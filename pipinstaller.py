import subprocess
import sys
import glob

def install(package):
    print("Dowloading package: ",package)
    subprocess.call([sys.executable, "-m", "pip", "install", package])

def main():
    a=glob.glob(r"C:/Users/Devansh/Downloads/whlsPython/*.whl")
    print(len(a))
    for i in a:
        #print(i)
        install(i)

main()