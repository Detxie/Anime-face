import glob

# mode = 1 生成train 和 valid两个txt文件
# mode = 2 生成 lables文件
mode  = 1

if mode == 1 :
    image_labels = glob.glob("labels/*")
    img_data = []
    for img_label in image_labels:
        img = img_label.split("\\")[1].split(".")[0] + ".jpg"
        img = "data/custom/images/" + img
        img_data.append(img)

    radio = 0.9
    data_num = len(img_data)
    for data in img_data[:int(data_num * radio)]: #训练集
        with open("train.txt",'a+') as f:
            f.write(data+"\n")

    for data in img_data[int(data_num*0.9):]:
        with open("valid.txt",'a+') as f:
            f.write(data+"\n")
if mode == 2:
    labels_path = glob.glob("raw_labels/*")
    for lp in labels_path:
        with open(lp,'r') as f:
            data = f.readline()

        cls , x_center , y_center , width , height = data.strip().split(" ")

        cls = 0 #做一下特殊处理，不知为何标注完后显示index为 1
        content = str(cls) + " " + x_center + " " + y_center +" " + width + " " + height + "\n"
        with open("labels/train.txt",'a+') as fp:
            fp.write(content)

