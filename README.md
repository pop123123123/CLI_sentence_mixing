# Sentence Mixing generator - command line interface

This program uses the [Sentence Mixing library](http://github.com/pop123123123/sentence-mixing) to **generate** sentence mixing styled **Youtube Poops**.

## Installation

1. Install requirements with ```pip install -r requirements.txt```
2. Set up the external dependencies by following the tutorial in [SM library github page](https://github.com/pop123123123/sentence-mixing)

### Sanity check

Use the file ```sample_cli.py```,  a minimal example for the sentence mixing library.
If no error pops, the Sentence Mixing library and the external dependencies are correctly installed.

Example:
```python sample_cli.py "Bonjour" ../config.json https://www.youtube.com/watch?v=4czmCgJryUM```

## Program usage

The following sections will explain you how to run and interact with the CLI Youtube Poop generation program.

### Running the script

Run ```video_creator_main.py``` with your json configuration file as first argument, and as many Youtube URLs as you want.

Example:
```python video_creator_main.py config.json 'https://www.youtube.com/watch?v=udmDOaHN9no https://www.youtube.com/watch?v=7CTH59GCNko'```

#### Audio feedback

By default, the ```video_creator_main.py``` script uses the ```tycat``` command, available on [Terminology](https://github.com/borisfaure/terminology) terminal emulator to play the audio feedback while building the video.

If you want to use any other program, give it to argument with -c. Replace the filename in the command by ```{}```.

Example:  
```python video_creator_main.py -c "vlc --play-and-exit --no-repeat --no-loop {}" config.json 'https://www.youtube.com/watch?v=udmDOaHN9no'```

### Interactive process

The audio sequence creation process works as follows:
1. Enter the chunk of the sentence you want to hear
2. You will hear an audio feedback from the chosen combo. There you can press:
	* ```ENTER``` if you are not satisfied with current combo for this chunk and want another phonems
	* ```e``` to change the written chunk
	* ```s``` to store the current combo in a buffer, so you can browse other combos without fearing to lose this one
	* ```l + number``` to load a previously stored combo
	* ```y``` to accept the current combo and go to next chunk
3. Loop to 1. until you enter an empty chunk
4. The full video is formed from the association of all the selected combo

## Tips

* Only subtitled youtube videos are usable.
* Punctuation symbols count as blank phonems. It can be very useful to add pause in your sentences.
* Do not hesitate to put a lot of Youtube URLs in argument. The more the video material, the more choice you will have to form the sentences you want.
* An already downloaded video will not be downloaded again. So, do not hesitate then to download long videos to boost accuracy.
* Advance little by little. There is no big difference in accuracy between long and short chunks, so, it is generally preferable to write short chunks (+/- 1 word by chunk) to have more control of how each word/syllabus sound. For example, it is probably better to split sentence *"Salut les gens"* in three chunks "*Salut*", "*les*", "*gens"* than in one big chunk "*Salut les gens*".
* For some long words, it can **sometimes** be interesting to split it in little chunks. For example, you can split the word *Compagnie* in three chunks *"Con"*, "*Pas*", *"Nie"*.
* If a word you want to hear can be directly heard in one of the source video (same word or homophone), don't split it in chunks, it will directly been taken from the source video. For example, if the word "Camp" is present in source subtitles, words "Camp", "Quand", "Quant" will automatically associate to the original "Camp".
* Related to previous point, try to use a maximum of words you can find in the original video. The result will be way more accurate and understandable.
* You can only enter a word that already exists in the dictionnary. If you want to hear an external word, you have two solutions: add the word in the dictionnary or split the word in sub-dictionnary-registered words. For example, the word "Bolos" can be either added in the dictionnary by adding the line "BOLOS b o l o s", either decomposed in three valid words "Beau l"eau se"
* Unfortunately, the system doesn't tolerates ambiguous words for the moment. For exemple, word "Est" can pronounce with phonem "e" (to be), or phonems "E s t" (east); thus, it is forbidden to write down word "Est". Waiting for a disambiguation feature, just change the word for an homophone. For word "Est", if you want to hear phonem "e", you can use word "Et" ; if you want to hear phonems "e s t", you can use words "Ai se te" (not perfect coverage of phonems in this case however).

## Building project

You can compile the program to use it freely without dependancies. Everything concerning this feature is explained in folder ```builder```.  
This is completely non-mandatory to use the program.
