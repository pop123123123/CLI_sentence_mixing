# Sentence Mixing generator - command line interface

This program uses the [Sentence Mixing library](http://github.com/pop123123123/sentence-mixing) to **generate** sentence mixing styled **Youtube Poops**.

## Installation

1. Clone the [Sentence Mixing library](http://github.com/pop123123123/sentence-mixing)
2. Install the library by doing ```pip install -e [path to sentence mixing library]```
3. Set up the external dependencies by following the tutorial in [SM library github page](https://github.com/pop123123123/sentence-mixing)

### Audio feedback

By default, the script uses the ```tycat``` command, available on [Terminology](https://github.com/borisfaure/terminology) terminal emulator to play the audio feedback while building the video.  
If you want to use any other program, juste change the global variable ```DEFAULT_AUDIO_COMMAND``` in ```video_creator_main.py```. The associated audio file is automatically given as argument.  
Example: ```DEFAULT_AUDIO_COMMAND = 'vlc "{}"'```

### Sanity check

Use the file ```sample_cli.py```,  a minimal example for the sentence mixing library.  
If no error pops, the Sentence Mixing library is correctly installed.  
Example:  
```python sample_cli.py "Test sentence" ../config.json https://www.youtube.com/watch?v=4czmCgJryUM```

## Program usage

Full CLI application with handy control interface.

### Running the script

Give your json configuration file as first argument, then give as many Youtube URLs as you want.  

Example:  
```python video_creator_main.py config.json 'https://www.youtube.com/watch?v=udmDOaHN9no https://www.youtube.com/watch?v=7CTH59GCNko'```

### Interactive process

The script will prompt you to divide your target speech in different segments.
There is no optimal way to divide a target speech to chunk. Just do as you wish.

Examples:  
Target sentence: Salut la compagnie  
Possible chunks:  
* Salut | la | con | pas | nie
* Salut la compagnie
* Salut | la compagnie
* ...

The audio sequence creation process works then as follows:
1. Enter the chunk of the sentence you want to hear
2. You will hear an audio feedback from the chosen combo. There you can press:
	* ```ENTER``` if you are not satisfied with current combo for this chunk and want another phonems
	* ```e``` to change the written chunk
	* ```s``` to store the current combo in a buffer, so you can browse other combos without fearing to this one
	* ```l + number``` to load a previously sotred combo
	* ```y``` to accept the current combo and go to next chunk
3. Loops to 1. until you enter an empty chunk
4. The full video is formed from the selected combo

Concerning the audio feedback mentioned at point 2:  

## Tips

* Only subtitled youtube videos are usable
* Spaces count as blank phonems. It can be very useful to add pause in your sentences.
* Do not hesitate to put a lot of Youtube URLs in argument. The more the video material, the more choice you will have to form the sentences you want
* An already downloaded video will not be downloaded again. So, do not hesitate then to download long videos to boost accuracy.
* Advance little by little
