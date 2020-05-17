#!/usr/bin/env python3

import argparse
import concurrent.futures

import sentence_mixing.sentence_mixer as sm
from sentence_mixing.video_creator.download import dl_video
from sentence_mixing.video_creator.video import create_video_file

from cli_interface import loop_interface


def main(audio_command, config_path, skip_first, urls):
    sm.prepare_sm(config_path)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures_vids = executor.map(dl_video, urls)
        futures_vids_audio = executor.map(sm.get_videos, [urls])

        total_timestamps, total_text, videos = loop_interface(
            audio_command, futures_vids_audio
        )

        paths = list(futures_vids)
    for v, p in zip(videos, paths):
        n = len(v._base_path)
        assert p[:n] == v._base_path
        v.extension = p[n + 1 :]

    create_video_file(total_timestamps, paths)

    return total_text


DEFAULT_AUDIO_COMMAND = 'tycat "{}"'

DESCRIPTION = "CLI Interface to create sentence mixing videos."

AUDIO_COMMAND_HELP = f"a command to launch a playback of an audio file passed as a format parameter (default: {DEFAULT_AUDIO_COMMAND})"
CONFIG_PATH_HELP = "path to the json config file"
VIDEO_URL_HELP = "a YouTube url of the wanted video"
SKIP_ANALYSIS_HELP = "tell the generator to skip the analysis (default: false)"

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        "-c",
        "--audio-command",
        default=DEFAULT_AUDIO_COMMAND,
        help=AUDIO_COMMAND_HELP,
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
    parser.add_argument(
        "-s",
        "--skip",
        dest="skip_first_analysis",
        action="store_true",
        default=False,
        help=SKIP_ANALYSIS_HELP,
    )

    args = parser.parse_args()

    print(
        main(
            args.audio_command,
            args.config_path,
            args.skip_first_analysis,
            args.video_urls,
        )
    )
