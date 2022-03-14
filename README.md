# EXTRACTING MUSIC DATA USING FROM SPOTIFY'S API
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

## Run Python Script
 - Clone project.
    ```bash
    git clone https://github.com/Marvellous-Chimaraoke/spotify-music-data.git
    ```
 - Open project folder in text editor (VSCode, Atom, etc).
 - Create virtual environment using terminal.
    ```bash
    python3 -m venv env
    ```

