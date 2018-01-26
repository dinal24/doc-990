import requests

TOKEN_BASE_URL_PW = "https://ideabiz.lk/apicall/token?grant_type=password&username={0}&password={1}@123&scope={2}"
TOKEN_BASE_URL_RT = 'https://ideabiz.lk/apicall/token?grant_type=refresh_token&refresh_token={0}&scope={1}'

USERNAME = "Bot_messenger"
PASSWORD = "messenger"

SCOPE_SANDBOX = "SANDBOX"
SCOPE_PRODUCTION = "PRODUCTION"

GRANT_TYPE_PW = "password"
GRANT_TYPE_RT = "refresh_token"

B64_KEY_SANDBOX = "Basic WWVXcXl5M2d2TGRWWjhXa1U2clBZUGhsVmZvYTpnV2dfUHNTclQ1N3BrbG9oTVI2bVB0VnF4U2Nh"
B64_KEY_PRODUCTION = "Basic b0VURjNoeXRmaFc0ZzQwOXZaNkFZMEpVR3ZVYTpUb2V5bUhUR2xCQXo3YXZJZ21hWDJjVTNUUGth"

def get_token(scope=SCOPE_SANDBOX, grant_type=GRANT_TYPE_PW, **kwargs):
    if grant_type == GRANT_TYPE_PW:
        url = TOKEN_BASE_URL_PW.format(USERNAME, PASSWORD, scope)
    else:
        url = TOKEN_BASE_URL_RT.format(kwargs.get('rt'), scope)

    if scope == SCOPE_SANDBOX:
        headers = {
            "Authorization" : B64_KEY_SANDBOX,
            "Content-Type" : "application/x-www-form-urlencoded"
        }
    else:
        headers = {
            "Authorization": B64_KEY_PRODUCTION,
            "Content-Type": "application/x-www-form-urlencoded"
        }

    _response = requests.post(url, headers=headers)
    response = _response.json()
    return response.get('access_token'), response.get('refresh_token')

API_URL = "https://ideabiz.lk/apicall/docs/V2.0/{0}"

def get_all(access_token, ):
    url = API_URL.format('hospitals')
    headers = {
        'authorization': 'Bearer {}'.format(access_token),
        'accept': 'application/json',
        'access': 'BTF'

    }
    response = requests.get(url, headers=headers)
    response_json = response.json()
    print(response_json)


# get_token(grant_type=GRANT_TYPE_RT, rt='3f1b9670c58b8d5f377c5c36d54764')
# get_token()
# get_all_hospitals('4289686492ff37c6793dc8573e98e24c')