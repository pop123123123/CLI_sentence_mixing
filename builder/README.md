# Build guide

This guide explains how to compile the python script and all its dependencies to an executable standalone version.

## Building the program

1. Install the requirements with ```pip install -r requirements.txt```
2. Run ```builder.sh```

## Usage

Sentence mixer CLI should now be generated. To run the program, go to ```dist/P00pMaker``` and run the file ```P00pMaker``` with the same arguments as usual.

Example:  
```./P00pMaker config.json 'https://www.youtube.com/watch?v=VTaoMHjnRbM'```

### For Windows users

Run the program with admin powershell.

To [change the audio feedback command](https://github.com/pop123123123/CLI_sentence_mixing#audio-feedback), you will face a problem if the command you want to use contains a space in its path.

Here is a simple trick to work around the problem. Let's say we want to use ```vlc``` as audio feedback command.  
Create ```feedback.bat``` with the following content:
```bat
"C:\Program Files\VideoLAN\VLC\vlc.exe" --play-and-exit --no-repeat --no-loop %*
```
(Path to vlc might change depending of your setup)

Then, call the program with the followin ```-c``` parameter:
```./P00pMaker config.json 'https://www.youtube.com/watch?v=VTaoMHjnRbM' -c "feeback.bat {}"```

## Cleanup

You can then remove the build and cleanup everything by running ```clean.sh```  
Use the argument --hard to remove MFA tarball and model zip.
