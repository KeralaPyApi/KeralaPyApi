import shutil
from datetime import datetime
from pathlib import Path

import pypandoc
import requests

URL = "https://api.github.com/repos/KeralaPyApi/KeralaPyApi/releases"
DEST = Path("source/releases")
INTRO = """
Release Notes
=============

Release notes for KeralaPyApi releases will describe what's new in each version, and will also make you aware of any
backwards-incompatible changes made in that version.

When upgrading to a new version of Pyrogram, you will need to check all the breaking changes in order to find
incompatible code in your application, but also to take advantage of new features and improvements.

**Contents**

""".lstrip("\n")

shutil.rmtree(DEST, ignore_errors=True)
DEST.mkdir(parents=True)

releases = requests.get(URL).json()

with open(DEST / "index.rst", "w") as index:
    index.write(INTRO)

    tags = []

    for release in releases:
        tag = release["tag_name"]
        title = release["name"]
        name = title.split(" - ")[1]

        date = datetime.strptime(
            release["published_at"],
            "%Y-%m-%dT%H:%M:%SZ"
        ).strftime("%b %d, %Y")

        body = pypandoc.convert_text(
            release["body"].replace(r"\r\n", "\n"),
            "rst",
            format="markdown_github",
            extra_args=["--wrap=none"]
        )

        tarball_url = release["tarball_url"]
        zipball_url = release["zipball_url"]

        index.write("- :doc:`{} <{}>`\n".format(title, tag))
        tags.append(tag)

        with open(DEST / "{}.rst".format(tag), "w") as page:
            page.write("KeralaPyApi " + tag + "\n" + "=" * (len(tag) + 9) + "\n\n")
            page.write("\t\tReleased on " + str(date) + "\n\n")
            page.write("- :download:`Source Code (zip) <{}>`\n".format(zipball_url))
            page.write("- :download:`Source Code (tar.gz) <{}>`\n\n".format(tarball_url))
            page.write(name + "\n" + "-" * len(name) + "\n\n")
            page.write(body + "\n\n")

    index.write("\n.. toctree::\n    :hidden:\n\n")
    index.write("\n".join("    {}".format(tag) for tag in tags))
