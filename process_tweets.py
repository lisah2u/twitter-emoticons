import sys
import json

in_file = open('tweets.json', 'r', encoding="utf8")
out_file = open('tweets-processed.json', 'a')

#t = in_file.read()
#json_string = json.loads(t)
# text = json.dumps(json_string, ensure_ascii=False).encode('utf16', "surrogatepass").decode("utf16")

with open('tweets.json', 'r') as f:
    line = f.readline()
    tweet = json.loads(line) # Python dict
    print(json.dumps(tweet, indent=4)) # pretty-print
    text = json.dumps(tweet, ensure_ascii=False).encode('utf16', "surrogatepass").decode("utf16")
    out_file.write(text)


# smiley
# 😃

