import os
import zipfile
from pathlib import Path

TRIGGER_DIR = r"C:\Users\20160\Downloads\voice"
# TRIGGER_PATH = os.environ["trigger_path"]

VOICE_DIR = r"C:\03_other\01_VTuber\01_voice"

def chose_lst(lst):
    for idx, item in enumerate(lst):
        print(f"{idx+1}: {item.name}")
    cmd = int(input("input to index:"))
    return lst[cmd-1]

def main():

    trigger_dir = Path(TRIGGER_DIR)
    trigger_path = chose_lst([x for x in trigger_dir.iterdir() if x.suffix in [".zip"]])
    print(trigger_path)

    root_dir = Path(VOICE_DIR)
    root_path = chose_lst([x for x in root_dir.iterdir() if x.is_dir()])
    print(root_path)

    type_path = chose_lst([x for x in root_path.iterdir() if x.is_dir()])
    print(type_path)

    for dir in [x for x in type_path.iterdir() if x.is_dir()]:
        print(dir)
    
    idx = input("input to index:")
    save_path = type_path / f"{idx}_{trigger_path.stem}"

    print(save_path)

    with zipfile.ZipFile(str(trigger_path)) as z:
        for info in z.infolist():
            print(info)
            try:
                info.filename = info.orig_filename.encode('cp437').decode('cp932')
            except:
                pass
            if os.sep != "/" and os.sep in info.filename:
                info.filename = info.filename.replace(os.sep, "/")
            z.extract(info, str(save_path))
    
    trigger_path.unlink()

if __name__ == "__main__":
    main()

