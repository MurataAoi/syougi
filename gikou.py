import requests


def gikou_return(sfen):
    r = requests.get(
        url=f"https://17xn1ovxga.execute-api.ap-northeast-1.amazonaws.com/production/gikou?byoyomi=10000&position=sfen {sfen}"
    )
    data = r.json()

    print(data["bestmove"])
    return data["bestmove"]
