import socket
import threading
import time

FLAG = "BSides{Fl4g5_J4CKP0T_ATM_C0mpR0m1s3d}"

def handle_connection(client_socket, address):
    print(f"[+] Connection from {address}")
    client_socket.send(b"=== IRONVAULT ATM MANAGEMENT INTERFACE ===\n")
    client_socket.send(b"WARNING: UNAUTHORIZED ACCESS STRICTLY PROHIBITED.\n")
    
    try:
        while True:
            client_socket.send(b"\nENTER 4-DIGIT MAINTENANCE PIN: ")
            
            # Read up to 1024 bytes to allow the attacker to send a large payload
            data = client_socket.recv(1024).decode('utf-8').strip()
            
            if not data:
                break
            
            # The Simulated "Buffer Overflow" Vulnerability
            if len(data) > 64:
                # The attacker sent too much data! Simulate a crash and memory dump.
                client_socket.send(b"\n[!] FATAL ERROR: Buffer limit exceeded at 0x00A4F8B0\n")
                client_socket.send(b"[!] Dumping core memory registers...\n\n")
                time.sleep(1) # Add a slight delay for dramatic effect
                
                # Dump fake hex values hiding the flag
                client_socket.send(b"EAX: 0x00000000\n")
                client_socket.send(b"EBX: 0x41414141\n")
                client_socket.send(f"ESP: {FLAG}\n".encode('utf-8'))
                client_socket.send(b"EIP: 0x41414141 (SEGMENTATION FAULT)\n")
                client_socket.send(b"\nSYSTEM HALTED. DISPENSING CASH VAULT RECOVERY LOGS...\n")
                
                client_socket.close()
                break
                
            elif len(data) == 4 and data.isdigit():
                client_socket.send(b"[-] ACCESS DENIED: Invalid PIN.\n")
            else:
                client_socket.send(b"[-] ERROR: Input must be exactly 4 digits.\n")
                
    except Exception as e:
        print(f"[-] Error handling {address}: {e}")
    finally:
        client_socket.close()

def start_atm_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Allow port reuse so it doesn't crash if restarted quickly
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server.bind(('0.0.0.0', 3333))
    server.listen(5)
    print("[*] Simulated ATM Listening on 0.0.0.0:3333...")
    
    while True:
        client_sock, addr = server.accept()
        client_handler = threading.Thread(target=handle_connection, args=(client_sock, addr))
        client_handler.start()

if __name__ == '__main__':
    start_atm_server()
