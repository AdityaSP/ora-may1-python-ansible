def ip_len(ip):
    ip_li = ip.split('.')
    if len(ip_li) != 4:
        print("Wrong length")
        exit(-1)
    
def range_check(part):
    if not 0 <= int(part) <=255:
        print("Wrong range")
        exit(-1)
        
ip= input("Enter the ip address: ")

ip_len(ip)
for part in ip.split('.'):
    range_check(part)

print("Good IP")    