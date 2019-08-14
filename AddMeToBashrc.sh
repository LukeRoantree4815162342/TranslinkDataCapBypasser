# Copy this function to your $HOME/.bashrc file, as well as the export line afterwards

# Change 'wlp3s0' to your wireless interface (probably wlan0 if not this)

# If possible, change $(locate Translink_confirm.py) to a hardcoded path
# to the other file in this directory

function bypass_translink() {
  	sudo ifconfig wlp3s0 down
  	sudo macchanger -r wlp3s0
  	sudo ifconfig wlp3s0 up
  	nmcli d wifi connect "TranslinkWiFi"
	python $(locate Translink_confirm.py)
  	fi 
  }

export -f bypass_translink
