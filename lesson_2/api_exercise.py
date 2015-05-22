#!/usr/bin/env python2.7

import json
import requests
import pprint


api_key = "2ea50d7dec0d069b494137ddf0ba253e"
base_url = "http://ws.audioscrobbler.com/2.0/?method=" 
method = "geo.getTopArtists"
country = "spain"
format = "json"

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.

    data = requests.get(url).text
    data = json.loads(data)
    print type(data)
    print data
    for index, artist in enumerate(data['topartists']['artist']):
        print "{}: {}".format(index +1, str(artist['name']))
        print "*" * 50

    return # return the top artist in Spain


def main():
    url = base_url + method + "&" + "country=" + country + "&" + "api_key=" + api_key +\
        "&" +"format=" + format
    print url
    api_get_request(url)

if __name__ == "__main__":
    main()