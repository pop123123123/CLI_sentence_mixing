# Sentence Mixing generator - command line interface

This program uses [Sentence Mixing library](http://github.com/pop123123123/sentence-mixing) to **generate** sentence mixing styled **Youtube Poops**.

## Installation

1. Clone the [Sentence Mixing library](http://github.com/pop123123123/sentence-mixing)
2. Install the library by doing ```pip install -e [path to sentence mixing library]```
3. Set up the external dependencies by following the tutorial in [SM library github page](https://github.com/pop123123123/sentence-mixing)

## Entrypoints

### sample_cli.py

Minimal example for the sentence mixing library.
**You should use it to make sure everything is working.**
Returns string representation of first selected combos.

### video_creator_main.py

Full CLI application with handy control interface.

#### Running the script

Give your json configuration file as first argument, then give as many youtube links as you want.  

Example:  
```python video_creator_main.py config.json 'https://www.youtube.com/watch?v=udmDOaHN9no https://www.youtube.com/watch?v=7CTH59GCNko'```

#### Interactive process

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

#### Audio feedback

By default, the script uses the ```tycat``` command, available on [Terminology](https://github.com/borisfaure/terminology) terminal emulator to play the audio feedback.  
If you want to use any other program, juste change the global variable ```DEFAULT_AUDIO_COMMAND``` in ```video_creator_main.py```. The associated audio file is automatically given as argument.  
Example: ```DEFAULT_AUDIO_COMMAND = 'vlc "{}"'```

#### Tips

* Only subtitled youtube videos are usable
* Spaces count as blank phonems. It can be very useful to add pause in your sentences.
* Do not hesitate to put a lot of Youtube links in argument. The more the video material, the more choice you will have to form the sentences you want
* An already downloaded video will not be downloaded again. Once more, do not hesitate then to download long videos to boost accuracy.
* Advance little by little
