name = input("file's name please: ").strip().lower()

if name.endswith(".jpeg") or name.endswith(".jpg"):
   print("image/jpeg")
elif name.endswith("gif"):
  print("image/gif")
elif name.endswith(".png"):
  print("image/png")
elif name.endswith(".zip"):
  print("application/zip")
elif name.endswith(".pdf"):
   print("application/pdf")
elif name.endswith(".txt"):
  print("text/plain")
else:
 print("application/octet-stream")
