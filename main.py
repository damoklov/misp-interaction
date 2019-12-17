from user import get_user_input
from create_event import create
from fetch_events import fetch

if __name__ == '__main__':
    KEY, URL = get_user_input()
    create(URL, KEY)
    fetch(URL, KEY)
