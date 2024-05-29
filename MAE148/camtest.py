#!/usr/bin/env python3

import depthai as dai
import cv2
import time


pipeline = dai.Pipeline()

monoLeft = pipeline.create(dai.node.MonoCamera)
apriltag = pipeline.create(dai.node.AprilTag)

xlinkout = pipeline.create(dai.node.XLinkOut)

xlinkout.setStreamName("camOut")


monoLeft.setCamera("left")
monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)

monoLeft.out.link(xlinkout.input)

with dai.Device(pipeline) as device:

        qLeft = device.getOutputQueue(name = "camOut", maxSize = 4, blocking = False)

        while True:
                inLeft = qLeft.tryGet()
                if inLeft is not None:
                        cv2.imshow("left",inLeft.getCvFrame())

                if cv2.waitKey(1) == ord('q'):
                        break
