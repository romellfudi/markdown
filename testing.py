import glob
from datetime import datetime

if glob.glob("%s-a-new-day.md"% datetime.today().strftime("%Y-%m-%d") ):
    print("Test file sucessfully")
else:
    raise Exception("Sorry, File does not created")
