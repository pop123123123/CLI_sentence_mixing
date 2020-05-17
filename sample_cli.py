import argparse

import sentence_mixing.logic.parameters as params
import sentence_mixing.sentence_mixer as sm

DESCRIPTION = "CLI Interface to build a sentence from a video"

SEED_HELP = f"change the seed used in phonem association's score attribution (default: {params.DEFAULT_SEED})"
TARGET_SENTENCE_HELP = "a sentence you want to hear from the video"
CONFIG_PATH_HELP = "path to the json config file"
VIDEO_URL_HELP = "a YouTube url of the wanted video"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        "-s", "--seed", default=params.DEFAULT_SEED, help=SEED_HELP,
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

    sm.prepare_sm(args.config_path)
    videos = sm.get_videos(args.video_urls)
    print(sm.process_sm(args.sentence, videos, args.seed)[0])
