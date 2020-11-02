# coding=utf-8
import requests

# connect API from url
URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'

# unique key you can get on site
KEY = 'YjYzOGQ0NWItYWZjYi00OTY0LWFkMWEtM2RmNGRkOTM2ZDEyOmM1MzRlNzBhNTkyODQ0ZTY4MGVmMTQyMjA3ZThmZGVi'

# authorization
headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)

# check for success of auth
if auth.status_code == 200:
    token = auth.text

    # translator while true loop
    while True:
        word = raw_input('')
        if word:
            headers_translate = {
                'Authorization': 'Bearer ' + token
            }
            params = {
                'text': word,
                'srcLang': 1033,
                'dstLang': 1049
            }
            r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
            res = r.json()
            try:
                print(res['Translation']['Translation'])
            finally:
                print('translation not found')

else:
    print('ERROR')