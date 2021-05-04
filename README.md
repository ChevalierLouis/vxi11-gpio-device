# barebones-vxi11-gpio-device
 In this project I would like to control the gpios of a Raspberry Pi with vxi11 in a graphical interface with radio buttons. I use python. For the moment I use the requests https://dridk.me/python-requests.html module, the graphics part is managed with tkinter.
 
 To run this project you have to put on the Raspberry:

          ├── code 
          │  ├── Raspberrypicode.py
          │  ├── templates
          │  │ ├── index.html(HTML and CSS)



 
On another machine (or the same) you can put the code of the graphical interface GUI.py but you can also run it on a web browser,mark the ip_address_of_the_raspberry_pi:8000

To know your IP address open a terminal and write this command

    $ hostname -I
