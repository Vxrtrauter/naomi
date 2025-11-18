from data.state import naomi



def get_target(cmd):
    try:
        global target
        target = cmd.replace("select ", "")
        target = int(target)
        connection = naomi.connections[target]
        print(f"[i] Connected to {str(naomi.addresses[target][0])}")
        print(str(naomi.addresses[target][0]) + ">", end="")
        return connection

    except:
        print("[!] Invalid Selection")
        return None

def send_target_commands(connection):
    while True:
        try:
            cmd = input()

            if cmd == "exit":
                break


            # use str.encode to convert string to bytes
            if len(str.encode(cmd)) > 0: # check if command is not null
                connection.send(str.encode(cmd))

                client_response = connection.recv(20480).decode("utf-8") # 1024 = bytes to read at once, utf-8 = encoding type
                print(f"({naomi.addresses[target][0]}) " + client_response, end="")
        except:
            print("[!] Error sending commands")
            break