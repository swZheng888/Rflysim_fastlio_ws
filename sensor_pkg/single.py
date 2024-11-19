
# import required libraries
# pip3 install pymavlink pyserial

import cv2
import numpy as np
import time
import VisionCaptureApi
import math
import ReqCopterSim
import RflyRosStart
import UE4CtrlAPI
import sys

# 启用ROS发布模式
VisionCaptureApi.isEnableRosTrans = True

req = ReqCopterSim.ReqCopterSim() # 获取局域网内所有CopterSim程序的电脑IP列表
StartCopterID = 1 # 初始飞机的ID号
TargetIP = req.getSimIpID(StartCopterID) # 获取CopterSim的1号程序所在电脑的IP，作为目标IP

ue = UE4CtrlAPI.UE4CtrlAPI(TargetIP)
# Send command to UE4 Window 1 to change resolution 
ue.sendUE4Cmd('r.setres 640x480w',0) # 设置UE4窗口分辨率，注意本窗口仅限于显示，取图分辨率在json中配置，本窗口设置越小，资源需求越少。
ue.sendUE4Cmd('t.MaxFPS 30',0) # 设置UE4最大刷新频率，同时也是取图频率
time.sleep(2)    
# 注意：如果是本电脑运行的话，那TargetIP是127.0.0.1的本机地址；如果是远程访问，则是192打头的局域网地址。
# 因此本程序能同时在本机运行，也能在其他电脑运行。

print('Request CopterSim Send data.')
req.sendReSimIP(StartCopterID) # 请求回传数据到本电脑

print(RflyRosStart.isLinux,RflyRosStart.isRosOk)

# 自动开启mavros
# if not (RflyRosStart.isLinux and RflyRosStart.isRosOk):
#     print('This demo can only run on with Ros')
#     sys.exit(0)

# 自动开启RosCore
#ros = RflyRosStart.RflyRosStart(StartCopterID,TargetIP)


vis = VisionCaptureApi.VisionCaptureApi(TargetIP)

# VisionCaptureApi 中的配置函数
vis.jsonLoad(jsonPath = "singleConfig.json") # 加载Config.json中的传感器配置文件
isSuss = vis.sendReqToUE4(
    0, TargetIP
)
vis.startImgCap() # 开启取图循环，执行本语句之后，已经可以通过vis.Img[i]读取到图片了
print('Start Image Reciver')
vis.sendImuReqCopterSim(StartCopterID,TargetIP) # 发送请求，从目标飞机CopterSim读取IMU数据,回传地址为127.0.0.1，默认频率为200Hz
# 执行本语句之后，会自动开启数据监听，已经可以通过vis.imu读取到IMU数据了。

#ros.EndRosLoop()
