import easygui
import os

print("\n██████████████████████████████")
print("  ES Disting File Assistant  ")
print("       by Icaro Ferre")
print("██████████████████████████████\n")


def makeAudioPlaylist():
    filelist = []
    settings = {
        "loop": 0,
        "fadeOut": 3,
        "fadeIn": 3,
        "gap": 3,
        "retriggerOnSampleChange": 1,
        "fixedPitch": 0,
        "ramp": 0,
        "triggers": 0,
        "clocks": 4
    }

    print("\nGenerating Audio playlist...\n")
    # sub_category = input("Enter number to generate algorithm-specific playlist:")
    cardPath = easygui.diropenbox()

    playlist_filename = "playlist.txt"


    with open(os.path.join(cardPath, playlist_filename), "a") as f:
        f.write("disting playlist v1")
        for filename in os.listdir(cardPath):
            if ".wav" in filename:
                filelist.append(filename)
                f.write("\n\n" + filename)
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

    with open(os.path.join(cardPath, playlist_filename), "a") as f:
        f.write("disting playlist v1")
        for filename in os.listdir(cardPath):
            if ".mid" in filename:
                filelist.append(filename)
                f.write("\n\n" + filename)
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
    
    playlist_filename = "midi-playlist.txt"
    
    with open(os.path.join(cardPath, playlist_filename), "a") as f:
        f.write("disting playlist v1")
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
    operations()
