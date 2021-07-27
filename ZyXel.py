import requests
import re

class ZyXEL:
    def __init__(self) -> None:
        self.url = "http://192.168.1.1/statsifc.html"
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Cookie': 'SESSION=681486590'
        }
        self.parseingData = []

    def getInfo(self) -> None:
        res = requests.get(self.url, headers=self.headers)
        if res.status_code == 200:
            self.data = res.text
            self.parseing()
        else:
            return "none"

    def parseing(self) -> None:
        if 'P8802T2R' not in self.data:
            return "none"
        reP = r'''<!---hide{---var-brdId-=-'(.*?)';---document.write\(\"<td-class='hd'>(.*?)</td>"\);}//-done-hiding---></script>------------------<td>(.*?)</td>------------------<td>(.*?)</td>------------------<td>(.*?)</td>------------------<td>(.*?)</td>------------------<td>(.*?)</td>------------------<td>(.*?)</td>------------------<td>(.*?)</td>------------------<td>(.*?)</td>'''
        reP = reP.replace('\n', '').strip().replace(' ', '-')
        res = re.findall(reP, self.data.replace(
            '\n', '').strip().replace(' ', '-'))
        structure = []
        for i in res:
            print(i)
            structure.append(
                {
                    # 'boradID': i[0],
                    'Lan': i[1],
                    'Download': {
                        'bytes': i[2],
                        'Pkts':	i[3],
                        'Errs':	i[4],
                        'Drops': i[5]
                    },
                    'Upload': {
                        'bytes': i[6],
                        'Pkts':	i[7],
                        'Errs':	i[8],
                        'Drops': i[9]
                    },
                }
            )
        self.parseingData = structure

    @property
    def getParseingData(self) -> str:
        self.getInfo()
        return self.parseingData


if __name__ == "__main__":
    main = ZyXEL()
    print(main.getParseingData)
