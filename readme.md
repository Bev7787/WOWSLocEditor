Introduction:
- This program is designed to run on Windows computers only.
- The program runs on a command line interface. Type in the character corresponding to the option required when prompted.
- Allows addition and convenient configuration of the global.mo file location, the addition or modification of elements to be changed, and the ability to implement changes automatically.

Background:
- WOWS localisation operates by having localisation matched to a corresponding ID. This ID is what is used in game to represent ships and other items. This system allows for the use of different localisations for different languages.
- The localisation for a particular message is stored in a file known as global.mo. Here, each localisation is matched to its ID. 
- By modifying the localisation in this file, it is possible to change the text displayed in game for a given language.

Usage:
- Ensure a backup copy of the global.mo file is made before using this program.
- Run locEditor.exe, and follow the prompts in the program.
- For actions related to the location of the global.mo file, type "1".
	- To add a new install location, type "1". Enter the location of your global.mo file. 
	- To update this location, type "2". The program will automatically update to the lastest version. 
- For actions related to the input of changes for localisation, type "2".
	- The program will prompt to determine if the change is for a ship. The game has two IDs for ships: The abbreviated name (Seen in battle), and the full name (visible when hovering over a ship in port). This option allows the user to change both names at once.
- To implement the changes, type "3". The program will prompt for confirmation, before modifying global.mo, and saving a new global.mo file located in the same filepath, except in the res_mods folder.
- To search for an ID via its current localisation, type "4". The search function will search for the exact phrase in the localisation. This can be an issue with names with special characters. Try searching for parts of a name instead if this is the case (e.g. Friedrich instead of Friedrich der Große.)

Note:
- When entering the location, the input should look similar to this:
	- (Path to your WOWS folder)\World_of_Warships\bin\4046169\res\texts\en\LC_MESSAGES
- The IDs and changed names are in the file editor_files/changes.txt/.
- If ship names have been changed and the changes do not show up, some ships have been modified and as a result, their ID has changed. An example of this is the Conqueror (IDS_PBSB110 and IDS_PBSB911). To be guaranteed of a name change, modify all instances of the same ship.


==========UPDATE NOTES==========
- v2.1
	- Added search interface. Allows for searching of an ID by the localisation.
	- The original global.mo file is no longer directly edited. The modified file is now located in res_mods. 
- v2.0 
	- Added Command Line Interface
	- Added ability to interact with changes.txt within the program itself.
	- Added ability to add/modify filepath.txt within the program itself.

Created by Bev7787.
