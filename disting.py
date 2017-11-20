import easygui
import os
import os.path
import sys

print("\n██████████████████████████████")
print("  ES Disting File Assistant  ")
print("       by Icaro Ferre")
print("██████████████████████████████\n")

scriptSettings = {
    "add-all-settings": 1,
    "add-global-settings": 0
}


def loadSettingsFile():
    global scriptSettings
    try:
        with open(sys.path[0] + "/settings.txt", "r") as f:
            for line in f:
                newline = line.rstrip()
                newline = newline.split("=")
                if newline[0] in scriptSettings:
                        scriptSettings[newline[0]] = int(newline[1])
        print(str(scriptSettings))
    except FileNotFoundError:
        print("Settings file not found.")


def eraseExistingFile(path):
    if os.path.isfile(path):
        open(path, "w").close()


def makeAudioPlaylist():
    filelist = []
    settings = {
        "loop": 1,
        "fadeOut": 3,
        "fadeIn": 3,
        "gap": 3,
        "retriggerOnSampleChange": 1,
        "fixedPitch": 0,
        "ramp": 0,
        "triggers": 0,
        "clocks": 16
    }

    print("\nGenerating Audio playlist...\n")
    sub_category = input("Enter suffix for algorithm-specific playlist (press enter for general audio): ")
    cardPath = easygui.diropenbox()

    if sub_category == "":
        playlist_filename = "playlist.txt"
        for filename in os.listdir(cardPath):
            if ".wav" in filename:
                filelist.append(filename)
    else:
        playlist_filename = "playlist-" + sub_category + ".txt"
        for filename in os.listdir(cardPath):
            if ".wav" in filename and sub_category + "_" in filename and "." + sub_category not in filename:
                filelist.append(filename)

    eraseExistingFile(os.path.join(cardPath, playlist_filename))

    with open(os.path.join(cardPath, playlist_filename), "a") as f:
        f.write("disting playlist v1")

        if scriptSettings["add-global-settings"] == 1:
            f.write("\n")
            for s in sorted(settings):
                f.write("\n-" + s + "=" + str(settings[s]))

        for filename in sorted(filelist):
                f.write("\n\n" + filename)
                if scriptSettings["add-all-settings"] == 1:
                    for s in sorted(settings):
                        f.write("\n-" + s + "=" + str(settings[s]))
        checkNumberOfFiles(filelist, 64)


def makeMidiPlaylist():
    filelist = []
    settings = {
        "loop": 0,
        "zeroVNote": 48,
        "bendRange": 2,
        "cc1offset": 0,
        "cc1scale": 5,
        "cc2offset": 0,
        "cc2range": 5
    }

    print("\nGenerating MIDI playlist...\n")
    cardPath = easygui.diropenbox()

    playlist_filename = "midi-playlist.txt"

    eraseExistingFile(os.path.join(cardPath, playlist_filename))

    with open(os.path.join(cardPath, playlist_filename), "a") as f:
        f.write("disting playlist v1")

        if scriptSettings["add-global-settings"] == 1:
            f.write("\n")
            for s in sorted(settings):
                f.write("\n-" + s + "=" + str(settings[s]))

        for filename in os.listdir(cardPath):
            if ".mid" in filename:
                filelist.append(filename)
                f.write("\n\n" + filename)
                if scriptSettings["add-all-settings"] == 1:
                    for s in sorted(settings):
                        f.write("\n-" + s + "=" + str(settings[s]))


def makeWaveTablePlaylist():
    filelist = []
    settings = {
        "wavelength": 600
    }
    print("\nGenerating Wavetable playlist...\n")
    addFolders = input("Add folders to playlist? [y/n]: ")
    cardPath = easygui.diropenbox()

    if addFolders == "y":
        addFolders = True
    else:
        addFolders = False

    playlist_filename = "playlist-wavetable.txt"

    eraseExistingFile(os.path.join(cardPath, playlist_filename))
    
    with open(os.path.join(cardPath, playlist_filename), "a") as f:
        f.write("disting playlist v1")

        if scriptSettings["add-global-settings"] == 1:
            f.write("\n")
            for s in sorted(settings):
                f.write("\n-" + s + "=" + str(settings[s]))
        
        for filename in os.listdir(cardPath):
            if ".wav" in filename and ".txt" not in filename:
                filelist.append(filename)
                f.write("\n\n" + filename)
                for s in sorted(settings):
                    f.write("\n-" + s + "=" + str(settings[s]))
        if addFolders:
            for folder in os.listdir(cardPath):
                if "." not in folder and ".txt" not in folder:
                    folder_path = os.path.join(cardPath, folder)
                    f.write("\n\n" + folder)
                    with open(os.path.join(folder_path, "playlist.txt"), "a") as w:
                        w.write("disting playlist v1\n")
                        for filename in os.listdir(folder_path):
                            if ".wav" in filename and ".txt" not in filename:
                                filelist.append(filename)
                                w.write("\n" + filename)


def checkNumberOfFiles(x, max):
    print("Number of files found: ", str(len(x)))
    if len(x) > max:
        print("ATTENTION! The directory contains more than " + str(max) + " files.")


def operations():
    print("Available operations: audio, midi, wavetable")
    operation = input("Enter operation: ")
    if operation == "audio":
        makeAudioPlaylist()
    elif operation == "midi":
        makeMidiPlaylist()
    elif operation == "wavetable":
        makeWaveTablePlaylist()
    else:
        print("Invalid operation. \n")
        operations()
    print("\nOperation was successful.")


if __name__ == "__main__":
    loadSettingsFile()
    operations()
