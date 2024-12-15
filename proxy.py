import sys
import socket
import threading

HEX_FILTER = ''.join(
    [(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)]
)

def hexdump(src, length=16, show=True):
    '''Takes some input as bytes or a string and
    returns a both the hexadecimal values and ASCII characters''' 
    if isinstance(src, bytes):
        src = src.decode
    results = list()
    for i in range(0, len(src), length):
        word = str(src[i:i+length])

        printable = word.translate(HEX_FILTER)
        hexa = ''.join([f'{ord(c):02X}' for c in word])
        hexwidth = length*3
        results.append(f'{i:04x}  {hexa:<{hexwidth}}  {printable}')
    if show:
        for line in results:
            print(line)
    else:
        return results
    
def receive_from(connection):
    buffer = b"" # empty byte string that will accumulate responses from the socket
    connection.settimeout(5) # This is a bit aggressive so adjust accordingly!
    try:
        while True: # Set up a loop to read data into the buffer until a time out or no more data
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
    except Exception as e:
        pass
    return buffer

def request_handler(buffer):
    '''Perform request packet modifications'''
    return buffer

def response_handler(buffer):
    '''Perform response packet modifications'''
    return buffer