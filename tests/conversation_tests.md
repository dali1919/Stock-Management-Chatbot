## Ask about lid 

* greet: hello
  - utter_greet
* question_about_lid_check: how many lids ? 
  - action_lid_check
  - slot{"lid": "The lid amount is: 10"}
* thanks: Thanks
  - utter_thanks
* goodbye: bye    
  - utter_goodbye

## Ask about seedBags 

* greet: hello
  - utter_greet
* question_about_seedBag_check: how many seedBags ? 
  - action_seedBag_check
  - slot{"seedBags": "The seedBag ammount is: 10"}
* thanks: Thanks
  - utter_thanks
* goodbye: bye    
  - utter_goodbye

## Ask about paperCup 
* greet: hello
  - utter_greet
* question_about_paperCup_check: how many paperCup ? 
  - action_paperCup_check
  -rewind
  - slot{"paperCup": "The paperCup ammount is: 10"}
* thanks: Thanks
  - utter_thanks
* goodbye: bye    
  - utter_goodbye

## Ask about plasticCup 
* greet: hello
  - utter_greet
* question_about_plasticCup_check: how many plasticCup ? 
  - action_plasticCup_check
  - slot{"plasticCup": "The plasticCup ammount is: 10"}
* thanks: Thanks
  - utter_thanks
* goodbye: bye    
  - utter_goodbye 

## Ask about pallet 
* greet: hello
  - utter_greet
* question_about_pallet_check: how many pallet ? 
  - action_pallet_check
  - slot{"pallet": "The pallet ammount is: 10"}
* thanks: Thanks
  - utter_thanks
* goodbye: bye    
  - utter_goodbye 

