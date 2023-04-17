# implement a program that prompts the user for the name of a file and then outputs that file’s media type
# if the file’s name ends, case-insensitively, in any of these suffixes: .gif, .jpg, .jpeg, .png, .pdf, .txt, .zip.
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.


name = input("\nfile name? ")
name = name.strip().lower()


if name.endswith(".gif"):
    print("image/gif")

elif name.endswith(".jpg") or name.endswith(".jpeg"):
    print("image/jpeg")

elif name.endswith(".png"):
    print("image/png")

elif name.endswith(".pdf"):
    print("application/pdf")

elif name.endswith(".txt"):
    print("text/plain")

elif name.endswith(".zip"):
    print("application/zip")

else:
    print("application/octet-stream")
