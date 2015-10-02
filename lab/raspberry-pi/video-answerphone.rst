Handless answerphone
====================

Here, we will describe step by step how to build a answerphone
handless and video based. The control flow is as follows:

 1. The device wait to see a new person in front 
 2. If nobody is there, run a small tagline as "come on"
 3. When a face is detected, find the identity of the person
 4. Play all messages for this person (if any)
 5. When no message lefts, propose to leave a new message
 6. Record the message until "stop" is said
 7. Ask confirmation
 8. Ask the recipient
 9. Store the identity, the recipient and the date
 10. Say goodbye


