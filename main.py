# import threading
# from Development.netprotocol import NetworkProtocols

# c1 = NetworkProtocols('Cisco', 'Juniper', 'Arista')
# j1 = NetworkProtocols('Cisco', 'Juniper', 'Arista')
# a1 = NetworkProtocols('Cisco', 'Juniper', 'Arista')

# t1 = threading.Thread(target=c1.cisco_router, name='c1')
# t2 = threading.Thread(target=j1.juniper_router, name='j1')
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# c1.cisco_router()

# j1.juniper_router()

# a1.arist_router()


with open('ipaddress.txt', 'r') as rd:
  r = rd.read()
  print(r)

  class Vehicle:
    parts = []
  v1,v2 = Vehicle(), Vehicle()
  v1.parts.append(5)
  print(v2.parts)

  class Vehicle:
    def __init__(self):
      self.parts=[]
  v1,v2 = Vehicle(), Vehicle()
  v1.parts.append(5)
  print(v2.parts)
