Introduction:
- The program runs on a command line interface. Type in the character corresponding to the option required. 
- The program allows addition and convenient configuration of the global.mo file location, the addition or modification of elements to be changed, and the ability to implement changes.

Usage:
- Ensure a backup copy of the global.mo file is made before using this program.
- Run locEditor.exe, and follow the prompts in the program.

Note:
- When entering the location, the input should look similar to this:
	- D:\Games\World_of_Warships_ASIA\bin\4046169\res\texts\en\LC_MESSAGES
	- Do not worry if the World_of_Warships_ASIA folder is named differently. This is a legacy folder name that does not affect anything.
- The IDs and changed names are in the file editor_files/changes.txt/. To modify another element of the game, do the following:
- If your changes do not show up, some ships have been modified and as a result, their ID has changed. An example of this is the Conqueror (IDS_PBSB110 and IDS_PBSB911). To be safe, modify all instances of the same ship.


==========UPDATE NOTES==========
- v2.0 
	- Added Command Line Interface
	- Added ability to interact with changes.txt within the program itself.
	- Added ability to add/modify filepath.txt within the program itself.

Created by Bev7787.
