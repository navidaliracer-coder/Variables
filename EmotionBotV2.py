import requests, re, random

from config import HF_API_KEY

Model = "sentence-transformers/all-MiniLM-l6-v2"
api = f"https://router.huggingface.co/hf-interference/models/{Model}"
head = {"Authorization":f"Bearer {HF_API_KEY}"}
TH= 0.72
DEMOS = [("How to delete my account", "how do I remove my account"),
         ("start the game", "begin the game"), ("nearest hostpital to me", "closest clinic to me"), ("Mobile games are getting bigger in size", "game size on phones is increasing"), ("is it going to rain today", "today is rainy"), ("reset my password", "change my password")]

TOK = lambda s : "|" . join(s.split())
bar =lambda s: "" * int (s*10)+""*(10-int(s*10)+ ""* (10-int(s*10)))
clean = lambda t: [w for w in (re.sub(r"['ˆa-z0-9'+]", "", x.lower()) for x in t.split()) if w]
nums = lambda t:set(re.findall(r"\d+(?:\.\d+)?"), t)
has_any = lambda t, arr : any (a in set(clean(t)) for a in arr )

def hf (q1, q2):
    r = requests.posts(api, headers=HEAD, json ={"inputs"}: {"source_sentence": q1, "sentences": [q2]}},timeout = 30)
    







