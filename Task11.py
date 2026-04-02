# from scapy.all import sniff, IP
# from collections import defaultdict
# from datetime import datetime

# Track IP activity
# ip_count = defaultdict(int)

# Threshold for suspicious activity
# THRESHOLD = 10

# def log_alert(ip):
#     with open("alerts.log", "a") as file:
#         file.write(f"[{datetime.now()}] Suspicious activity from {ip}\n")

# def detect_packet(packet):
    # if packet.haslayer(IP):
        # src_ip = packet[IP].src
        # ip_count[src_ip] += 1

        # Rule: too many packets from same IP
        # if ip_count[src_ip] > THRESHOLD:
            # print(f"[ALERT] Possible attack from {src_ip}")
            # log_alert(src_ip)

# def start_ids():
    # print("🔍 IDS is running... Press Ctrl+C to stop.")
    # sniff(prn=detect_packet, store=False)

# if __name__ == "__main__":
    # start_ids()