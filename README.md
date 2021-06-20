# server-multichat
Description:
 The chat server is initially simplistic, which takes into account a simultaneous connection of several clients.
 
  Specification:
        Communication between clients.

 How to use it ?
    A version of python 3.x is required (download it here: https://www.python.org/downloads/)

    clone the repository with the command below git clone https://github.com/WonderAwa/server-tftp.git

    use the command ./tftp-server.py in a terminal to run the project and in another window of the terminal use this command netcat localhost 7777
 
With specifications:
    -The client once connected to the server must specify his nickname by typing the command 'NICK' followed by the chosen nickname.
    -If a client wishes to write a message he will have to specify 'MSG' before writing his message.
    -To quit the chat, the customer must precede their goodbye message with the command 'QUIT'
    -A client can disconnect another if he considers it rude by using the command 'KILL' followed by the pseudonym of the target and the targeted message.
    -And finally we can consult the list of connected clients using the 'WHO' command.

