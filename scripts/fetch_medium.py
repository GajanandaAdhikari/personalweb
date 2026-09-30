import json, re, sys, html, urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

m = re.search(r'^medium_user:\s*"?(@?[\w.\-]+)', open("_config.yml").read(), re.M)
if not m or "YOUR-MEDIUM" in m.group(1):
    sys.exit("Set medium_user in _config.yml")
user = m.group(1) if m.group(1).startswith("@") else "@" + m.group(1)
req = urllib.request.Request(f"https://medium.com/feed/{user}", headers={"User-Agent": "Mozilla/5.0"})
root = ET.fromstring(urllib.request.urlopen(req, timeout=30).read())
ns = {"c": "http://purl.org/rss/1.0/modules/content/"}
path = "_data/medium.json"
try:
    items = {i["url"]: i for i in json.load(open(path))}
except Exception:
    items = {}
for it in root.iter("item"):
    title = (it.findtext("title") or "").strip()
    url = it.findtext("link").split("?")[0]
    body = re.sub(r"<figure.*?</figure>", " ", it.findtext("c:encoded", namespaces=ns) or "", flags=re.S)
    text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", body))).strip()
    if text.startswith(title):
        text = text[len(title):].strip()
    if len(text) > 180:
        text = text[:180].rsplit(" ", 1)[0] + "…"
    items[url] = {"title": title, "url": url, "description": text,
                  "date": parsedate_to_datetime(it.findtext("pubDate")).strftime("%Y-%m-%d")}
out = sorted(items.values(), key=lambda i: i["date"], reverse=True)
json.dump(out, open(path, "w"), indent=2, ensure_ascii=False)
print(f"{len(out)} articles")
