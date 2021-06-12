import requests_mock
import utils


def test_web_request():
    with requests_mock.Mocker() as mock_request:
        mock_request.get('http://localhost', text='data')
        x = utils.web_request()

    assert 'data' == x
