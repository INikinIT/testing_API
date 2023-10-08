from api.client import Client


class HttpBinApi(Client):
    BASE_URL = 'https://httpbin.org'
    HTML = '/html'
    ROBOTS = '/robots.txt'
    IP = '/ip'

    def list_html(self):
        url = self.BASE_URL + self.HTML
        return self.get(url)

    def robots_txt(self):
        url = self.BASE_URL + self.ROBOTS
        return self.get(url)

    def get_ip(self):
        url = self.BASE_URL + '/ip'
        return self.get(url)


http_bin_api = HttpBinApi()
