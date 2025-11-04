from pathlib import PurePath, Path

p = PurePath(
    "C:/Users/Anton/OneDrive/Desktop/Python_Projects/Pyhon_Neoversity/module05/4_shutil/1_files.py"
)
print(p)  # 4_shutil\1_files.py
print(type(p))  # 'pathlib._local.PureWindowsPath'>
print(p.parent)  # 4_shutil - parent of path
print(p.name)  # 1_files.py - name of file
print(p.stem)  # 1_files - name without suffix
print(p.suffix)  # .py - suffix
p = PurePath().joinpath(
    "C:",
    "Users",
    "Anton",
    "OneDrive",
    "Desktop",
    "Python_Projects",
    "Pyhon_Neoversity",
    "module05",
    "4_shutil",
    "2_files.py",
)
p = p.with_suffix(".txt")  # change in end suffix from .py to .txt
print(p)  # join two other path in one

p = Path("example.txt")
print(p.exists())  # False, don't create example.txt
p = Path("test.txt")
print(p.exists())  # True, create file early test.txt
print(p.is_dir())  # False, because is not directory
print(p.is_file())  # True, because is file


# C:/Users/Anton/OneDrive/Desktop/Python_Projects/Pyhon_Neoversity/module05/4_shutil/1_files.py  ->  absolute path Windows from disk
# /user/bin/python3 ->  absolute path from root directory "./"
# ./4_shutil/1_files.py -> relative path in Windows from currect directory


# base_dir = Path("F:\pylab")  # var create path for directory
# print(base_dir)
# file_p = base_dir / "PythonBestPractices" / "file.txt"  # add to path directory and file
# print(file_p)
# file_p = file_p.joinpath(
#     "F:", "pylab", "PythonBestPractices", "file.txt"
# )  # F:\pylab\PythonBestPractices\file.txt\pylab\PythonBestPractices\file.txt without F: in second
# print(file_p)

# Get absilute path
base_dir = Path("1_files.py")
# C:\Users\Anton\OneDrive\Desktop\Python_Projects\Pyhon_Neoversity\module05\1_files.py
print(base_dir.absolute())

# From absolute to relative use r"" string
base_dir = Path(
    r"C:\Users\Anton\OneDrive\Desktop\Python_Projects\Pyhon_Neoversity\module05\1_files.py"
)
print(base_dir.relative_to(r"C:\Users\Anton"))
# From absolute to relative use \\
base_dir = Path(
    "C:\\Users\\Anton\\OneDrive\\Desktop\\Python_Projects\\Pyhon_Neoversity\\module05\\1_files.py"
)
print(base_dir.relative_to("C:\\Users\\Anton"))


# Two ways to execute commands
base_dir = Path(".")  # use current directory
file = (base_dir / "test1.txt").absolute()  # add to current directory file test1.txt
print(file)  # print new path with absolute path
# C:\Users\Anton\OneDrive\Desktop\Python_Projects\Pyhon_Neoversity\module05\test1.txt


base_dir = Path(".").absolute()  # use current directory with absolut path
file = base_dir / "test1.txt"  # add to current directory file test1.txt
print(file)  # print new path with absolute path
# C:\Users\Anton\OneDrive\Desktop\Python_Projects\Pyhon_Neoversity\module05\test1.txt
file.write_text(
    "Hello my name is Anton\nHow are you?", encoding="utf-32"
)  # create and write text in file
print(file.read_text(encoding="utf-32"))  # output in terminal text
