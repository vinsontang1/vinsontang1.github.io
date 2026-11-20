import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from urllib.request import urlopen

import yaml
from bs4 import BeautifulSoup
from scholarly.author_parser import AuthorParser


def profile_id():
    if os.getenv("GOOGLE_SCHOLAR_ID"):
        return os.environ["GOOGLE_SCHOLAR_ID"]
    config_path = Path(__file__).resolve().parents[1] / "_config.yml"
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    return parse_qs(urlparse(config["author"]["googlescholar"]).query)["user"][0]


class ProfilePages:
    """Fetch each public profile page once so access errors reach the job log."""

    logger = logging.getLogger(__name__)

    def _get_soup(self, path):
        with urlopen("https://scholar.google.com" + path, timeout=30) as response:
            page = BeautifulSoup(response.read(), "html.parser")
        if not page.select_one("#gsc_prf_in"):
            raise ValueError("Google Scholar did not return a public author profile")
        return page


def main():
    scholar_id = profile_id()
    parser = AuthorParser(ProfilePages())
    author = parser.fill(parser.get_author(scholar_id),
                         sections=["basics", "indices", "counts", "publications"])
    total = author.get("citedby")
    if author.get("scholar_id") != scholar_id or type(total) is not int or total < 0:
        raise ValueError("Google Scholar returned an incomplete citation profile")

    author["updated"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    author["publications"] = {p["author_pub_id"]: p for p in author["publications"]}
    badge = {"schemaVersion": 1, "label": "citations", "message": str(total)}
    results = Path(__file__).resolve().parent / "results"
    results.mkdir(exist_ok=True)
    for filename, data in [("gs_data.json", author), ("gs_data_shieldsio.json", badge)]:
        (results / filename).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"Fetched {total} citations for {author['name']} on {author['updated']}")


if __name__ == "__main__":
    main()
