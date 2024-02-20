# KillJamesBondMP3
 A tool to rename podcast KJB files from patreon. This will rename the files and apply ID3 tags.

# NO PIRACY 
 Note: This will NOT let you pirate Kill James Bond episodes you don't have access to. 
 This is solely for people who subscribe to the patreon at the bonus episodes tier. 

# Usage:
 1. Install the requirements:
  ``` python3 -m pip install -r requirements.txt```
 2. Use [PatreonDownloader](https://github.com/AlexCSDev/PatreonDownloader) to get the raw mp3 files. Make sure you pass --json! 
  ``` PatreonDownloader.App.exe --json --url https://www.patreon.com/killjamesbond/posts ```
 3. Copy name.py into the download directory (download/Kill James Bond!)
 4. Switch to the download directory and run name.py:
  ```python3 name.py```
 5. The files will now be in the mp3 subfolder. They will now have more reasonable filenames and id3 tags.

# Notes
 This script has to apply some manual fixes for some mistakes or odd decisions done by the KJB team (such as there being two S2E2 episodes). 

 It has manual fixes for these issues, but any episodes newer than this script (S03E13 - Our Agent Tiger) may not be properly labeled.

 This has only been pretty manually tested. It could definitely be cleaned up and options added and better integrated.

# Issues with manual fixes:

* KJB100: Dr No Notes: This episode is assigned to S02E15.5 as it has no episode number
* KJB Holiday Special: Die Hard: This episode is assigned S02E14.75 as it has no episode number
* S2E2: Agent Secret FX-18: This episode is reassigned to S3E2 since S2E2 already exists

# Requirements 
 * Python 3.6+ (tested on 3.11)
 * [PatreonDownloader](https://github.com/AlexCSDev/PatreonDownloader)

# License
 * GPL version 3. See LICENSE file for details
