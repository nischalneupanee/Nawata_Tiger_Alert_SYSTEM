import json,os
from channels.generic.websocket import AsyncWebsocketConsumer
import cv2
import asyncio
import base64
from .TigerDetector import TigerDetector
import logging
logging.basicConfig(level=logging.INFO)
from django.conf import settings


class WebcamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.tiger_detector = TigerDetector()

        self.camera = cv2.VideoCapture(0)
        asyncio.create_task(self.process_frames())

    async def disconnect(self, close_code):
        self.camera.release()

    async def process_frames(self):
        while True:
            ret, frame = self.camera.read()
            if not ret:
                break

            self.type='live'
            processed_frame = self.tiger_detector.process_frame(frame,self.type)

            _, buffer = cv2.imencode('.jpg', processed_frame)
            frame_base64 = base64.b64encode(buffer).decode('utf-8')

            await self.send(json.dumps({
                'frame': frame_base64,
            }))

            await asyncio.sleep(0.033)  # ~30 fps


class VideoDemoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.tiger_detector = TigerDetector()

        # Open the video file instead of the webcam
        self.video_file = 'tiger.mp4'
        self.video_capture = cv2.VideoCapture(self.video_file)
        if not self.video_capture.isOpened():
            logging.error("Unable to open video file")
            await self.close()
            return

        asyncio.create_task(self.process_frames())

    async def disconnect(self, close_code):
        self.video_capture.release()
        logging.info("Video demo connection closed")

    async def process_frames(self):
        while True:
            ret, frame = self.video_capture.read()
            if not ret:
                logging.info("End of video stream")
                break  # End of video

            # Process the frame with your tiger detector
            self.type='video'
            processed_frame = self.tiger_detector.process_frame(frame,self.type)

            # Encode the frame as JPEG
            _, buffer = cv2.imencode('.jpg', processed_frame)
            frame_base64 = base64.b64encode(buffer).decode('utf-8')

            # Send the processed frame to the WebSocket
            await self.send(json.dumps({
                'frame': frame_base64,
            }))

            await asyncio.sleep(0.033)  # ~30 fps

        # When done, close the connection
        await self.close()
