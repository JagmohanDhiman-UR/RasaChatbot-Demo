from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_core_sdk.events import SlotSet
from datetime import datetime

from rasa_sdk.forms import FormAction
# def fetchingJWTToken(username,password):

return_slots = []

# class Action_from_date(Action):

#     def name(self):
#         return "action_from_date"

#     def run(self, dispatcher, tracker, domain):
#         message = tracker.latest_message.get('text')
#         return [SlotSet('from_date', message)]

# class Action_to_date(Action):

#     def name(self):
#         return "action_to_date"

#     def run(self, dispatcher, tracker, domain):
#         message = tracker.latest_message.get('text')
#         return [SlotSet('to_date', message)]


class Action_transaction_status(Action):

    def name(self):
        return "action_transaction_status"

    def run(self, dispatcher, tracker, domain):
        transactionID=tracker.get_slot('transactionID')
        dispatcher.utter_message("This is your Transaction status for {} is : XXX".format(transactionID))

class Action_transaction_summary(Action):

    def name(self):
        return "action_transaction_summary"

    def run(self, dispatcher, tracker, domain):
        f_d=tracker.get_slot('from_date')
        # print(f_d)
        from_date=datetime.strptime(f_d,'%m-%d-%Y')
        t_d=tracker.get_slot('to_date')
        # print(t_d)
        to_date=datetime.strptime(t_d,"%m-%d-%Y")
        dispatcher.utter_message("This is your transaction summarry from {} to {}".format(from_date.date(),to_date.date()))

class ActionSlotReset(Action): 	
    def name(self): 		
        return 'action_slot_reset' 	
    def run(self, dispatcher, tracker, domain): 
        for slot in tracker.slots:
            return_slots.append(SlotSet(slot, None))
        return return_slots

class SummaryForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""
        return "summary_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["from_date", "to_date"]
    
    def slot_mappings(self):
        return {
        "from_date": self.from_entity(entity="date"),
        "to_date": self.from_entity(entity="date")}
    
    def validate_from_date(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        print("came for validation of from date")
        try:
            return {"from_date": value}
        except:
            dispatcher.utter_message(template="utter_wrong_date_format")
            return {"from_date": None}

        # if self.is_int(value) and int(value) > 0:
        #     return {"num_people": value}
        # else:
        #     dispatcher.utter_message(template="utter_wrong_num_people")
        #     # validation failed, set slot to None
        #     return {"num_people": None}

    def validate_to_date(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        print("came for validation of from date")
        try:
            to_date=datetime.strptime(value,'%m-%d-%Y')
            from_date=datetime.strptime(tracker.get_slot('from_date'),'%m-%d-%Y')
            if from_date>to_date:
                dispatcher.utter_template('utter_wrong_date', tracker)
                return {"from_date": None,"to_date": None}
            else:
                return {"to_date": value}
        except:
            dispatcher.utter_template('utter_wrong_date_format', tracker)
            return {"to_date": None}

        # if self.is_int(value) and int(value) > 0:
        #     return {"num_people": value}
        # else:
        #     dispatcher.utter_message(template="utter_wrong_num_people")
        #     # validation failed, set slot to None
        #     return {"num_people": None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        # dispatcher.utter_template('utter_submit', tracker)
        return []

class TransactionForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "transaction_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["transactionID"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        # dispatcher.utter_template('utter_submit', tracker)
        return []
