import requests


class FetchData:

    def __init__(self, url):
        self.url = url

    def fetch(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                print('Successfully fetched data\n')
                print(f'data {response.text}')
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
        # return None


if __name__ == '__main__':
    fetch_data = FetchData('https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&pageNo=58&pageSize=30&systemType=PC')
    fetch_data.fetch()