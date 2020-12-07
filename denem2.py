from pathlib import Path
home = str(Path.home())
baglantilar = dict() # Goal 1

with open(home+'/.ssh/config','r') as f:    
    for line in f: # Goal 2 
        if 'Host ' in line: # Goal 3
            if line != '\n':
                
                (key,value) = line.split()
                hostline = value
                baglantilar[hostline] = dict() # Goal 3
                baglantilar[hostline][key] = value # Goal 5

            else:
                continue
            
        else: # Goal 4
            if line != '\n':
                (key,value) = line.split() 
                baglantilar[hostline][key] = value
           
            else:
                continue
    deneme = dict()
   

    print(baglantilar.items()) # Goal 
    baglantilar['proxmos2'] = {'Host' : 'New Host', 'Hostname' : '192.168.2.1' , 'User' : 'Deneme_User'}
    print('----------------------------------------------')
    baglantilar['proxmos2']['Deneme'] = 'Deniyoz'
    print('----------------------------------------------')
    print(baglantilar.items())
