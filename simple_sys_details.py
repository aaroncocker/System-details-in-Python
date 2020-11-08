#!/usr/bin/python3

# import packages and throw an exception should they not be installed 

try:
    import ipaddress
    import socket
    import uuid
    import binascii
    import psutil
    import platform
    import shutil
    
except:
    print("Error! Unable to find needed Python 3 packages on your system.")

def ram_usage():
    
    # calculate total memory and return in 'GB' format
    
    total_memory = str(psutil.virtual_memory().total)
    slice_object1 = slice(1) 
    total_memory_GB = total_memory[slice_object1] 
    
    # calculate memory in use and return in 'GB' format
    
    used_memory = str(psutil.virtual_memory().available)
    slice_object2 = slice(1) 
    used_memory_GB = used_memory[slice_object2]

    # calculate memory in use percentage

    RAM_usage_percent = psutil.virtual_memory().percent

    # print memory in use in GB and percentage

    print("Current memory usage:",int(total_memory_GB) - int(used_memory_GB), "/", total_memory_GB,"GB or",RAM_usage_percent,"%")

def cpu_usage():
    
    # print cpu usage percentage
    
    print("Current CPU usage:",psutil.cpu_percent(),"%")
      
def mac_address():
    
    # open socket connection 
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
   
    # extract MAC address from operating system as hex value and convert to string and assign IP address to variable
    
    mac_address = hex(uuid.getnode())
    mac_address = str(mac_address)
   
    # close socket connection
    
    s.close()
   
    # partition mac address into pairs and insert a colon to format as a human readable MAC address
    
    formatted_mac_address = [mac_address[i:i+2] for i in range(0, len(mac_address), 2)]
    
    # print MAC address 
    
    print("Your MAC address is",':'.join(formatted_mac_address))

def ip_address():
    
    # open socket connection 
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
   
    # close socket connection
    
    s.close()
    
    # determine whether IP address is IPv 4 or IPv 6
    ip_network_type = ipaddress.ip_address(ip_address).version
    
    # print out IP address and type either IPv 4 or IPv 6
    
    print("Your IP address is",ip_address,"and you have an IPv",ip_network_type,"network address")
    
def operating_system():
    print("You are using the",platform.system(),"operating system and your kernel is",platform.release())
    
def processor_type():
    
    #print CPU information
    
    print("Your processor is: ",platform.processor())
    
def hard_disk_storage():
    
    # calculate and print total, free and remaining storage
    
    total, used, free = shutil.disk_usage("/")
    
    print("Your disk size is: %d GiB" % (total // (2**30)))
    print("You are currently using: %d GiB" % (used // (2**30)))
    print("Your remaining free storage is: %d GiB" % (free // (2**30)))

def main():
    
    print("Your system details")
    print("")
    operating_system()
    processor_type()
    print("")
    hard_disk_storage()
    ram_usage()
    cpu_usage()
    print("")
    mac_address()
    ip_address()    

# run main program subroutine  
main()
