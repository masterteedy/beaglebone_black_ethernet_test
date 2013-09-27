from datetime import datetime
from time import sleep

import dlipower
import paramiko

BB_IP = '192.168.30.19'
BB_USER = 'debian'
BB_PASSWORD = 'temppwd'

POWER_IP = '192.168.30.50'
POWER_USER = 'admin'
POWER_PASSWORD = '1234'
POWER_PORT = 6

def main():
    ps = dlipower.PowerSwitch(userid=POWER_USER, password=POWER_PASSWORD, hostname=POWER_IP)
    n_runs = 0
    
    # Run until ethernet fails
    while True:
        # Cycle power
        ps.cycle(POWER_PORT)
        # Wait a minute for the board to boot
        sleep(60)

        # Try SSHing in
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(BB_IP, username=BB_USER, password=BB_PASSWORD)
        except Exception as e:
            print e
            print 'Ethernet failed!', datetime.now()
            break

        # If there was no exception, SSH was successful
        n_runs += 1
        print 'Test passed.', datetime.now(), n_runs

if __name__ == '__main__':
    main()
