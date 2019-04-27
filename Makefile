install:
	sudo apt install python3-pip
	sudo -H pip install -U pipenv  # Install onto global Python interpreter
	sudo apt install python3-tk  # Ensure tkinter installed on base ubuntu python3
	pipenv install  # Install project requirements
