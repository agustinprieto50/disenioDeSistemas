from factory import *


def main():
    for factory in (ChinaFactory(), CaliforniaFactory()):
        mac = factory.create_mac()
        win = factory.create_win()
        mac.mac_so()
        win.win_so()
        print(mac)
        print(win)
        
    
if __name__ == '__main__':
    main()

