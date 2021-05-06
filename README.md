# barebones-vxi11-gpio-device
 In this project I would like to control the gpios of a Raspberry Pi with vxi11 in a graphical interface with radio buttons. I use python.
 
 
With requests https://dridk.me/python-requests.html module, the graphics part is managed with tkinter.
 
 To run this project you have to put on the Raspberry:

          ├── code 
          │  ├── Raspberrypicode.py
          │  ├── templates
          │  │ ├── index.html(HTML and CSS)



 
On another machine (or the same) you can put the code of the graphical interface GUI.py but you can also run it on a web browser,mark the ip_address_of_the_raspberry_pi:8000

To know your IP address open a terminal and write this command

    $ hostname -I
    
With the GUI you need to change the ip address in the code or in the entry text bar on the top left 
    
    
  With vxi11 https://pypi.org/project/python-vxi11/ module, the graphics part is managed with tkinter.
 
 To run this project you have to put on the Raspberry:



          ├── python-vxi11-server-GPIOs 
          │  ├── demo_serveur
          │  │  ├── demo_serveur
          │  │  │   ├── srq-device.py
          │  │  │   ├── GPIOs_control_vxi.py
          │  │  ├── vxi11_serveur
          │  │  │   ├── _pycashe_
          │  │  │   ├── _init_.py   
          │  │  │   ├── instrument_device.py
          │  │  │   ├── instrument_serveur.py
          │  │  │   ├── rpc.py
          │  │  │   ├── vxi11.py
          
          
          
You just need to run GPIOs_control_vxi.py in demo server 

To change GPIOs pin go in instrument_device.py and do some changes line 36 to 43 in the dictionary(don't forget to create some states below ligne 43) 

 
On another machine (or the same) you can put the code of the graphical interface vxiclientgui.py just change the ip address in the code line 5

To know your IP address open a terminal and write this command
    $ hostname -I
    


