import requests
from bs4 import BeautifulSoup


URL_TEMPLATE = 'http://www2.alleghenycounty.us/RealEstate/GeneralInfo.aspx?ParcelID='

def get_owner_name(parcel_id):
    print(parcel_id)
    owner_name = ''
    r = requests.get(URL_TEMPLATE+parcel_id);
    try:
        if (r.ok):
            soup = BeautifulSoup(r.text, 'html.parser')
            thing = soup.find_all(id='BasicInfo1_lblOwner')
            owner_name = ' '.join(thing[0].text.split())

    finally:
        return owner_name
