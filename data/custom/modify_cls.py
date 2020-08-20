import glob

labels = glob.glob("labels/*")

for lbs in labels:
    with open(lbs,"r") as f:
        data = f.readline()

    cls,x,y,w,h = data.strip().split(" ")

    cls = 0

    content = str(cls) + " " + x + " " + y + " " + w + " " + h

    with open(lbs,'w') as fp:
        fp.write(content + "\n")