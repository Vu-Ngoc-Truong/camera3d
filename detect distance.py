import cv2
import pyrealsense2
from realsense_depth import *

point = (400, 300)

def show_distance(event, x, y, args, params):
    global point
    point = (x, y)
    # print(x,y)

# Initialize Camera Intel Realsense
dc = DepthCamera()

# Create mouse event
cv2.namedWindow("Color frame")
cv2.setMouseCallback("Color frame", show_distance)

while True:
    ret, depth_frame, color_frame = dc.get_frame()

    # Show distance for a specific point
    cv2.circle(color_frame, point, 4, (0, 0, 255))
    cv2.circle(depth_frame, point, 4, (0, 0, 255))
    distance = depth_frame[point[1], point[0]]
    # print("color: ", color_frame.shape)
    # print("depth: ", depth_frame.shape)

    width = 640
    height = 480
    for i in range(height):
        for j in range(width):
            dis = depth_frame[i,j]
            if dis > 3000 or dis < 300 :
                dis = 0
            else:
                dis = 10000 + (dis - 300)*20
            depth_frame[i,j] =  dis

    cv2.putText(color_frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
    cv2.putText(depth_frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (222, 222, 222), 4)

    cv2.imshow("depth frame", depth_frame)
    cv2.imshow("Color frame", color_frame)
    key = cv2.waitKey(1)
    if key == 27:
        break