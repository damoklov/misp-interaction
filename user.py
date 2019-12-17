def get_user_input():
    key = input('Enter your MISP auth key: ').strip()
    url = input('Enter your MISP URL endpoint: ').strip()
    return key, url

