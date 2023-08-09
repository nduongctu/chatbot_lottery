from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests
import json
import feedparser

class action_get_lottery(Action):
   def name(self):
          return 'action_get_lottery'

   def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
            url_bac = 'https://xskt.com.vn/rss-feed/mien-bac-xsmb.rss'
            url_nam = 'https://xskt.com.vn/rss-feed/mien-nam-xsmn.rss'
            url_trung= 'https://xskt.com.vn/rss-feed/mien-trung-xsmt.rss'

            feed_bac = feedparser.parse(url_bac)
            first_node = feed_bac['entries']

            feed_nam = feedparser.parse(url_nam)
            first_node_nam = feed_nam['entries']

            feed_trung = feedparser.parse(url_trung)
            first_node_trung = feed_trung['entries']

            return_msg = first_node[0]['title'] + "\n" + first_node[0]['description']

            return_msg += "\n" + first_node_nam[0]['title'] + "\n" + first_node_nam[0]['description']

            return_msg += "\n" + first_node_trung[0]['title'] + "\n" + first_node_trung[0]['description']

            dispatcher.utter_message(return_msg)
            return []

class action_get_lottery_bac(Action):
   def name(self):
          return 'action_get_lottery_bac'

   def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
            url_bac = 'https://xskt.com.vn/rss-feed/mien-bac-xsmb.rss'


            feed_bac = feedparser.parse(url_bac)
            first_node = feed_bac['entries']

            return_msg = first_node[0]['title'] + "\n" + first_node[0]['description']

            dispatcher.utter_message(return_msg)
            return []

class action_get_lottery_trung(Action):
   def name(self):
          return 'action_get_lottery_trung'

   def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
            url_trung= 'https://xskt.com.vn/rss-feed/mien-trung-xsmt.rss'


            feed_trung = feedparser.parse(url_trung)
            first_node = feed_trung['entries']

            return_msg = first_node[0]['title'] + "\n" + first_node[0]['description']

            dispatcher.utter_message(return_msg)
            return []

class action_get_lottery_nam(Action):
   def name(self):
          return 'action_get_lottery_nam'

   def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
            url_nam = 'https://xskt.com.vn/rss-feed/mien-nam-xsmn.rss'

            feed_nam = feedparser.parse(url_nam)
            first_node = feed_nam['entries']

            return_msg = first_node[0]['title'] + "\n" + first_node[0]['description']

            dispatcher.utter_message(return_msg)
            return []