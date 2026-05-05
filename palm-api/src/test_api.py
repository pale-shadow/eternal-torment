"""
At the command line, only need to run once to install the package via pip:
$ pip install google-generativeai
"""

import google.generativeai as palm

palm.configure(api_key="YOUR API KEY")

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.95,
  'candidate_count': 5,
  'top_k': 40,
  'top_p': 0.95,
}
context = ""
examples = [
  [
    "Talk to American revolutionary war cavalry expert.",
    "I dress like Casimir Pulaski because I am a deep well of equine facts."
  ]
]
messages = [
  "How long does it take to properly train a horse for war? ",
  "The amount of time it takes to properly train a horse for war can vary depending on the horse's individual temperament and abilities, as well as the level of training required. In general, however, it can take anywhere from six months to a year or more to train a horse for war.\n\nThe first step in training a horse for war is to establish a solid foundation of obedience and trust. This means teaching the horse basic commands, such as \"whoa,\" \"stop,\" and \"go,\" as well as how to respond to cues from the rider's body language. It is also important to socialize the horse so that it is comfortable around other horses and people.\n\nOnce the horse has a good foundation of obedience and trust, the next step is to begin training it for specific tasks that it will need to perform in battle. This may include things like charging into battle, carrying a rider and equipment, and responding to gunfire. It is important to be patient and consistent during this stage of training, as it can take some time for the horse to learn and master these tasks.\n\nFinally, once the horse has been trained in the specific tasks that it will need to perform in battle, it is important to put it through a series of tests to ensure that it is ready for combat. These tests may include things like simulating battle conditions, such as loud noises and gunfire. It is important to make sure that the horse is able to handle these conditions without becoming stressed or panicked.\n\nTraining a horse for war is a complex and challenging process, but it is essential for ensuring the safety of both the horse and its rider. By following these steps, you can help to ensure that your horse is properly prepared for the rigors of battle.",
  "How many horses did the American Colonies train for the revolutionary war? ",
  "The American Colonies used an estimated 40,000 horses during the Revolutionary War. These horses were used for a variety of purposes, including transportation, communication, and combat.\r\n\r\nHorses were essential for transporting supplies and troops across the vast distances of the American colonies. They were also used to carry messages and dispatches between different parts of the army. In battle, horses were used to charge enemy lines, carry cannons and supplies, and transport wounded soldiers.\r\n\r\nThe American Colonies were able to obtain horses from a variety of sources. Some were captured from the British, while others were purchased from local farmers. The Continental Congress also set up a system of horse requisitions, which required all able-bodied men to provide horses for the war effort.\r\n\r\nThe use of horses during the Revolutionary War had a significant impact on the course of the conflict. Horses allowed the American army to move quickly and efficiently, and they were essential for carrying out many of the key military operations of the war.",
  "Did the French assist the Americans in the revolutionary war? ",
  "Yes, the French provided significant assistance to the Americans during the Revolutionary War. They provided money, supplies, and troops, which helped to turn the tide of the war in the Americans' favor.\n\nThe French had a number of reasons for wanting to help the Americans. They were eager to weaken their longtime rival, Great Britain. They also believed in the ideals of the American Revolution and wanted to see a new, independent nation emerge in North America.\n\nThe French began providing assistance to the Americans in 1776, even before the Declaration of Independence was signed. They sent a small fleet of ships to the American colonies and provided supplies and money. In 1778, France officially entered the war on the side of the Americans.\n\nThe French intervention was a major turning point in the war. The French fleet helped to prevent the British from taking control of the American coast, and the French army helped to defeat the British at the Battle of Saratoga. These victories gave the Americans hope and confidence, and they helped to persuade other European nations to support the American cause.\n\nThe French continued to provide assistance to the Americans until the war ended in 1783. Their help was essential to the American victory, and it helped to ensure the independence of the United States of America.",
  "Did the Polish assist America in the Revolutionary War? ",
  "Yes, the Polish assisted the Americans in the Revolutionary War. Most notably, Casimir Pulaski, a Polish nobleman and military commander, fought on the side of the Americans and was instrumental in the Continental Army's victory at the Battle of Savannah.\n\nPulaski was born in 1745 into a noble Polish family. He joined the Polish army at a young age and quickly rose through the ranks. He fought in the Polish-Russian War of 1768-1772, and after the war, he went into exile in France.\n\nIn 1777, Pulaski met Benjamin Franklin in Paris. Franklin was on a mission to seek support for the American Revolution from European powers. Pulaski was inspired by the American cause, and he decided to offer his services to the Continental Army.\n\nPulaski arrived in America in 1778. He was appointed a brigadier general in the Continental Army, and he quickly proved to be a valuable asset. He was a skilled military commander, and he was also a charismatic leader. He was known for his bravery and his willingness to fight on the front lines.\n\nPulaski's most notable contribution to the American Revolution was his role in the Battle of Savannah. In December 1779, the Continental Army launched an attack on the British-held city of Savannah. The attack was initially successful, but the British were able to counterattack and drive the Americans back. Pulaski was wounded in the battle, and he died a few days later.\n\nPulaski's death was a great loss to the American cause. He was a brave and skilled soldier, and he was a true friend to the American people. His legacy is one of courage, determination, and sacrifice."
]
messages.append("NEXT REQUEST")
response = palm.chat(
  **defaults,
  context=context,
  examples=examples,
  messages=messages
)
print(response.last) # Response of the AI to your most recent request