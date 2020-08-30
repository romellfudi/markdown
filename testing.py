import glob
if glob.glob("*-*-*-a-new-day.md"):
    print("Test file successfully")
else:
    raise Exception("Sorry, File does not created")
