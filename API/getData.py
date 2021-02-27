import bs4 as bs
import requests, json



def serverInfo():

    headerz = {"user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
    link = 'https://www.battlemetrics.com/servers/rust/7459421'


    with requests.session() as s:
        data = s.get(link, headers = headerz).text

    soup = bs.BeautifulSoup(data, 'lxml')

    try:
        mapURL = soup.find("img", {"class": "css-1jeg8p6"})
        mapURL = mapURL['src']
    except:
        mapURL = 'error'


    serverName = soup.find('title').text
    serverName = serverName[:-16]

    infoList = soup.find("dl", {"class": "css-1i1egz4"})

    lst = []

    for element in infoList.find_all('dd'):
        lst.append(element.text)



    with open("API/server_data.json", "r") as f:
        data = json.load(f)

    data["server_name"] = serverName
    data["server_rank"] = lst[0]
    data["player_count_current"] = lst[1]
    data["server_ip"] = lst[2]
    data["server_status"] = lst[3]
    data["server_map"] = mapURL

    with open("API/server_data.json", "w") as f:
        json.dump(data, f, indent=4)
