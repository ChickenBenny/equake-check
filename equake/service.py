import time
import requests
from equake.models import EquakeData


class Service:
    def __init__(self, num_of_data: int = 5):
        self._year = time.strftime('%Y', time.localtime())
        self._month = time.strftime('%m', time.localtime())
        self._url = 'https://scweb.cwa.gov.tw/zh-tw/earthquake/ajaxhandler'
        self._headers = {
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        
        self._data = {
            'draw': '3',
            'columns[0][data]': '0',
            'columns[0][name]': 'EventNo',
            'columns[0][searchable]': 'false',
            'columns[0][orderable]': 'true',
            'columns[0][search][value]': '',
            'columns[0][search][regex]': 'false',
            'columns[1][data]': '1',
            'columns[1][name]': 'MaxIntensity',
            'columns[1][searchable]': 'true',
            'columns[1][orderable]': 'true',
            'columns[1][search][value]': '',
            'columns[1][search][regex]': 'false',
            'columns[2][data]': '2',
            'columns[2][name]': 'OriginTime',
            'columns[2][searchable]': 'true',
            'columns[2][orderable]': 'true',
            'columns[2][search][value]': '',
            'columns[2][search][regex]': 'false',
            'columns[3][data]': '3',
            'columns[3][name]': 'MagnitudeValue',
            'columns[3][searchable]': 'true',
            'columns[3][orderable]': 'true',
            'columns[3][search][value]': '',
            'columns[3][search][regex]': 'false',
            'columns[4][data]': '4',
            'columns[4][name]': 'Depth',
            'columns[4][searchable]': 'true',
            'columns[4][orderable]': 'true',
            'columns[4][search][value]': '',
            'columns[4][search][regex]': 'false',
            'columns[5][data]': '5',
            'columns[5][name]': 'Description',
            'columns[5][searchable]': 'true',
            'columns[5][orderable]': 'true',
            'columns[5][search][value]': '',
            'columns[5][search][regex]': 'false',
            'columns[6][data]': '6',
            'columns[6][name]': 'Description',
            'columns[6][searchable]': 'true',
            'columns[6][orderable]': 'true',
            'columns[6][search][value]': '',
            'columns[6][search][regex]': 'false',
            'order[0][column]': '2',
            'order[0][dir]': 'desc',
            'start': '0',
            'length': num_of_data,
            'search[value]': '',
            'search[regex]': 'false',
            'Search': f'{self._year}年{self._month}月',
            'txtSDate': '',
            'txtEDate': '',
            'txtSscale': '',
            'txtEscale': '',
            'txtSdepth': '',
            'txtEdepth': '',
            'txtLonS': '',
            'txtLonE': '',
            'txtLatS': '',
            'txtLatE': '',
            'ddlCity': '',
            'ddlTown': '',
            'ddlCitySta': '',
            'ddlStation': '',
            'txtIntensityB': '',
            'txtIntensityE': '',
            'txtLon': '',
            'txtLat': '',
            'txtKM': '',
            'ddlStationName': '------',
            'cblEventNo': '',
            'txtSDatePWS': '',
            'txtEDatePWS': '',
            'txtSscalePWS': '',
            'txtEscalePWS': '',
            'ddlMark': ''
        }


    def _get_headers(self):
        return self._headers

    def _get_data(self):
        return self._data
    
    def _get_url(self) -> str:
        return self._url

    def _request_earthquake_data(self):
        response = requests.post(
            url=self._get_url(),
            headers=self._get_headers(),
            data=self._get_data()
        )
        return response.json() if response.status_code == 200 else None
    
    def _process_earthquake_data(self, data: dict):
        equake_data = data['data']
        return [
            EquakeData(
                datatime_in_tw=data[2],
                scale=data[3],
                depth=data[4],
                location=data[5]
            ) for data in equake_data
        ]
    
    def get_data(self):
        data = self._request_earthquake_data()
        return self._process_earthquake_data(data) if data else None
    