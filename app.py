# -*- coding: utf-8 -*-
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import apikeys
import buzzer


class StdOutListener(StreamListener):
    def on_data(self, data):
        DataParser().convert(data)
        return True

    def on_error(self, status):
        print(status)


class DataParser:
    def convert(self, data):
        jso = json.loads(data)
        if "entities" in jso:
            if "media" in jso['entities']:
                pass
        try:
            user = jso['user']['screen_name']
            text = jso['text']
            date = jso['created_at']
            print(text)
            buzzer.times(1)
        except Exception as e:
            print("Error 123", e)


if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(apikeys.consumer_key, apikeys.consumer_secret)
    auth.set_access_token(apikeys.access_token, apikeys.access_token_secret)
    stream = Stream(auth, listener)

    # stream.filter(track=['#TenemosSismo', '#sasmex', '#TenemosAlerta', '#AlertaSísmica'])
    stream.filter(track=['#MORENAGobiernaMal'])
