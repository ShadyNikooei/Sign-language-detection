import subprocess
import webbrowser

def run_action(action_type, value):
    try:
        if action_type == "app":
            subprocess.Popen([value])
        elif action_type == "url":
            webbrowser.open(value)
        elif action_type == "file":
            subprocess.Popen(["xdg-open", value])
        elif action_type == "folder":
            subprocess.Popen(["xdg-open", value])
        elif action_type == "audio":
            subprocess.Popen(["xdg-open", value])
        elif action_type == "cmd":
            subprocess.Popen(value, shell=True)
        elif action_type == "message":
            print(value)
        else:
            print(f"Unknown action type: {action_type}")
    except Exception as e:
        print(f"Error executing action: {e}")