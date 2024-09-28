
# Tiger Detection System

The Tiger Detection System is a project aimed at reducing human-wildlife conflict near the buffer zones of national parks by detecting tigers in real-time. This system employs advanced machine learning techniques to identify tiger presence in monitored areas, providing timely alerts to nearby communities and park authorities.

Installed cameras and IoT hardware systems placed on electric poles near the buffer zones will monitor tiger activity to serve the community. A red bulb on these poles will illuminate to alert community members walking on the road or foraging in the jungle for grass, wood, or other resources necessary for their livelihoods. Additionally, a buzzer will sound to enhance safety and awareness.

To support ongoing research and proactive wildlife management, the system will store detected data in a database. This data can be utilized in a web app to create heat maps that show tiger activity patterns, indicating the months when tigers are more active in specific areas. This information will aid in better understanding tiger behavior and help inform conservation strategies.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Acknowledgments](#acknowledgments)
- [Authors](#authors)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nischalneupanee/Nawata_Tiger_Alert_SYSTEM
   ```

2. Navigate to the project directory:
   ```bash
   cd Tiger-Detection-System
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:
   ```bash
   daphne -p 8000 test_django.asgi:application
   ```

2. The system identifies the tiger through live video. The cameras are generally placed in jungle areas (using already installed national park cameras).

3. The system generates an alert signal and sends it to IoT devices when a tiger is detected near the community.

Make sure to place the downloaded model in the appropriate directory (`models/`) before running the application.

## Technologies Used

1. **Python (Django)**: Backend framework used for managing the server-side logic and database.
2. **OpenCV**: Used for image processing and feeding live camera streams into the system.
3. **YOLOv8**: State-of-the-art real-time object detection algorithm used for identifying tigers.
4. **NodeMCU**: Microcontroller used to trigger IoT-based alerts via buzzer and light signals.
5. **Bootstrap, HTML, CSS, JS**: For building the frontend and web application.
6. **OpenStreetMap**: Provides map services for visualizing tiger activity on the web app.

## Features

1. **Real-time Tiger Detection**: Utilizes advanced object detection algorithms (YOLOv8) to accurately detect tigers in real-time through live video feeds from cameras installed in the jungle.
   
2. **Immediate Alerts**: The system sends a signal to IoT-enabled alert devices near buffer zones when a tiger is detected. These devices trigger an audible buzzer and a red bulb to notify nearby community members.

3. **Data Storage & Analysis**: Detected data is stored in a database, enabling research and analysis of tiger activity over time. The data can be visualized using heat maps that show patterns of tiger movements.

4. **Web App Integration**: A user-friendly web interface is integrated to allow researchers, conservationists, and park authorities to monitor tiger activity, access heat maps, and analyze trends.

5. **Community Safety**: The system helps prevent human-wildlife conflict by providing real-time alerts to community members in buffer zones, enhancing their safety when collecting resources from the jungle.

6. **Scalability**: The system can be expanded to monitor multiple areas and integrated with additional wildlife monitoring technologies for broader wildlife conservation efforts.

## Acknowledgments

1. **Open Source Communities**: Special thanks to the developers and maintainers of the open-source libraries and frameworks that made this project possible, including OpenCV, YOLOv8, Django, and OpenStreetMap.
2. **Researchers**: Acknowledgment goes to the researchers and machine learning experts who helped optimize the tiger detection algorithms.

## Authors

This project was developed by **Team NAWATA** as part of the **IDEAX Hackathon 2024**.

- **Nischal Neupane**
- **Ankit Devkota**
- **Madhav Poudel**

For any inquiries, feel free to reach out:

1. **Email**: contact@nischalneupane.name.np

