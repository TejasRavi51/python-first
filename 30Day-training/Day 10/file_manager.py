import os

this_file_path = os.path.abspath(__file__)
base_dir = os.path.dirname(this_file_path)
proj_dir = os.path.dirname(base_dir)

#print(this_file_path, base_dir, proj_dir)
email_txt = os.path.join(base_dir, "templates", "email.txt")
#email_txt = "templates/email.txt"

content = ""

with open(email_txt, 'r') as f:
    content = f.read()

print(content.format(name="teja")) 