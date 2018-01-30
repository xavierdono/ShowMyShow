import requests

from Show import Show

class APIShow:
    def __init__(self):
        self.URL = 'http://api.tvmaze.com'

    def has_attribute(data, attr):
        return attr in data and data[attr] is not None
        
    def search(self, showName):
        lstShow = []
        resp = requests.get(self.URL + '/search/shows?q={}'.format(showName))

        if resp.status_code != 200:
            return None
        
        for show in resp.json():
            id = show['show']['id']
            name = show['show']['name']
            image = show['show']['image']['medium'] if APIShow.has_attribute(show['show'], 'image') else ""
            
            s = Show(id, name, image)
            lstShow.append(s)
        
        return lstShow
    
    def get_show(self, idShow):
        show = Show()
        
        return show
