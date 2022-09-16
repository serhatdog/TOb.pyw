<p align="center">
  <img src="https://github.com/serhatdog/TOb.pyw/blob/main/banner.png?raw=true" alt="TOb.pyw Banner">
</p>

<p align="center"><b>Author: Serhat Dogan</b><p>
<p align="center"><b>Last update: 16.09.2022</b><p>
<p align="center"><b>Preparing...</b><p>

    #Creating a object
    
    #SETTINGS: Checks the folder and it deletes the files that didn't use since 26 Hours 30 Minutes 15 Seconds
    EXAMPLE_FOLDER = TOb(
        path = r'C:\Users\YourUsername\Desktop\TempFolder\\', #make sure you put double slash at the end 
        settings= {
            'd':1, 'h':2, 'm': 30, 's': 15
        }
    )

    #One-time cleaning after computer starts
    EXAMPLE_FOLDER.clear() #Checks only once when PC boots

    #Automated cleaning
    EXAMPLE_FOLDER.auto('m', 30) #Every 30 minutes script checks folder
    
    #You have to put .pyw file into your shell:startup location to start this script everytime when the PC boots
