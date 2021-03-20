# Build guide

This guide explains how to compile the python script and all its dependencies to an executable standalone version.

## Building the program

1. Install MFA through anaconda environment by following the [official tutorial](https://montreal-forced-aligner.readthedocs.io/en/latest/installation.html)
2. Activate the conda environment with ```source /opt/anaconda/bin/activate root && conda activate aligner```
3. Add the lib path of anaconda to ```LD_LIBRARY_PATH``` environment variable. Example: ```export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.conda/envs/aligner/lib/```
4. Run ```builder.sh```
5. Deactivate your conda environment with ```conda deactivate```

## Usage

Sentence mixer CLI should now be generated. To run the program, go to ```dist/P00pMaker``` and run the file ```P00pMaker``` with the same arguments as usual.

Example:  
```./P00pMaker config.json 'https://www.youtube.com/watch?v=VTaoMHjnRbM'```

## Cleanup

You can then remove the build and cleanup everything by running ```clean.sh```
