# -*- coding: utf-8 -*-
"""
Created on wed Mar 05 10:36:32 2025

@authors: Martina Riva, Politecnico di Milano
"""


#add for Visual Studio: this allows the code to run even with hardware folders outside the 
#app folder
import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
print('here:', dirname(dirname(__file__)))


from ScopeFoundry import BaseMicroscopeApp

class hyper_app(BaseMicroscopeApp):
    
    name = 'hyper_app'
    
    def setup(self):
        
        #Add hardware components
        print("Adding Hardware Components")
         
        from Hamamatsu_ScopeFoundry.CameraHardware import HamamatsuHardware
        self.add_hardware(HamamatsuHardware(self))
        
        from PI_ScopeFoundry.PI_GCS_hardware import PI_GCS_HW
        self.add_hardware(PI_GCS_HW(self))

        
        # Add measurement components
        print("Create Measurement objects")
        from hyperspectral_measure import hyperMeasure
        self.add_measurement(hyperMeasure(self))

        #For ScopeFoundry release 2.0.2 comment these lines:
        #self.ui.show()
        #self.ui.activateWindow()

if __name__ == '__main__':
    
    import sys
    
    app = hyper_app(sys.argv)
    #app.settings_load_ini(".\\Settings\\settings.ini")
    for hc_name, hc in app.hardware.items():
        hc.settings['connected'] = True    # connect all the hardwares  
    
    
    sys.exit(app.exec_())