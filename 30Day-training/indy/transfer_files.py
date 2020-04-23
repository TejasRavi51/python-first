import os
import sys
import shutil

def copy_file(source = None, occassion="", number=None):
    #separate the string in file name form "."
    for f in os.listdir(source):
        if f.endswith('.jpg') or f.endswith('.JPG'):
            f_path = os.path.join(source, f)
            print(f_path)
            #text_files.append(f)
            file_name = f"{occassion}{number}.JPG"
            target = os.path.join(dest_dir, file_name)
            shutil.copy( f_path , target)
            print(file_name)
            number += 1

def delete_file(source = None):
    for f in os.listdir(source):
        if f.endswith('.ARW'):
            f_path = os.path.join(source, f)
            print(f_path)
            if os.path.exists(f_path):
                os.remove(f_path)
            else:
                print("no such folder")
            

if __name__ == "__main__":
    file_path = os.path.abspath(__file__)
    Base_dir = os.path.dirname(file_path)
    #disk_path = r'J:\Raw Data\Reception\Convention'
    source_dir = os.path.join(Base_dir, "100MSDCF")
    dest_dir = os.path.join(Base_dir, "Wedding_pics")
    print(disk_path)
    try:
        number = int(sys.argv[1]) + 1
        occassion = sys.argv[2]
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir, exist_ok=True)

        copy_file(source = source_dir, occassion=occassion, number=number)
    except:
        print('enter the appropriate arguments 1.Number on last file and 2. name on current file')