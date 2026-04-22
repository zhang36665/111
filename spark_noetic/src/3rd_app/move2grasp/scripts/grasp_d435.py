#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import random
import ctypes
from turtle import position

import roslib
import rospy
import smach
import smach_ros
import threading
import string
import math
import cv2
import numpy as np
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from geometry_msgs.msg import Pose, Point, Quaternion
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from spark_carry_object.msg import *


class GraspObject():
    '''
    监听主控，用于物品抓取功能
    '''

    def __init__(self):
        '''
        初始化
        '''
        
        global xc, yc, xc_prev, yc_prev, found_count, quanju, hx, hy, hz
        xc = 0
        yc = 0
        xc_prev = xc
        yc_prev = yc
        found_count = 0
        quanju = 120
        hx = 200
        hy = 0
        hz = 40      
        self.is_found_object = True
        # self.sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.image_cb, queue_size=1)
        # 订阅机械臂抓取指令
        self.sub2 = rospy.Subscriber(
            '/grasp', String, self.grasp_cp, queue_size=1)
        # 发布机械臂位姿
        self.pub1 = rospy.Publisher(
            'position_write_topic', position, queue_size=10)
        # 发布机械臂吸盘
        self.pub2 = rospy.Publisher('pump_topic', status, queue_size=1)
        # 发布机械臂状态
        self.grasp_status_pub = rospy.Publisher(
            'grasp_status', String, queue_size=1)
        # 发布TWist消息控制机器人底盘
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        pos = position()
        pos.x = 120
        pos.y = 0
        pos.z = 40
        self.pub1.publish(pos)

    def grasp_cp(self, msg):
        if msg.data == '0':
            # 订阅摄像头话题,对图像信息进行处理
            self.sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.image_cb, queue_size=1)
            self.is_found_object = True
            rate = rospy.Rate(10)
            times=0
            steps=0
            self.grasp()
            status=String()
            status.data='1'
            self.grasp_status_pub.publish(status) 
            
            while not self.is_found_object:
                rate.sleep()
                times+=1
                # 转一圈没有发现可抓取物体,退出抓取
                if steps>=5:
                    self.sub.unregister()
                    print("stop grasp\n")
                    status=String()
                    status.data='-1'
                    self.grasp_status_pub.publish(status)
                    return
                # 旋转一定角度扫描是否有可供抓取的物体
                if times>=30:
                    times=0
                    steps+=1
                    
                    print("not found\n")
            print("unregisting sub\n")
            self.sub.unregister()
            print("unregisted sub\n")
            
            # 抓取检测到的物体    
            
        if msg.data=='1':
            # 放下物体
            self.is_found_object = True
            self.release_object()
            status=String()
            status.data='0'
            self.grasp_status_pub.publish(status) 
        if msg.data=='2':
            # 放下物体
            self.is_found_object = True
            self.release_objectu()
            status=String()
            status.data='0'
            self.grasp_status_pub.publish(status) 
        if msg.data=='3':
            # 放下物体
            self.is_found_object = True
            self.release_objectj()
            status=String()
            status.data='0'
            self.grasp_status_pub.publish(status) 
        if msg.data=='4':
            # 放下物体
            self.is_found_object = True
            self.release_objecth()
            status=String()
            status.data='0'
            self.grasp_status_pub.publish(status) 
        if msg.data=='5':
            # \u653e\u4e0b\u7269\u4f53
            self.is_found_object = True
            self.release_objectk()
            status=String()
            status.data='0'
            self.grasp_status_pub.publish(status) 
        if msg.data=='6':
            # 放下物体
            self.is_found_object = True
            self.release_objecty()
            status=String()
            status.data='0'
            self.grasp_status_pub.publish(status) 
        if msg.data=='7':
            # 放下物体
            self.is_found_object = True
            self.release_objecti()
            status=String()
            status.data='0'
            self.grasp_status_pub.publish(status) 
        if msg.data=='8':
            # 放下物体
            self.is_found_object = True
            self.release_objectb()
            status=String()
            status.data='0'
            self.grasp_status_pub.publish(status) 
        if msg.data=='9':
            # 放下物体
            self.is_found_object = True
            self.release_objectn()
            status=String()
            status.data='0'
            self.grasp_status_pub.publish(status) 
        if msg.data=='10':
            # 放下物体
            self.is_found_object = True
            self.release_objectm()
            status=String()
            status.data='0'
            self.grasp_status_pub.publish(status) 
        if msg.data=='11':
            # 放下物体
            self.is_found_object = True
            self.release_objectv()
            status=String()
            status.data='0'
            self.grasp_status_pub.publish(status) 
        if msg.data=='12':
            # 放下物体
            self.is_found_object = True
            self.release_object11()
            status=String()
            status.data='0'
            self.grasp_status_pub.publish(status) 
        if msg.data=='13':
            # 放下物体
            self.is_found_object = True
            self.release_object22()
            status=String()
            status.data='0'
            self.grasp_status_pub.publish(status) 
        if msg.data=='14':
            # 放下物体
            self.is_found_object = True
            self.release_object33()
            status=String()
            status.data='0'
            self.grasp_status_pub.publish(status) 
        if msg.data=='15':
            # 放下物体
            self.is_found_object = True
            self.release_object44()
            status=String()
            status.data='0'
            self.grasp_status_pub.publish(status) 

        if msg.data=='16':
            # 放下物体
            self.is_found_object = True
            self.release_object55()
            status=String()
            status.data='0'
            self.grasp_status_pub.publish(status) 

    # 执行抓取
    def grasp(self):
    
        print("kaishizhuaqu\n")
        global xc, yc, found_count
        # stop function

        filename = os.environ['HOME'] + "/thefile.txt"
        file_pix = open(filename, 'r')
        s = file_pix.read()
        file_pix.close()
        #print(s)
        arr=s.split()
        a1=arr[0]
        a2=arr[1]
        a3=arr[2]
        a4=arr[3]
        a = [0]*2
        b = [0]*2
        a[0]=float(a1)
        a[1]=float(a2)
        b[0]=float(a3)
        b[1]=float(a4)
        #print('k and b value:',a[0],a[1],b[0],b[1])
        r1 = rospy.Rate(0.095)
        r2 = rospy.Rate(1)
        pos = position()
        # 物体所在坐标+标定误差
        
	    # pos.z = 20
        #print("z = 20\n")
        self.pub1.publish(pos)
        #r2.sleep()
        # go down -100
        #pos.z = -50
        self.pub1.publish(pos)
        #print("z = -83\n")
        #r2.sleep()

        # 开始吸取物体
        self.pub2.publish(1)
        r2.sleep()

        # 提起物体
        #pos.x = 250  #160
        #pos.y = 0
        #pos.z = 150  #55
        self.pub1.publish(pos)
       #r1.sleep()
    # 使用CV检测物体       
    def image_cb(self, data):
        global xc, yc, xc_prev, yc_prev, found_count
        # change to opencv
        try:
            cv_image1 = CvBridge().imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print('error')

        # change rgb to hsv
        cv_image2 = cv2.cvtColor(cv_image1, cv2.COLOR_BGR2HSV)

        # 蓝色物体颜色检测范围
        LowerBlue = np.array([95, 90, 80])
        UpperBlue = np.array([130, 255, 255])
        mask = cv2.inRange(cv_image2, LowerBlue, UpperBlue)
        cv_image3 = cv2.bitwise_and(cv_image2, cv_image2, mask=mask)

        # gray process
        cv_image4 = cv_image3[:, :, 0]

        # smooth and clean noise
        blurred = cv2.blur(cv_image4, (9, 9))
        (_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
        cv_image5 = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        cv_image5 = cv2.erode(cv_image5, None, iterations=4)
        cv_image5 = cv2.dilate(cv_image5, None, iterations=4)

        # detect contour
        # cv2.imshow("win1", cv_image1)
        # cv2.imshow("win2", cv_image5)
        # cv2.waitKey(1)
        contours, hier = cv2.findContours(cv_image5, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # if find contours, pick the biggest box
        if len(contours) > 0:
            size = []
            size_max = 0
            for i, c in enumerate(contours):
                rect = cv2.minAreaRect(c)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                x_mid = (box[0][0] + box[2][0] + box[1][0] + box[3][0]) / 4
                y_mid = (box[0][1] + box[2][1] + box[1][1] + box[3][1]) / 4
                w = math.sqrt((box[0][0] - box[1][0]) ** 2 + (box[0][1] - box[1][1]) ** 2)
                h = math.sqrt((box[0][0] - box[3][0]) ** 2 + (box[0][1] - box[3][1]) ** 2) 
                size.append(w * h)
                if size[i] > size_max:
                    size_max = size[i]
                    index = i
                    xc = x_mid
                    yc = y_mid
            # if box is not moving for 20 times
            # print found_count
            if found_count >= 30:
                self.is_found_object = True
                cmd_vel = Twist()
                self.cmd_vel_pub.publish(cmd_vel)
            else:
                # if box is not moving
                if abs(xc - xc_prev) <= 2 and abs(yc - yc_prev) <= 2:
                    found_count = found_count + 1
                else:
                    found_count = 0
        else:
            found_count = 0
        xc_prev = xc
        yc_prev = yc
    # 释放物体
    def release_object(self):
        r1 = rospy.Rate(0.15)  # 5s
        r2 = rospy.Rate(1)
        pos = position()
        # go forward
        #pos.x = 200
        #pos.y = 0
        #pos.z = -40  #-80
        self.pub1.publish(pos)
        #r1.sleep()

        # stop pump
        self.pub2.publish(0)
        r2.sleep()
        #r1.sleep()
        #pos.x = 120
        #pos.y = 0
        #pos.z = 35
        self.pub1.publish(pos)
        #r1.sleep()
        return 'succeeded'
    def release_objectu(self):
        global hx
        global hy
        global hz        
        hx += 10 
        if hx > 340:
        	hx = 340   
        print('hx=',hx)
        r1 = rospy.Rate(0.15)  # 5s
        r2 = rospy.Rate(10)
        pos = position()
        # go forward            
        pos.x = hx
        pos.y = hy
        pos.z = hz  #-80
        self.pub1.publish(pos)
        r2.sleep()

        # stop pump
        #self.pub2.publish(0)
        #r2.sleep()
        #r1.sleep()
        #pos.x = 120
        #pos.y = 0
        #pos.z = 35
        self.pub1.publish(pos)
        #r1.sleep()
        return 'succeeded'
    def release_objectj(self):
        global hx
        global hy
        global hz
        hx -= 10
        if hx < 0:
        	hx = 0   
        print('hx=',hx)  
        r1 = rospy.Rate(0.15)  # 5s
        r2 = rospy.Rate(10)
        pos = position()
        # go forward            
        pos.x = hx
        pos.y = hy
        pos.z = hz  #-80
        self.pub1.publish(pos)
        r2.sleep()

        # stop pump
        #self.pub2.publish(0)
        #r2.sleep()
        #r1.sleep()
        #pos.x = 120
        #pos.y = 0
        #pos.z = 35
        self.pub1.publish(pos)
        #r1.sleep()
        return 'succeeded'
    def release_objecth(self):
        global hx
        global hy
        global hz
        hy += 10 
        if hy > 360:
        	hy = 360  
        print('hy=',hy)       
        r1 = rospy.Rate(0.15)  # 5s
        r2 = rospy.Rate(10)
        pos = position()
        # go forward            
        pos.x = hx
        pos.y = hy
        pos.z = hz  #-80
        self.pub1.publish(pos)
        r2.sleep()

        # stop pump
        #self.pub2.publish(0)
        #r2.sleep()
        #r1.sleep()
        #pos.x = 120
        #pos.y = 0
        #pos.z = 35
        self.pub1.publish(pos)
        #r1.sleep()
        return 'succeeded'
    def release_objectk(self):
        global hx
        global hy
        global hz
        hy -= 10 
        if hy < -350:
        	hy = -350 
        print('hy=',hy)       
        r1 = rospy.Rate(0.15)  # 5s
        r2 = rospy.Rate(10)
        pos = position()
        # go forward            
        pos.x = hx
        pos.y = hy
        pos.z = hz  #-80
        self.pub1.publish(pos)
        r2.sleep()

        # stop pump
        #self.pub2.publish(0)
        #r2.sleep()
        #r1.sleep()
        #pos.x = 120
        #pos.y = 0
        #pos.z = 35
        self.pub1.publish(pos)
        #r1.sleep()
        return 'succeeded'
    def release_objecty(self):
        global hx
        global hy
        global hz
        hz += 10 
        if hz > 170:
        	hz = 170 
        print('hz=',hz)       
        r1 = rospy.Rate(0.15)  # 5s
        r2 = rospy.Rate(10)
        pos = position()
        # go forward            
        pos.x = hx
        pos.y = hy
        pos.z = hz  #-80
        self.pub1.publish(pos)
        r2.sleep()

        # stop pump
        #self.pub2.publish(0)
        #r2.sleep()
        #r1.sleep()
        #pos.x = 120
        #pos.y = 0
        #pos.z = 35
        self.pub1.publish(pos)
        #r1.sleep()
        return 'succeeded'
    def release_objecti(self):
        global hx
        global hy
        global hz
        hz -= 10
        if hz < -50:
        	hz = -50 
        print('hz=',hz)       
        r1 = rospy.Rate(0.15)  # 5s
        r2 = rospy.Rate(10)
        pos = position()
        # go forward            
        pos.x = hx
        pos.y = hy
        pos.z = hz  #-80
        self.pub1.publish(pos)
        r2.sleep()

        # stop pump
        #self.pub2.publish(0)
        #r2.sleep()
        #r1.sleep()
        #pos.x = 120
        #pos.y = 0
        #pos.z = 35
        self.pub1.publish(pos)
        #r1.sleep()
        return 'succeeded'
    def release_objectb(self):
        global hx
        global hy
        global hz
        hz = -40
        print('hz=',hz)  
        r1 = rospy.Rate(0.15)  # 5s
        r2 = rospy.Rate(10)
        pos = position()
        # go forward            
        pos.x = hx
        pos.y = hy
        pos.z = hz  #-80
        self.pub1.publish(pos)
        r2.sleep()

        # stop pump
        #self.pub2.publish(0)
        #r2.sleep()
        #r1.sleep()
        #pos.x = 120
        #pos.y = 0
        #pos.z = 35
        self.pub1.publish(pos)
        #r1.sleep()
        return 'succeeded'
    def release_objectn(self):
        global hx
        global hy
        global hz
        hz = 60
        print('hz=',hz)  
        r1 = rospy.Rate(0.15)  # 5s
        r2 = rospy.Rate(10)
        pos = position()
        # go forward            
        pos.x = hx
        pos.y = hy
        pos.z = hz  #-80
        self.pub1.publish(pos)
        r2.sleep()

        # stop pump
        #self.pub2.publish(0)
        #r2.sleep()
        #r1.sleep()
        #pos.x = 120
        #pos.y = 0
        #pos.z = 35
        self.pub1.publish(pos)
        #r1.sleep()
        return 'succeeded'
    def release_objectm(self):
        global hx
        global hy
        global hz
        hz = 170
        print('hz=',hz)  
        r1 = rospy.Rate(0.15)  # 5s
        r2 = rospy.Rate(10)
        pos = position()
        # go forward            
        pos.x = hx
        pos.y = hy
        pos.z = hz  #-80
        self.pub1.publish(pos)
        r2.sleep()

        # stop pump
        #self.pub2.publish(0)
        #r2.sleep()
        #r1.sleep()
        #pos.x = 120
        #pos.y = 0
        #pos.z = 35
        self.pub1.publish(pos)
        #r1.sleep()
        return 'succeeded'
    def release_objectv(self):
        global hx
        global hy
        global hz
        hx = 120
        hy = 0
        hz = 40
        print('hx=',hx)  
        print('hy=',hy)  
        print('hz=',hz)  
        r1 = rospy.Rate(0.15)  # 5s
        r2 = rospy.Rate(10)
        pos = position()
        # go forward            
        pos.x = hx
        pos.y = hy
        pos.z = hz  #-80
        self.pub1.publish(pos)
        r2.sleep()

        # stop pump
        #self.pub2.publish(0)
        #r2.sleep()
        #r1.sleep()
        #pos.x = 120
        #pos.y = 0
        #pos.z = 35
        self.pub1.publish(pos)
        #r1.sleep()
        return 'succeeded'
    def release_object11(self):
        global hx
        global hy
        global hz
        hx = 210
        hy = 0
        hz = -37
        print('hx=',hx)  
        print('hy=',hy)  
        print('hz=',hz)  
        r1 = rospy.Rate(0.9)  # 5s
        r2 = rospy.Rate(10)
        pos = position()
        # go forward            
        pos.x = hx
        pos.y = hy
        pos.z = hz  #-80
        self.pub1.publish(pos)
        r2.sleep()

        # stop pump
        #self.pub2.publish(0)
        #r2.sleep()
        #r1.sleep()
        #pos.x = 120
        #pos.y = 0
        #pos.z = 35
        self.pub1.publish(pos)
        #r1.sleep()
        return 'succeeded'
    def release_object22(self):
        global hx
        global hy
        global hz
        hx = 210
        hy = 0
        hz = 70
        print('hx=',hx)  
        print('hy=',hy)  
        print('hz=',hz)  
        r1 = rospy.Rate(0.9)  # 5s
        r2 = rospy.Rate(10)
        pos = position()
        # go forward            
        pos.x = hx
        pos.y = hy
        pos.z = hz  #-80
        self.pub1.publish(pos)
        r2.sleep()

        # stop pump
        #self.pub2.publish(0)
        #r2.sleep()
        #r1.sleep()
        #pos.x = 120
        #pos.y = 0
        #pos.z = 35
        self.pub1.publish(pos)
        #r1.sleep()
        return 'succeeded'
    def release_object33(self):
        global hx
        global hy
        global hz
        hx = 210
        hy = 0
        hz = 170
        print('hx=',hx)  
        print('hy=',hy)  
        print('hz=',hz)  
        r1 = rospy.Rate(0.9)  # 5s
        r2 = rospy.Rate(10)
        pos = position()
        # go forward            
        pos.x = hx
        pos.y = hy
        pos.z = hz  #-80
        self.pub1.publish(pos)
        r2.sleep()

        # stop pump
        #self.pub2.publish(0)
        #r2.sleep()
        #r1.sleep()
        #pos.x = 120
        #pos.y = 0
        #pos.z = 35
        self.pub1.publish(pos)
        #r1.sleep()
        return 'succeeded'
    def release_object44(self):
        global hx
        global hy
        global hz
        hx = 70
        hy = 270
        hz = -17
        print('hx=',hx)  
        print('hy=',hy)  
        print('hz=',hz)  
        r1 = rospy.Rate(0.9)  # 5s
        r2 = rospy.Rate(10)
        pos = position()
        # go forward            
        pos.x = hx
        pos.y = hy
        pos.z = hz  #-80
        self.pub1.publish(pos)
        r2.sleep()

        # stop pump
        #self.pub2.publish(0)
        #r2.sleep()
        #r1.sleep()
        #pos.x = 120
        #pos.y = 0
        #pos.z = 35
        self.pub1.publish(pos)
        #r1.sleep()
        return 'succeeded'       
    def release_object55(self):
        global hx
        global hy
        global hz
        hx = 90
        hy = -250
        hz = -27
        print('hx=',hx)  
        print('hy=',hy)  
        print('hz=',hz)  
        r1 = rospy.Rate(0.9)  # 5s
        r2 = rospy.Rate(10)
        pos = position()
        # go forward            
        pos.x = hx
        pos.y = hy
        pos.z = hz  #-80
        self.pub1.publish(pos)
        r2.sleep()

        # stop pump
        #self.pub2.publish(0)
        #r2.sleep()
        #r1.sleep()
        #pos.x = 120
        #pos.y = 0
        #pos.z = 35
        self.pub1.publish(pos)
        #r1.sleep()
        return 'succeeded'   
    # 转动机器人到一定角度       
    def turn_body(self):
        cmd_vel = Twist()
        cmd_vel.angular.z = 0.9
        rate = rospy.Rate(10)
        for i in range(40):            
            self.cmd_vel_pub.publish(cmd_vel)            
            rate.sleep()
       

        
if __name__ == '__main__':
    try:
        rospy.init_node('GraspObject', anonymous=False)
        rospy.loginfo("Init GraspObject main")   
        GraspObject()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("End spark GraspObject main")


