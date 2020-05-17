import argparse
import os

import sentence_mixing.logic.parameters as params
import sentence_mixing.logic.video_processing
import sentence_mixing.sentence_mixer as sm
from sentence_mixing.logic.display import combo_displayer
from sentence_mixing.serialize import load, save

import cli_interface


def preprocess_and_align(video_urls):
    """
    Build all the model objects for several video urls by downloading videos and analysing the
    videos using Montreal aligner.

    Argument:
    video_urls - list containing youtube videos url

    Returns a list containing all the video objects
    """

    # Creates basic Video objects
    videos = sentence_mixing.logic.video_processing._create_videos(video_urls)

    # Enriches Video objects with SubtitleLine objects
    sentence_mixing.logic.video_processing._create_subs(videos)

    # Enriches Video objects with AudioWords and AudioPhonem objects
    for video in videos:
        for i, subtitle in enumerate(video.subtitles):
            textgrid_path = os.path.join(
                out_dir, video.get_hashed_basename() + str(i) + ".TextGrid"
            )
            sentence_mixing.logic.video_processing._parse_align_result(
                textgrid_path, subtitle
            )

    return videos


DESCRIPTION = "CLI Interface to build a sentence from a video"

SEED_HELP = f"change the seed used in phonem association's score attribution (default: {params.DEFAULT_SEED})"
TARGET_SENTENCE_HELP = "a sentence you want to hear from the video"
CONFIG_PATH_HELP = "path to the json config file"
VIDEO_URL_HELP = "a YouTube url of the wanted video"

out_dir = None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--seed", default=params.DEFAULT_SEED, help=SEED_HELP,
    )
    parser.add_argument(
        "out_dir", action="store", help="textgrids directory",
    )
    parser.add_argument(
        "sentence",
        metavar="TARGET_SENTENCE",
        action="store",
        help=TARGET_SENTENCE_HELP,
    )
    parser.add_argument(
        "config_path",
        metavar="CONFIG_PATH",
        action="store",
        help=CONFIG_PATH_HELP,
    )
    parser.add_argument(
        "video_urls",
        metavar="VIDEO_URL",
        nargs="+",
        action="store",
        help=VIDEO_URL_HELP,
    )

    args = parser.parse_args()
    out_dir = args.out_dir

    sm.prepare_sm(args.config_path)
    videos = sm.get_videos(args.video_urls)
    combos = sm.process_sm(args.sentence, videos, args.seed)

    print(combo_displayer(combos[0]))
    sentence_mixing.video_creator.audio.concat_wav(
        cli_interface.AUDIO_FILE_PATH, combos[0].get_audio_phonems()
    )
