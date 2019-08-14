# TranslinkDataCapBypasser
Short Bash &amp; Python scripts which, bypass the data cap on Translink NI services. (Linux only for now)

### Requirements:
---
* sudo / root access

* macchanger - [Tarball](http://mirrors.kernel.org/gnu/macchanger/) / "apt-get install macchanger" / "yum install macchanger"

* nmcli - [Tarball](http://www.linuxfromscratch.org/blfs/view/svn/basicnet/networkmanager.html) / "yum install NetworkManager" / "snap install network-manager" / "apt-get install network-manager"

* ifconfig - *should be installled on most Debian based systems* / "apt-get install net-tools" / "yum install net-tools"

* python (either 2/3) - already installed as part of Linux kernel

---
---

### How It Works:
---

* Turns off your wireless interface

* Spoofs your MAC address randomly to prevent your laptop being identified by the network (usage tied to this)

* Turns on your wireless interface

* Connects to Translink wifi

* Calls the python script to automate accepting terms &amp; conditions (prints response code: 200 means it worked)
