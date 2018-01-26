import requests, datetime

BASE_URL = "https://ideabiz.lk/apicall/docs/V2.0/{}"

headers = {
    'authorization': "Bearer {}",
    'accept': "application/json",
    'access': "BTF",
    'cache-control': "no-cache"
}

def get_hospital_list(key):
    try:
        headers['authorization'] = headers['authorization'].format(key)
        url = BASE_URL.format('hospitals')
        _response = requests.get(url, headers=headers)
        response = _response.json()
        return response
    except Exception as error:
        print('Caught this error: ' + repr(error))

def get_doctor_list(key):
    try:
        headers['authorization'] = headers['authorization'].format(key)
        url = BASE_URL.format('doctors')
        _response = requests.get(url, headers=headers)
        response = _response.json()
        return response
    except Exception as error:
        print('Caught this error: ' + repr(error))

def get_specialization_list(key):
    try:
        headers['authorization'] = headers['authorization'].format(key)
        url = BASE_URL.format('specializations')
        _response = requests.get(url, headers=headers)
        response = _response.json()
        return response
    except Exception as error:
        print('Caught this error: ' + repr(error))

def get_payment_methods(key):
    try:
        headers['authorization'] = headers['authorization'].format(key)
        url = BASE_URL.format('payment-methods')
        _response = requests.get(url, headers=headers)
        response = _response.json()
        return response
    except Exception as error:
        print('Caught this error: ' + repr(error))

def get_doctors_by_name(key, name_guess):
    params = {
        'doctor' : name_guess
    }
    try:
        headers['authorization'] = headers['authorization'].format(key)
        url = BASE_URL.format('hospital-doctors')
        _response = requests.get(url, headers=headers, params=params)
        response = _response.json()
        return response
    except Exception as error:
        print('Caught this error: ' + repr(error))

# Todo: Add time limits
def get_session_by_doctor_hospital(key, doc_id, hospital_id):
    params = {
        'doctor' : doc_id,
        'hospital' : hospital_id,
        'to' : (datetime.datetime.today() + datetime.timedelta(days=7)).date().strftime("%d.%m.%Y")
    }
    try:
        headers['authorization'] = headers['authorization'].format(key)
        url = BASE_URL.format('doctor-sessions')
        _response = requests.get(url, headers=headers, params=params)
        response = _response.json()
        return response
    except Exception as error:
        print('Caught this error: ' + repr(error))

# Just to check availability from the backend. continue to payment
def get_session_availability(key, session_id):
    try:
        headers['authorization'] = headers['authorization'].format(key)
        url = BASE_URL.format('doctor-sessions' + '/' + session_id)
        _response = requests.get(url, headers=headers)
        response = _response.json()
        return response
    except Exception as error:
        print('Caught this error: ' + repr(error))

# Store the session after checking session availability
def store_session(key, session_id, *args):
    try:
        headers['authorization'] = headers['authorization'].format(key)
        url = BASE_URL.format('/appointments/store')
        _response = requests.get(url, headers=headers)
        response = _response.json()
        return response
    except Exception as error:
        print('Caught this error: ' + repr(error))

def complete_session(key, session_id, *args):
    try:
        headers['authorization'] = headers['authorization'].format(key)
        url = BASE_URL.format('/appointments/store')
        _response = requests.get(url, headers=headers)
        response = _response.json()
        return response
    except Exception as error:
        print('Caught this error: ' + repr(error))

def confirm_session(key, session_id, *args):
    try:
        headers['authorization'] = headers['authorization'].format(key)
        url = BASE_URL.format('/appointments/store')
        _response = requests.get(url, headers=headers)
        response = _response.json()
        return response
    except Exception as error:
        print('Caught this error: ' + repr(error))

