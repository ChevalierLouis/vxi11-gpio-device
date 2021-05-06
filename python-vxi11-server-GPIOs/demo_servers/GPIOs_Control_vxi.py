import sys
import os
import signal
import time
import logging

sys.path.append(os.path.abspath('..'))
import vxi11_server as Vxi11

def signal_handler(signal, frame):
    logger.info('Handling Ctrl+C!')
    instr_server.close()
    sys.exit(0)
                                        
class TimeDevice(Vxi11.InstrumentDevice):

    def device_init(self):
        print('TimeDevice: device_init()')
        return

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C to exit')
    logger.info('starting time_device')
    
    # create a server, attach a device, and start a thread to listen for requests
    instr_server = Vxi11.InstrumentServer()
    #name = 'TIME'
    name = 'inst1'
    instr_server.add_device_handler(TimeDevice, name)
    instr_server.listen()
    

    # sleep (or do foreground work) while the Instrument threads do their job
    while True:
        time.sleep(1)

        
