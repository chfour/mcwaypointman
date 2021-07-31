#!/usr/bin/env python3
from waypoint import NotACopiedLocation, Waypoint
import clipboard
import logging, argparse

if __name__ == "__main__":
    logging.basicConfig(format="[%(asctime)s] %(levelname)s: %(message)s", level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=str,
                        help="output waypoints file")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="set the logging level to DEBUG")
    args = parser.parse_args()

    if args.verbose: logging.getLogger().setLevel(logging.DEBUG)

    try:
        while True:
            logging.debug("listening for clipboard changes")
            clip = clipboard.wait()
            logging.debug(repr(clip))
            try:
                waypoint = Waypoint.from_copied(clip)
            except NotACopiedLocation:
                logging.debug("not a copied location")
                continue
            logging.info(repr(waypoint))

            logging.debug(f"write to {args.output}")
            with open(args.output, "a") as f:
                f.write(str(waypoint) + "\n\n")
    except KeyboardInterrupt:
        logging.info("KeyboardInterrupt, exiting.")
