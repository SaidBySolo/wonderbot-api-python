import aiohttp
import json

apimain = "https://api.wonderbot.xyz/shards"

async def shards(shardsid=None, raw=False):
    """
    샤드 넘버를 인자값을 주신경우, 해당 넘버만 dict로 반환합니다.

    ``raw``가 ``True``일시에는 요청한 그대로 json.loads하여 반환합니다.

    인자값이 없을경우 리스트를 출력합니다..
    """
    async with aiohttp.ClientSession() as cs:
        async with cs.get(apimain) as r:
            response = await r.text()
            data = json.loads(response)
            datalist = data['data']

            if raw is True:
                return data
            
            if shardsid is not None:
                shard = datalist[int(shardsid)]
            else:
                return datalist

            return shard