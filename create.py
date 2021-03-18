import os
import glob
import json
import cv2
import numpy as np
import shutil


def ensure_color(image):
    if len(image.shape) == 2:
        return np.dstack([image] * 3)
    elif image.shape[2] == 1:
        return np.dstack([image] * 3)
    return image

net = cv2.dnn.readNetFromCaffe(
    "deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel"
)


def main():
    configs = json.load(open("./configs/fer2013_config.json"))
    image_size = (configs["image_size"], configs["image_size"])
    videoList = os.listdir('./video')

    for videoName in videoList:
        
        videoPath = os.path.join('video',videoName)
        videoName = videoName.split('.')[0]
        outputPath = os.path.join('output',videoName)

        if os.path.exists(outputPath):continue
        else:
            os.mkdir(outputPath)
            chopFacePath =os.path.join(outputPath,'chopFace')
            os.mkdir(chopFacePath)
            os.mkdir(os.path.join(outputPath,'keyExpFrame'))
            with open(os.path.join(outputPath,'conversation.txt'),'w+',encoding='UTF-8') as f:
                f.write("")
            vid = cv2.VideoCapture(videoPath)
            idx = 0
            print(videoName+' 正在截取……')
            while True:
                try:
                    ret, frame = vid.read()
                    if frame is None or ret is not True:
                        break

                    h, w = frame.shape[:2]
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    # gray = frame

                    blob = cv2.dnn.blobFromImage(
                        cv2.resize(frame, (300, 300)),
                        1.0,
                        (300, 300),
                        (104.0, 177.0, 123.0),
                    )
                    net.setInput(blob)
                    faces = net.forward()

                    for i in range(0, faces.shape[2]):
                        confidence = faces[0, 0, i, 2]
                        if confidence < 0.5:
                            continue
                        box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
                        start_x, start_y, end_x, end_y = box.astype("int")

                        # covnert to square images
                        center_x, center_y = (start_x + end_x) // 2, (start_y + end_y) // 2
                        square_length = ((end_x - start_x) + (end_y - start_y)) // 2 // 2

                        square_length *= 1.1

                        start_x = int(center_x - square_length)
                        start_y = int(center_y - square_length)
                        end_x = int(center_x + square_length)
                        end_y = int(center_y + square_length)

                        cv2.rectangle(
                            frame, (start_x, start_y), (end_x, end_y), (179, 255, 179), 2
                        )
                        # cv2.rectangle(frame , (x, y), (x + w, y + h), (179, 255, 179), 2)

                        # face = gray[y:y + h, x:x + w]
                        face = gray[start_y:end_y, start_x:end_x]

                        # face = ensure_color(face)

                        face = cv2.resize(face, image_size)
                        faceName = videoName+'-%04d.jpg'%idx
                        cv2.imwrite(os.path.join(chopFacePath,faceName),face)
                        idx+=1

                except:
                    continue

if __name__ == "__main__":
    main()
    print('Done.')