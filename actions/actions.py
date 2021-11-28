# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionKonsonan(Action):

    def name(self) -> Text:
        return "action_tanya_vokal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        vokal = tracker.get_slot("vokal")
        if not vokal:
            dispatcher.utter_message(text= "Huruf yang dimaksud tidak termasuk huruf vokal !")
        else:
            dispatcher.utter_message(text= "Huruf {} termasuk huruf vokal !".format(vokal))
        return [SlotSet("vokal")]
