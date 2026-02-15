from flask import Flask
from flask_socketio import SocketIO, emit
from unitree_sdk2py.core.channel import ChannelFactoryInitialize
from unitree_sdk2py.g1.arm.g1_arm_action_client import G1ArmActionClient, action_map


INTERFACE = "lo" 
TIMEOUT = 5.0

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

ChannelFactoryInitialize(0, INTERFACE)
arm_client = G1ArmActionClient()
arm_client.Init()
arm_client.SetTimeout(TIMEOUT)


def run_arm_action(action_name):
    release_needed = [
            "shake hand", "high five", "hug",
            "heart", "right heart", "hands up",
            "x-ray", "right hand up", "reject"
        ]

    if action_name not in action_map:
        print(f"[ERROR] Unknown action: {action_name}")
        return 404

    print(f"[INFO] Running action: {action_name}")
    arm_client.ExecuteAction(action_map.get(action_name))

    if action_name in release_needed:
        arm_client.ExecuteAction(action_map.get("release arm"))

    return 0


@socketio.on("arm_action")
def handle_arm_action(json_data):
    action_name = json_data.get("action")
    if not action_name:
        print("[ERROR] No action")
        emit("action_response", {"status": "error", "message": "no action specified"})
        return

    emit("action_response", {"status": "running", "action": action_name})
    code = run_arm_action(action_name)
    if code == 0:
        emit("action_response", {"status": "finished", "action": action_name})
    elif code == 404:
        emit("action_response", {"status": "error", "message": "unknown action"})
    else:
        emit("action_response", {"status": "error", "message": "unknown error"})


if __name__ == "__main__":
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    print("[INFO] WebSocket server running on port 5000")
    socketio.run(app, host="0.0.0.0", port=5000)
