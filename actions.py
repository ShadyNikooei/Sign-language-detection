import json
from utils import run_action

def load_actions(config_path="config.json"):
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Failed to load config: {e}")
        return {}

def perform_action(sign, action_map):
    action = action_map.get(sign)
    if not action:
        print(f"No action defined for sign: {sign}")
        return
    action_type = action.get("type")
    value = action.get("value")
    run_action(action_type, value)