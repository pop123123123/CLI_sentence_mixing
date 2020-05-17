import os

import sentence_mixing.sentence_mixer as sm
from sentence_mixing.logic.display import combo_displayer
from sentence_mixing.model.exceptions import PhonemError, TokenAmbiguityError
from sentence_mixing.serialize import load, save
from sentence_mixing.video_creator.audio import concat_wav

AUDIO_FILE_PATH = "out.wav"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_sentence(text):
    if text is not None:
        print("Previous sentences:\n", text)
    return input("Enter a sentence: ")


def loop_interface(audio_command, video_futures):
    total_timestamps = []
    total_text = ""
    timestamps_buffer = []
    timestamps_buffer_sentence = []

    sentence = get_sentence(None)
    videos = None

    while sentence != "":
        timestamps = []
        combo = None
        available_combos = []

        edit = False
        store = False
        valid = False
        load_audio_index = None
        i = 0
        while not valid and not edit:

            # Stores previous audio in buffer
            if store:
                timestamps_buffer.append(timestamps)
                timestamps_buffer_sentence.append(sentence)
                store = False

            if load_audio_index is not None:
                timestamps = timestamps_buffer[load_audio_index]
                load_audio_index = None
            else:
                if len(available_combos) == 0:
                    bad_sentence = True
                    while bad_sentence:
                        try:
                            if videos is None:
                                print("downloading...")
                                videos = list(video_futures)[0]
                            available_combos = sm.process_sm(sentence, videos)
                            bad_sentence = False
                        except KeyError as e:
                            print(e, "not recognized")
                            sentence = get_sentence(total_text)
                        except PhonemError as e:
                            print(
                                e,
                                "Try to change your sentence or add more videos.",
                            )
                            sentence = get_sentence(total_text)
                        except TokenAmbiguityError as e:
                            print(
                                e, "Please change this word",
                            )
                            sentence = get_sentence(total_text)
                combo = available_combos.pop(0)
                timestamps = combo.get_audio_phonems()

            print(combo_displayer(combo))
            concat_wav(AUDIO_FILE_PATH, timestamps)

            os.system(audio_command.format(AUDIO_FILE_PATH))

            if timestamps_buffer_sentence:
                print("Stashed audios:")
                for i, stashed_sentence in enumerate(
                    timestamps_buffer_sentence
                ):
                    print(i, ".", stashed_sentence)
                print("")

            line = input(
                "Enter 'y' to validate, 'e' to edit the sentence, 's' to store this audio in the buffer, 'l' + index for loading previously stored audio, otherwise just press enter: "
            )
            valid = line == "y"
            edit = line == "e"
            store = line == "s"

            if line.startswith("l "):
                index = line.split(" ")[1]
                if index.isdigit():
                    index = int(index)
                    if -1 < index < len(timestamps_buffer):
                        load_audio_index = index
                        print(load_audio_index)

            i += 1
            clear_screen()
        if not edit:
            total_timestamps.extend(timestamps)
            total_text += "\n" + sentence

        save(total_timestamps, total_text, name="video.json")
        sentence = get_sentence(total_text)
    clear_screen()
    return total_timestamps, total_text, videos
