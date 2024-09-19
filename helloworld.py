import os
file_name = "hello_world.py"
with open(file_name, "w") as hello_world_file: 
    hello_world_file.write("""print("hello world!")""")

os.system("python3 " + file_name)
os.remove("hello_world.py")
