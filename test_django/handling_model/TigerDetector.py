import cv2
import requests
from ultralytics import YOLO
import numpy as np
import os
import base64
from django.utils import timezone  # For timezone-aware datetime
from datetime import timedelta

class TigerDetector:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Path to the model
        model_path = os.path.join(BASE_DIR, 'mlmodels', 'enhanced_tiger.pt')
        self.model=YOLO(model_path)
        self.confidence_threshold=0.78

    async def save_detection(self, location_id):
        from asgiref.sync import sync_to_async
        from .models import Location_of_camera, detected_database
        try:
            # ordered_entry = detected_database.objects.all().order_by('Detected_date')
            # last_entry = await sync_to_async(ordered_entry.objects.last)()
            ordered_entry = await sync_to_async(detected_database.objects.all().order_by)('-Detected_date')

            # Retrieve the last entry asynchronously
            last_entry = await sync_to_async(ordered_entry.last)()


            # If there's a last entry, calculate the time difference
            if last_entry is not None:
                current_time = timezone.now()
                time_difference = current_time - last_entry.Detected_date
                total_seconds = time_difference.total_seconds()
            else:
                total_seconds=9999999


            if total_seconds > 600:
                    try:
                        first_location = await sync_to_async(Location_of_camera.objects.get)(id=location_id)
                        detected_database_instance = detected_database(camera=first_location)
                        await sync_to_async(detected_database_instance.save)()
                    except Location_of_camera.DoesNotExist:
                        print("Camera location not found.")
                    except Exception as e:
                        print(f"Error saving detection: {e}")
        except Exception as e:
            print(e)


    def process_frame(self, frame,type):
        self.type=type
        results = self.model.predict(source=frame, show=False)

        for detection in results[0].boxes:
            score = float(detection.conf.cpu().numpy().item())
            print(score)

            if score > self.confidence_threshold:
                box = detection.xyxy[0].cpu().numpy().astype(int)
                # Fixed parentheses around .cpu()
                class_id = int(detection.cls.cpu().numpy().item())
                if class_id == 0:
                    response=requests.get('http://esp8266.local/alert')
                    print(response.status_code)
                    for char in range(15):
                        print("tiger detected")

                    if self.type == 'live':
                        import asyncio
                        asyncio.create_task(self.save_detection(location_id=1))


                    x_min, y_min, x_max, y_max = box
                    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
                    label = f"Tiger ({score:.2f})"
                    cv2.putText(frame, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        return frame