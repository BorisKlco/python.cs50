import re


def yt():
    return shrt(input("Link: "))


def shrt(list):
    extr = re.search(r'src="(.*?)"', list)
    if extr:
        link = extr.groups()
        if "youtube" in link[0]:
            short = link[0].replace("youtube.com", "youtu.be")
            try:
                return short.replace("www.", "")
            except:
                return short
        else:
            return f"not yt link"
    else:
        return f"Not yt link"


print(yt())
