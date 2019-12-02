# Ada-Lovelace

Ada-Lovelace 2019 : 24th and 25th October. 

Thank you for your interest in our event, we really appreciate the feedback you gave us at the time

Please do the following steps to get the notebooks running and try your hand at the code yourself!


A. For windows users - 

1. Install pip - Download the python file from this [url](https://bootstrap.pypa.io/get-pip.py) to your Desktop. Then, open your terminal change your current directory to the Destop directory. Then type in the command - `python get-pip.py`. Done, pip is installed on your computer!

2. Install spatialindex - Open your terminal and copy paste the following command - `sudo apt install libspatialindex-dev`. 
			  It might prompt you to enter the user ID and password of your computer
3. Install pipenv - Then do `pip3 install pipenv`. If this doesn't work, try - `pip install pipenv`
4. Navigate to this project in your terminal - Then type in the following command - `pipenv install`
					     - Then type the command - `pipenv shell`
					     - Then type the command - `jupyter noteebook`


B. For MacOS users - 

1. Install homebrew - Open your terminal and copy paste the following command - `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
2. Install pip - `brew install python3`
3. Install spatialindex - `brew install spatialindex` and  `pip3 install rtree`
4. Install pipenv - `pip3 install pipenv`
5. Navigate to this project in your terminal - Then type in the following command - `pipenv install`
                                             - Then execute `pipenv shell`
                                             - Then execute `jupyter noteebook`			

The above steps are only for the initial set up. The next time you want to reopen the project, simply navigate to the folder in your terminal
And then type - `pipenv shell` and `jupyter notebook`. 
This will open up a tab in your browser where you can access and explore the notebooks
