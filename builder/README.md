# Build guide

This guide explains how to compile the python script and all its dependencies to an executable standalone version.

## Building the program

1. Install the requirements of the main project ```pip install -r ../requirements.txt```
2. Install the requirements with ```pip install -r requirements.txt```
3. Run ```builder.sh```

The compiled program is located in ```dist/P00pMaker```

## Cleanup

You can then remove the build and cleanup everything by running ```clean.sh```  
Use the argument --hard to remove MFA tarball and model zip.
