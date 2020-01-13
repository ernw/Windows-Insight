# Windows Telemetry ETW Monitor: Windbg Framework

This folder ("windbg_fmw") stores the implementation of the Windbg Framework, a part of the Windows Telemetry ETW Monitor. The Windbg Framework is a set of scripts for monitoring Windows Telemetry ETW activities (i.e., Windows ETW activities for providing data to Windows Telemetry - visit [this link](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Cyber-Sicherheit/SiSyPHus/Workpackage4_Telemetry.pdf?__blob=publicationFile&v=4) for more information). The output produced by the scripts can be fed to the Telemetry Information Visualization framework (also part of the Windows Telemetry ETW Monitor) for visualization of information and statistics.

The scripts for monitoring Windows Telemetry ETW activities are fed to a running windbg instance, connected to the Windows instance whose Windows Telemetry ETW activities are monitored (i.e., the monitored Windows instance).

The scripts comprising the Windbg Framework are stored in the "scripts" folder.

There are more elegant ways to monitor Windows Telemetry ETW activities than the deployment of a set of windbg scripts. We focus on the windbg alternative because:

* it allows for a first-hand, kernel-level insight into the system's ETW activities for providing data to Windows Telemetry. This is useful for extracting information that can be accessed only at kernel-level;
* being script-based, it allows for others to modify or extend the scripts comprising the Windbg Framework in order to extract any kernel-specific information of interest. 

## Technology domain

The Windbg Framework has been tested on Windows 10, version 1909. 

## Usage guidelines

**Important note**: Do not change the filenames of the scripts stored in the "scripts" folder.

In order to automate and centralize the use of the windbg scripts comprising the Windbg Framework, we developed a Python script that generates a master windbg script. This script is named "start_script.txt".

The master script deploys the set of windbg scripts stored in the "scripts" folder and is the central engine of the Windbg Framework.

The Python script that generates the master windbg script is stored in the file named "windbg_start_script_builder.py".
    
In order to use the Windbg Framework:

1. Place the "windbg_fmw" folder in the filesystem of the platform from which you monitor Windows Telemetry ETW activities, for example, "C:\Users\TestUser\foo\windbg_fmw"
2. Execute the Python script "windbg_start_script_builder.py", providing the path to the folder where the "scripts" folder is placed (parameter -f) and the path at which the newly generated master windbg script ("start_script.txt") is to be stored (parameter -o):
```
python windbg_start_script_builder.py -f "C:\\Users\\TestUser\\foo\\windbg_fmw\\scripts" -o "C:\\Users\\TestUser"
```
3. Start the master windbg script ("start_script.txt") - once generated, the master windbg script can be fed to a running windbg instance, connected to the monitored Windows instance
```windbg
.logopen C:\\Users\\TestUser\\log.txt
$$><"C:\Users\TestUser\start_script.txt"
```

**Important note**: By default, the master windbg script ("start_script.txt") outputs data to the screen. In order for the data to be visualized by the Telemetry Information Visualization framework, the output of the master windbg script ("start_script.txt") should be logged to a file ("log.txt" in the above example). This file is fed to the Telemetry Information Visualization framework for visualization of information and statistics. 


## Credits

**Pablo Artuso**
 
⋅⋅⋅ Main contributor

⋅⋅⋅ Email: artusopablo@gmail.com

⋅⋅⋅ Twitter account: [@lmkalg](https://twitter.com/lmkalg)

**Aleksandar Milenkoski** 

⋅⋅⋅ Supervisor and contributor

⋅⋅⋅ Email: amilenkoski@ernw.de

⋅⋅⋅ Twitter account: [@milenkowski](https://twitter.com/milenkowski)


