import os
import argparse
import logging
import re
import datetime
import shutil

logging.basicConfig(level=logging.DEBUG)

re_header = re.compile("^#+\s+(.+)", re.MULTILINE)

def firstline(s):
    """Return first non-whitespace line in <s>, or None"""
    lines = filter(lambda x: x.strip(), s.split("\n"))
    return lines[0] if lines else None


def process_file(src_file, dst_file):
    """Read src_file, and generate pelican input into dst_file."""
    with open(src_file) as src:
        data = src.read()
        match = re_header.search(data)
        if match:
            st = os.stat(src_file)
            f_mtime = datetime.datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            f_title = match.group(1)
            f_firstline = firstline(data[:200])
            # print("===\n{dst_file}\nTitle: {f_title}\nModified: {f_mtime}\n\n{f_firstline}\n\n\n".format(**locals()))
            with open(dst_file, "w") as out:
                out.write("""Title: {f_title}
Modified: {f_mtime}

{data}
""".format(**locals()))
        else:
            logging.debug("{}: no header".format(src_file))


def build_site(**kwargs):

    inputdir = kwargs['inputdir']
    outputdir = kwargs['outputdir']

    if os.path.realpath(inputdir) == os.path.realpath(outputdir):
        raise ValueError("Output directory cannot be input directory")

    if os.path.exists(outputdir):
        if os.path.isdir(outputdir):
            if kwargs["f"]:
                logging.debug("Output directory '{}' exists: overwriting".format(outputdir))
                if kwargs["D"]:
                    logging.debug("Deleting output directory '{}'".format(outputdir))
                    shutil.rmtree(outputdir)
            else:
                raise ValueError("Output directory exists (specify -f to overwrite)")
        else:
            raise ValueError("Output exists but is not a directory")

    if not os.path.exists(outputdir):
        os.mkdir(outputdir)
        logging.debug("Created output directory '{outputdir}'".format(**locals()))

    print("inputdir={}, outputdir={}, force={}".format(inputdir, outputdir, kwargs["f"]))

    for r, dirs, files in os.walk(inputdir):

        # Don't recurse into outputdir if it's a subdirectory of inputdir
        if os.path.realpath(r).startswith(os.path.realpath(outputdir)):
            logging.debug("Skipping {}".format(outputdir))
            continue

        outdir_path = os.path.join(outputdir, r[1+len(inputdir):])
        if not os.path.exists(outdir_path):
            os.makedirs(outdir_path)

        for thisfile in files:
            src_file = os.path.join(r, thisfile)
            dst_file = os.path.join(outdir_path, thisfile)
            if ".md" in thisfile:
                process_file(src_file, dst_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert gitbook to pelican site")
    parser.add_argument("inputdir", help="The directory containing the gitbook site to convert")
    parser.add_argument("outputdir", help="Destination directory for pelican site")
    parser.add_argument("-f", action="store_true", default=False, help="Force write existing output directory")
    parser.add_argument("-D", action="store_true", default=False, help="Force deletion of existing output directory "
                        "before writing")

    args = parser.parse_args()
    try:
        build_site(**(args.__dict__))
    except Exception as e:
        logging.error(e.message)
        raise
