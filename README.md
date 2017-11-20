# Disting File Assistant

The Disting File Assistant is a Python script for generating additional files (playlists) for the Expert Sleepers MK3 / MK4 modules.
Currently it can generate audio, MIDI and wavetable playlists.

----

## Requirements

- Python 3
- [EasyGUI library](http://easygui.sourceforge.net)

----	
	
## How to Use

Download or clone the repo, open the terminal and enter the following command to run the Python script:

``` python3 /path/to/folder/disting.py ```

The script will then ask you to select an operation and will prompt you to select the path to your MicroSD card.  
All relevant files (.wav for Audio / Wavetable and .mid for MIDI) will be added the playlist. The script will also add all available settings below each filename in the playlist file.

----

## settings.txt

The settings.txt lets you change certain settings for the script:

```add-all-settings=0```: Adds all available settings for each file in the playlist

```add-global-settings=1```: Adds all available settings to the top of playlist file (which are used as global settings for all files in the playlist)

----

**Ícaro Ferre**  
[@icaroferre](http://twitter.com/icaroferre)  
[spektroaudio.com](http://spektroaudio.com/)  
 

