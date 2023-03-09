import os
path = "C:/Users/User/Desktop/pp2/tsis6"
print("directories:", "")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("files:","")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("All directories and files :")
print([ name for name in os.listdir(path)])
