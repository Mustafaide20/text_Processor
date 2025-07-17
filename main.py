with open("ملف نصي.txt","r",encoding="utf-8") as file:
  lines=file.readlines()
  new=[line.strip()[::-1] for line in lines]
  print(new)
with open("new file.txt","a",encoding="utf-8") as new_file:
  for line in new:
   new_file.write(line+ "\n")
    