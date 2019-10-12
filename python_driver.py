#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Supported instruments (identified):
- 
"""

import numpy as np
import visa
    

class Driver():
    
    category = 'Optical shutter'
    
    def __init__(self,address='ASRL::2::INSTR'):
        
        # Instantiation
        rm = visa.ResourceManager()
        self.inst = rm.open_resource(address)
        self.inst.timeout = 5000 #ms
        self.inst.baud_rate = 115200 

        
        # Angle configuration : 1=Closed  0=Open
        self.POS = {1:{1:30,0:60},
                    2:{1:125,0:85},
                    3:{1:25,0:70}}
        
        self.config = '111' # default position ALL closed


    def close(self):
        try : self.inst.close()
        except : pass

    def query(self,command):

        result = self.inst.query(command)
        result = result.strip('\n')
        
        if '=' in result : result = result.split('=')[1]
        
        try : result = float(result)
        except: pass
    
        return result
    
    def write(self,command):
        self.inst.write(command)
        


    def getID(self):
        return self.query('ID?')
    


    def setSafeState(self):
        self.setConfig('111')
        if self.getConfig() == '111' :
            return True
        
        
        
    def setConfig(self,value):
        assert isinstance(value,str)
        assert len(value) == 3
        
        command = ''
        for i in range(3):
            try :
                servoID = i+1
                position = self.POS[servoID][int(value[i])]
                command+=f'SRV{servoID}={position},'
            except :
                pass

        self.query(command)

        self.config = value
        
    
    def getConfig(self):
        return self.config
    
    
 
    def invertConfig(self):
        newConfig = ''
        for i in range(3):
            try :
                newConfig += str(int(not bool(int(self.config[i]))))
            except :
                newConfig += 'x'

        self.setConfig(newConfig)
        
      
        
    def setAngleShutter1(self,value):
        self.query(f'SRV1={value}')
        
    def setAngleShutter2(self,value):
        self.query(f'SRV2={value}')
        
    def setAngleShutter3(self,value):
        self.query(f'SRV3={value}')
        
        
    def setShutter1(self,value):
        self.setConfig(f'{int(value)}xx')
        
    def setShutter2(self,value):
        self.setConfig(f'x{int(value)}x')
        
    def setShutter3(self,value):
        self.setConfig(f'xx{int(value)}')
        
        
    def getShutter1(self):
        return bool(int(self.config[0]))
    
    def getShutter2(self):
        return bool(int(self.config[1]))
    
    def getShutter3(self):
        return bool(int(self.config[2]))
    
    
       
    
    def danse(self):
        mess = ''
        for i in range(6) :
            for j in range(1,4) :
                mess += f'SRV{j}={round(np.random.random()*180)},'
        self.inst.timeout = 10000
        self.query(mess)
        self.inst.timeout = 5000
  
    