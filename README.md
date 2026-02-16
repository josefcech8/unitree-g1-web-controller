# Unitree G1 Web Controller
Web-based high-level control interface for the Unitree G1 robotic arms.

## Dependencies
- Python >= 3.8
- cyclonedds == 0.10.2
- numpy
- opencv-python
- Flask
- Flask-SocketIO
- [unitree_sdk2_python](https://github.com/unitreerobotics/unitree_sdk2_python/tree/master)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/josefcech8/unitree-g1-web-controller.git
cd unitree-g1-web-controller
```
2. Create and activate a Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Run the server:
```bash
python3 unitree_control_server.py <networkInterface>
```
2. Open [templates/index.html](./templates/index.html) in your browser.
