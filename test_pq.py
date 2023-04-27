import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    # "Cookie": "enable_ZkLlO5PNXDiy=true; ZkLlO5PNXDiyS=5pnQ7.ufv3fF3xahWhKKY3BAd9WYIv1hgZKiQW2kyD3TvKd85JYSILt9uC7d.HhmeKAF8ENm9rcBMUruTGEhWOG; f1a6be9aae0b1d98d8=92175afca191878d131cf74abd1304d1; dataHide2=b63166fc-202f-4111-a8b2-2c34730edfc5; ZkLlO5PNXDiyT=oCTGieVhDq2Dov73stJfB41DLmpoNAY2NMXjn5gIpu6fofK7vUmxSOpzPrb_EONJmTobYafNcrwLhiy7IP.vLlkYEhW6u_TTI9mZ03rGh8vkYt4vPuZmovEdULeSPsX6m7OehRhS_yeFSCXiL5q6pP81dKCcXqOCUNObxC2dGqnWltnK_9igKiDxzIEnhQgz277djyBrQJNg_LTRXdIoFceS4RE1WL7r238uHN2VTcX5LgdJDj2.jcU4FQ.ZLyG0",
    "Cookie": "f1a6be9aae0b1d98d8=92175afca191878d131cf74abd1304d1; dataHide2=b63166fc-202f-4111-a8b2-2c34730edfc5;ZkLlO5PNXDiyS=5WhAkBy8xFx7AFk7It.zwIVh05vDs.Xj.BftMXwWTL8lV7dugdCU5kgFQjHH8S6P2K6sxkcO4er_xF58KGakySA; ZkLlO5PNXDiyT=viXliVXivv.g3GSwzemVrZEzDA4l5I1hEYOc2AldarDSH5NK70PMRfuHoRnmRdlf76ZEFGZgzxiZgI08SHFNMLhBw2Vxq8_bQlHRI4NB9qh5Eq7Dn104wKe4DDZcbiXsPzjCVPk8J9DjXiEgWs3aV1Qhc7RFBeRq4dS1x5tY6NRSDDDflQiaTbnaxVPgfZscip3bJRuloD4FEPA1aMgAVr5JaqAJH4V4hye4omUkS_fV2Fg27U_o1J2Zsqa3EjxS",
    "Host": "mpa.hubei.gov.cn",
    "Pragma": "no-cache",
    "Referer": "http://mpa.hubei.gov.cn/zfxxgk/fdzdgknr/cpzh/index.shtml",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44"
}

url = "http://mpa.hubei.gov.cn/zfxxgk/fdzdgknr/cpzh/index.shtml"

resp = requests.get(url, headers=headers)

print(resp.text)