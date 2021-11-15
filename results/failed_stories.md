## Ask about lid (C:\Users\Dali\AppData\Local\Temp\tmpec8kveo_\111f1c3d5bb24f7fa869da27efd03d79_conversation_tests.md)
* greet: hello
    - utter_greet
* question_about_lid_check: how many lids ?
    - action_lid_check   <!-- predicted: utter_goodbye -->
    - slot{"lid": "The lid amount is: 10"}
* thanks: Thanks
    - utter_thanks
* goodbye: bye
    - utter_goodbye


## Ask about seedBags (C:\Users\Dali\AppData\Local\Temp\tmpec8kveo_\111f1c3d5bb24f7fa869da27efd03d79_conversation_tests.md)
* greet: hello
    - utter_greet
* question_about_seedBags_check: how many seedBags ?   <!-- predicted: question_about_seedBag_check: how many seedBags ? -->
    - action_seedBag_check   <!-- predicted: utter_affirm -->
    - slot{"seedBags": "The seedBag ammount is: 10"}
* thanks: Thanks
    - utter_thanks
* goodbye: bye
    - utter_goodbye


## Ask about paperCup (C:\Users\Dali\AppData\Local\Temp\tmpec8kveo_\111f1c3d5bb24f7fa869da27efd03d79_conversation_tests.md)
* greet: hello
    - utter_greet
* question_about_paperCup_check: how many paperCup ?   <!-- predicted: out_of_scope: how many [paperCup](ORG) ? -->
    - action_paperCup_check   <!-- predicted: utter_affirm -->
    - slot{"paperCup": "The paperCup ammount is: 10"}
* thanks: Thanks
    - utter_thanks
* goodbye: bye
    - utter_goodbye


## Ask about plasticCup (C:\Users\Dali\AppData\Local\Temp\tmpec8kveo_\111f1c3d5bb24f7fa869da27efd03d79_conversation_tests.md)
* greet: hello
    - utter_greet
* question_about_plasticCup_check: how many plasticCup ?   <!-- predicted: out_of_scope: how many [plasticCup](ORG) ? -->
    - action_plasticCup_check   <!-- predicted: utter_affirm -->
    - slot{"plasticCup": "The plasticCup ammount is: 10"}
* thanks: Thanks
    - utter_thanks
* goodbye: bye
    - utter_goodbye


## Ask about pallet (C:\Users\Dali\AppData\Local\Temp\tmpec8kveo_\111f1c3d5bb24f7fa869da27efd03d79_conversation_tests.md)
* greet: hello
    - utter_greet
* question_about_pallet_check: how many pallet ?
    - action_pallet_check   <!-- predicted: utter_affirm -->
    - slot{"pallet": "The pallet ammount is: 10"}
* thanks: Thanks
    - utter_thanks
* goodbye: bye
    - utter_goodbye


