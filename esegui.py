import threading
import subprocess

def run_script(script_path):
    subprocess.call(["python2", script_path])

def run_script3(script_path):
    subprocess.call(["python3", script_path])

if __name__ == "__main__":
    script1_path = "Azioni.py"
    script2_path = "App.py"

    thread1 = threading.Thread(target=run_script3, args=(script2_path,))
    thread2 = threading.Thread(target=run_script, args=(script1_path,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
