import psutil
from pypresence import Presence
import time
import os

client_id = '1295805537098928178'

details = [
    "Analyzing network...",
    "Scanning for vulnerabilities...",
    "Gathering network data...",
    "Performing network discovery...",
    "Assessing network security...",
    "Mapping network devices...",
    "Zenmap RPC by github.com/sakusql"
]

def process_en_cours(process):
    for proc in psutil.process_iter(['name']):
        if process.lower() in proc.info['name'].lower():
            return True
    return False

def activer_rpc():
    RPC = Presence(client_id)
    RPC.connect()
    RPC.update(state="Scanning Network", details=details[0], large_image="zenmap_logo", large_text="Zenmap")
    return RPC

def temps(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02}:{seconds:02}"

def maj_rpc(RPC, index, temps_écoulé):
    timer = temps(temps_écoulé)
    RPC.update(state=f"Scanning Network: {timer}", details=details[index % len(details)], large_image="zenmap_logo", large_text="Zenmap")

def desactiver_rpc(RPC):
    if RPC:
        RPC.clear()

if __name__ == "__main__":
    os.system("title Zenmap RPC by saku")
    process= "pythonw"
    RPC = None
    rpc_active = False
    detail_index = 0
    start_time = None

    while True:
        if process_en_cours(process):
            if not rpc_active:
                RPC = activer_rpc()
                rpc_active = True
                start_time = time.time()

            elapsed_time = time.time() - start_time
            maj_rpc(RPC, detail_index, elapsed_time)
            detail_index += 1
        else:
            if rpc_active:
                desactiver_rpc(RPC)
                rpc_active = False
        
        time.sleep(5)
