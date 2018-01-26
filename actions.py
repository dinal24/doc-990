import fields, utility

def match():
    pass

# step 1
def find_doctor_by_name(doc_name):
    # exact/partial matches suggest
    # No matches prompt to renter
    at, rt = utility.get_token()
    result = fields.get_doctors_by_name(at, doc_name)
    count, doctors = result.get("response").get('count', 0), result.get("response").get('doctors', [])
    if count < 1:
        pass
    elif 0 < count < 10:
        pass
    else:
        pass

    return

# step 1.1
def know_more_doctor(doc_name, doc_id):
    at, rt = utility.get_token()
    result = fields.get_doctors_by_name(at, doc_name)
    count, doctors = result.get("response").get('count', 0), result.get("response").get('doctors', [])
    if count < 1:
        pass
    elif count == 1:
        pass
    else:
        pass

    return

# step 2
def hospital_for_doctor(doc_name, doc_id):
    at, rt = utility.get_token()
    result = fields.get_doctors_by_name(at, doc_name)
    count, doctors = result.get("response").get('count', 0), result.get("response").get('doctors', [])
    if count < 1:
        pass
    elif count == 1:
        pass
    else:
        pass

    return

# step 3
def date_for_doctor_hospital(doc_id, hospital_id):
    at, rt = utility.get_token()
    result = fields.get_session_by_doctor_hospital(at, doc_id, hospital_id)
    count, doctors = result.get("response").get('count', 0), result.get("response").get('doctors', [])
    if count < 1:
        pass
    elif count == 1:
        pass
    else:
        pass

    return

# step 3 : show invoice
def check_availability_and_confirm(session_id):
    pass

# step 4
def payment_gateway():
    pass
