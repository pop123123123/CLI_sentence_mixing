# Build guide

This guide explains how to compile the python script and all its dependencies to an executable standalone version.

## Building the program

1. Install the requirements with ```pip install -r requirements.txt```
2. Run ```builder.sh```

## Usage

Sentence mixer CLI should now be generated. To run the program, go to ```dist/P00pMaker``` and run the file ```P00pMaker``` with the same arguments as usual.

Example:  
```./P00pMaker config.json 'https://www.youtube.com/watch?v=VTaoMHjnRbM'```

## Cleanup

You can then remove the build and cleanup everything by running ```clean.sh```
