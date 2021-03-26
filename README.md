# Sentence Mixing generator - command line interface

This program uses the [Sentence Mixing library](http://github.com/pop123123123/sentence-mixing) to **generate** sentence mixing styled **Youtube Poops**.

You can get it via the release tab or install it manually.

## Installation

### Release

1. Choose a [release version](https://github.com/pop123123123/CLI_sentence_mixing/releases)
2. Uncompress the release archive 

### From source

1. Install requirements of CLI original project with ```pip install -r ../requirements.txt```
2. Install requirements with ```pip install -r requirements.txt```
3. Set up the external dependencies by following the tutorial in [SM library github page](https://github.com/pop123123123/sentence-mixing)

#### Sanity check

Use the file ```sample_cli.py```,  a minimal example for the sentence mixing library.
If no error pops, the Sentence Mixing library and the external dependencies are correctly installed.

Example:  
```python sample_cli.py "Bonjour" ../config.json https://www.youtube.com/watch?v=4czmCgJryUM```

## Program usage

The following sections will explain you how to run and interact with the CLI Youtube Poop generation program.

### Running the script

The file to run may vary:
* **Linux** release: ```P00pMaker```
* **Windows** release: ```P00pMaker.exe```
* **From source:** ```video_creator_main.py```

Run the executable with your json configuration file as first argument, and as many Youtube URLs as you want.

Examples:
* **Linux:** ```./P00pMaker config.json 'https://www.youtube.com/watch?v=udmDOaHN9no' 'https://www.youtube.com/watch?v=7CTH59GCNko'```
* **Windows:** ```.\P00pMaker.exe config.json 'https://www.youtube.com/watch?v=udmDOaHN9no' 'https://www.youtube.com/watch?v=7CTH59GCNko'```
* **From source:** ```python video_creator_main.py config.json 'https://www.youtube.com/watch?v=udmDOaHN9no' 'https://www.youtube.com/watch?v=7CTH59GCNko'```

For windows, the program might be blocked by your antivirus, be aware of this possibility.

#### Audio feedback

By default, the ```video_creator_main.py``` script uses the ```tycat``` command, available on [Terminology](https://github.com/borisfaure/terminology) terminal emulator to play the audio feedback while building the video.

If you want to use any other program, give it to argument with -c. Replace the filename in the command by ```{}```.

Example:  
```python video_creator_main.py -c "vlc --play-and-exit --no-repeat --no-loop {}" config.json 'https://www.youtube.com/watch?v=udmDOaHN9no'```

##### For Windows release

You will face a problem if the command you want to use contains a space in its path.

Here is a simple trick to work around the problem. Let's say we want to use ```vlc``` as audio feedback command.  
Create ```feedback.bat``` with the following content:
```bat
"C:\Program Files\VideoLAN\VLC\vlc.exe" --play-and-exit --no-repeat --no-loop %*
```
(Path to vlc might change depending of your setup)

Then, call the program with the followin ```-c``` parameter:  
```./P00pMaker config.json 'https://www.youtube.com/watch?v=VTaoMHjnRbM' -c "feeback.bat {}"```


### Interactive process

The audio sequence creation process works as follows:
1. Enter the chunk of the sentence you want to hear
2. You will hear an audio feedback from the chosen combo. There you can press:
	* ```ENTER``` if you are not satisfied with current combo for this chunk and want another phonemes
	* ```e``` to change the written chunk
	* ```s``` to store the current combo in a buffer, so you can browse other combos without fearing to lose this one
	* ```l + number``` to load a previously stored combo
	* ```y``` to accept the current combo and go to next chunk
3. Loop to 1. until you enter an empty chunk
4. The full video is formed from the association of all the selected combo

### Tips

* Punctuation symbols count as blank phonemes. It can be very useful to add pause in your sentences.
* Do not hesitate to put a lot of Youtube URLs in argument. The more the video material, the more choice you will have to form the sentences you want.
* An already downloaded video will not be downloaded again. So, do not hesitate then to download long videos to boost accuracy.
* Advance little by little. There is no big difference in accuracy between long and short chunks, so, it is generally preferable to write short chunks (+/- 1 word by chunk) to have more control of how each word/syllabus sound. For example, it is probably better to split sentence *"Salut les gens"* in three chunks "*Salut*", "*les*", "*gens"* than in one big chunk "*Salut les gens*".
* For some long words, it can **sometimes** be interesting to split it in little chunks. For example, you can split the word *Compagnie* in three chunks *"Con"*, "*Pas*", *"Nie"*.
* If a word you want to hear can be directly heard in one of the source video (same word or homophone), don't split it in chunks, it will directly been taken from the source video. For example, if the word "Camp" is present in source subtitles, words "Camp", "Quand", "Quant" will automatically associate to the original "Camp".
* Related to previous point, try to use a maximum of words you can find in the original video. The result will be way more accurate and understandable.

### Restrictions and workarounds

#### Subtitles free videos

Only subtitled youtube videos are usable. Automatically generated youtube subtitles work as well.  
If you really want to use a non subtitled video, you will have to write the subtitles yourself.

#### Phoneme not found

If your source video corpus is very short or contains very few words, it might be possible that some phonemes are not prounounced at all through the whole video material.
In that case, you will not be able to use these particular phonemes.  
The problem can be easily solved by adding video material to the corpus, or not using these missing phonemes.

#### Unrecognized word

You can only enter a word that already exists in the dictionnary. If you want to hear an external word, you have two solutions:
1. Add the word in the dictionnary
2. Split the word in sub-dictionnary-registered words  

For example, the word "Bolos" can be either:  
1. Added in the dictionnary by adding the line "BOLOS b o l o s"
2. Decomposed in three valid words "Beau" "l'eau" "se"

#### Ambiguity intolerance

Unfortunately, the system doesn't tolerates ambiguous words for the moment.  
For exemple, word "Est" can be pronounced:
1. With phoneme "e" (to be)
2. With phonemes "E s t" (east)

Thus, it is for the moment forbidden to write down word "Est". Waiting for a disambiguation feature, just **change the word for an homophone**.

For word "Est", if you want to hear phoneme "e", you can use word "Et" ; if you want to hear phonemes "e s t", you can use the sequence of words "S" "te" (not perfect coverage of phonemes in this case however).

## Building project

You can make your own release of the program in order to use it freely without dependancies.  
Everything concerning this feature is explained in folder ```builder```.  
