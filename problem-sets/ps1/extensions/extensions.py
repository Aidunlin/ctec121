# extensions.py
# Aidan Linerud

# Prompt the user for the name of a file
file_name = input("File name: ")
file_name = file_name.strip().lower()

# Display the file extension's corresponding media type
# (or a default type for unknown extensions)
if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
    print("image/jpeg")
elif file_name.endswith(".png"):
    print("image/png")
elif file_name.endswith(".pdf"):
    print("application/pdf")
elif file_name.endswith(".txt"):
    print("text/plain")
elif file_name.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
