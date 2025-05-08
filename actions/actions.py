from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import random

vocabulary = {
    "apple": "яблоко",
    "dog": "собака",
    "cat": "кошка", 
    "house": "дом",
    "book": "книга",
    "water": "вода",
    "car": "машина",
    "computer": "компьютер",
    "world": "мир",
    "person": "человек",
    "school": "школа",
    "window": "окно",
    "door": "дверь",
    "hello": "привет",
    "goodbye": "до свидания",
    "thanks": "спасибо",
    "please": "пожалуйста",
    "friend": "друг",
    "food": "еда",
    "day": "день"
}

class ActionProvideWord(Action):
    def name(self) -> Text:
        return "action_provide_word"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      
        word = random.choice(list(vocabulary.keys()))
        translation = vocabulary[word]
        
       
        return [SlotSet("current_word", word), SlotSet("correct_translation", translation)]
        

class ActionCheckTranslation(Action):
    def name(self) -> Text:
        return "action_check_translation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        user_translation = next(tracker.get_latest_entity_values("translation"), None)
        current_word = tracker.get_slot("current_word")
        correct_translation = tracker.get_slot("correct_translation")
        
       
        if not user_translation:
          
            new_word = random.choice(list(vocabulary.keys()))
            new_translation = vocabulary[new_word]
            
            dispatcher.utter_message(text=f"I didn't catch your translation. Let's try another word: {new_word}")
            return [SlotSet("current_word", new_word), SlotSet("correct_translation", new_translation)]
        
      
        if user_translation.lower() == correct_translation.lower():
     
            new_word = random.choice(list(vocabulary.keys()))
            new_translation = vocabulary[new_word]
           
            dispatcher.utter_message(response="utter_correct", current_word=new_word)
            return [SlotSet("current_word", new_word), SlotSet("correct_translation", new_translation)]
        else:
            new_word = random.choice(list(vocabulary.keys()))
            new_translation = vocabulary[new_word]
            
        
            dispatcher.utter_message(response="utter_incorrect", 
                                    correct_translation=correct_translation,
                                    current_word=new_word)
            return [SlotSet("current_word", new_word), SlotSet("correct_translation", new_translation)]
