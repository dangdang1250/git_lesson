## Learn from OnlinePLC
Studio 5000 emulator (software) : can create a virtual Chassis
Check version, Studio 5000's software needs to match Firmware's version

Rslogix 5000
version 20 and below

Studio 5000
version 21 and above

When you "Add new Moudle" check version...and Slot
Module Type (Check Studio 5000)
- Analog
- Digital
- Driver
- Communication
- Controller
- Specialty 

## How to set Produce and Consumed Tags
理解，一個controller把數據傳輸給另外的controllers
produces(broadcase) and consumes(receive) system-shared tags.

| Term | Definition |
| ---- | ---------- |
| Produced tag | A tag that a controller makes available for use by other controllers. Multiple controllers can simulataneously consume(receive) the data. A produced tag sends its data to one or more consumed tags(consumers) without using logic.|
| Consumed tag | A tag that receives the data of a produced tag. The data type of consumed tag must match the data type(including any array dimensions) of the produced tag. The RPI of the consumed tag determines the period at which the data updates. |

For two controllers to share produced or consumed tags, both controllers must be in the same backplane or attachedc to the same control network.

https://literature.rockwellautomation.com/idc/groups/literature/documents/pm/1756-pm011_-en-p.pdf

https://literature.rockwellautomation.com/idc/groups/literature/documents/pm/1756-pm004_-en-p.pdf

https://literature.rockwellautomation.com/idc/groups/literature/documents/pm/1756-pm010_-en-p.pdf
RPI: Reqested packet interval 
NUT: Network update time

PLC: Programmable Logic Controller
PAC: Programmable Automation Controller

TON: Timer on Delay
TOF: Timer off Delay
RTO: Retentive Timer On
Ladder Language