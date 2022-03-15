# EXTRACTING MUSIC DATA USING SPOTIFY'S API
This simple python script allows one to extract some specific data from the spotify API and save the extracted data to a `.txt` file in a more readable format.

It makes use of the [spotipy](https://spotipy.readthedocs.io/en/2.19.0/) python package and demonstrates how data can be extracted from the spotify API with user authentication and without user authentication. 

## Before running the python script
 - Make sure to have [python 3.10](https://www.python.org/downloads/) installed on your local mahcine.
 - Create a [spotify account](https://www.spotify.com/signup/). You'll need some important credentials from your spotify developer account for this to work smoothly.
 - Login to your [spotify developer account](https://developer.spotify.com/dashboard/).
    - Create a developer app with the help of this [guide](https://www.newline.co/courses/build-a-spotify-connected-app/getting-started-with-the-spotify-developer-dashboard).

### Using your app credentials as environment variables
After creating an app in your spotify developer account, There are some credentials you'll need to take note of:
 - Client ID
 - Client Secret 

These two credentials are vital and should be added to this script as environment variables. Learn how to set environment variables for python projects using this [guide](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1).
   - Take note that your environment variables should be named `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET` respectively.

You'll also need to add a redirection URI to your spotify app. To do this, Simply log in, find your app and click "Edit Settings" in the top right section. Under redirect URIs you add ```http://localhost:8080/callback``` and remember to click save in the bottom.

## Run Python Script
 - Clone project.
    ```bash
    git clone https://github.com/Marvellous-Chimaraoke/spotify-music-data.git
    ```
 - Open project folder in text editor (VSCode, Atom, etc).
 - Create virtual environment using terminal.
    ```bash
    python3.10 -m venv env
    ```
 - Activate virtual environment (MacOS/Linux/Git Bash).
   ```bash
   source env/bin/activate
   ```
 - Activate virtual environment (Windows).
   ```powershell
   env/bin/activate.ps1 (powershell)
   env/bin/activate.bat (command prompt)
   ```
 - Install all required packages.
   ```bash
   pip3 install -r requirements.txt
   ```
 - Run python script.
   ```bash
   python3.10 extract.py
   ```
- A browser window will open up. Copy the URL of the page that opened and paste in terminal then hit the `enter` button but not too hard... pity your keyboard :)
