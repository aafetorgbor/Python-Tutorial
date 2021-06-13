import threading, os

class NetworkProtocols:

  def __init__(self, iosxe, junos, arista):
    self.iosxe = iosxe
    self.junos = junos
    self.arista = arista

  def cisco_router(self):
    print('Current threading is: ', threading.current_thread().name)
    print('Current running process ID is: ', os.getpid())
    print('IOS-XE is: ', self.iosxe)

  def juniper_router(self):
    print('Current threading is: ', threading.current_thread().name)
    print('Current running process ID is: ', os.getpid())
    print('JUNOS is: ', self.junos)
  
  def arist_router(self):
    print('EOS is: ', self.arista)

# if __name__ == '__main__':
#   c = NetworkProtocols()
#   j = NetworkProtocols()
#   a = NetworkProtocols()
