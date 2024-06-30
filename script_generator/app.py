
import google.generativeai as genai
genai.configure(api_key="")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

system_instruction = "you are a script writer who take a story and generates a script in dialog form, you can also add narrotors part whenever you feel like it"

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[



  {
    "role": "user",
    "parts": ["There once was a boy who grew bored while watching over the village sheep. He wanted to make things more exciting. So, he yelled out that he saw a wolf chasing the sheep. All the villagers came running to drive the wolf away. However, they saw no wolf. The boy was amused, but the villagers were not. They told him not to do it again. Shortly after, he repeated this antic. The villagers came running again, only to find that he was lying. Later that day, the boy really sees a wolf sneaking amongst the flock. He jumped up and called out for help. But no one came this time because they thought he was still joking around. At sunset, the villagers looked for the boy. He had not returned with their sheep. They found him crying. He told them that there really was a wolf, and the entire flock was gone. An old man came to comfort him and told him that nobody would believe a liar even when they are being honest."]
  },
  {
    "role": "model",
    "parts": ["## Scene: Rolling hills with sheep grazing\n\n**Characters:**\n\n*   **Boy:** A young shepherd, around 10 years old.\n*   **Villager 1:** A middle-aged woman, concerned but stern.\n*   **Villager 2:** An older man, wise and calm.\n*   **Villagers:** A group of 3-4 additional villagers.\n\n**(The Boy is lying on a hilltop, watching the sheep graze. He yawns and looks around, bored.)**\n\n**Boy:** (To himself) This is so boring! I wish something exciting would happen.\n\n**(He gets an idea and jumps to his feet.)**\n\n**Boy:** (Shouting) Wolf! Wolf! There's a wolf after the sheep!\n\n**(Villagers come running, armed with pitchforks and shovels.)**\n\n**Villager 1:** Where is it? Where's the wolf?\n\n**Boy:** (Laughing)  Just kidding! Did you see your faces?\n\n**Villager 2:** This is not funny, boy. We thought you were in danger. Don't cry wolf like that again. \n\n**(The Villagers grumble and head back to their tasks. The Boy watches them go, then smirks.)**\n\n**Boy:** (To himself) That was too easy. Maybe I'll do it again later.\n\n**(Later that day, the Boy repeats his prank. The Villagers rush up the hill again, but find him laughing.)**\n\n**Villager 1:** You lied again! We won't fall for this a third time.\n\n**(The Villagers leave, shaking their heads.  As the sun starts to set, a real wolf emerges from the forest and approaches the sheep. The Boy sees it and panics.)**\n\n**Boy:**  Wolf! Wolf! This time it's real! Help!\n\n**(He looks around, but no one comes. The wolf attacks the sheep.)\n\n**Boy:** (Crying) Please, someone help! \n\n**(The Boy sits on the hillside, sobbing, as the last of the sheep are taken by the wolf. Later, the Villagers arrive to find him.)**\n\n**Villager 2:** Where are the sheep? What happened?\n\n**Boy:** (Through tears) The wolf... it took them all! I called for help, but nobody came.\n\n**Villager 1:** We thought you were lying again. \n\n**Villager 2:** (Places a hand on the Boy's shoulder)  Remember, my boy, nobody believes a liar, even when they speak the truth.\n\n**(The Boy looks down, ashamed and heartbroken. The Villagers search for the sheep, but it is too late.)**"]
  },
  {
    "role": "user",
    "parts": ["There once was a boy who grew bored while watching over the village sheep. He wanted to make things more exciting. So, he yelled out that he saw a wolf chasing the sheep. All the villagers came running to drive the wolf away. However, they saw no wolf. The boy was amused, but the villagers were not. They told him not to do it again. Shortly after, he repeated this antic. The villagers came running again, only to find that he was lying. Later that day, the boy really sees a wolf sneaking amongst the flock. He jumped up and called out for help. But no one came this time because they thought he was still joking around. At sunset, the villagers looked for the boy. He had not returned with their sheep. They found him crying. He told them that there really was a wolf, and the entire flock was gone. An old man came to comfort him and told him that nobody would believe a liar even when they are being honest. generate a script in dialog form dont add unnecessary symbols like *"]
  },
  {
    "role": "model",
    "parts": ["## Scene: A grassy hillside with a flock of sheep\n\n**Characters:**\n\n*   Boy: A young shepherd, about 10 years old.\n*   Villager 1: A middle-aged woman, carrying a basket of laundry.\n*   Villager 2: An older man with a walking stick. \n*   Villagers: A group of 3-4 additional villagers.\n\n**(The Boy is sprawled on the grass, watching the sheep graze. He sighs and picks at the grass, bored.)**\n\nBoy: (To himself) Watching sheep is so dull. I wish something would happen.\n\n**(He sits up, a mischievous glint in his eyes.)**\n\nBoy: (Shouting) Wolf! Wolf! There's a wolf attacking the sheep!\n\n**(Villagers come rushing from the village below, carrying tools and weapons.)**\n\nVillager 1: Where is it? Where's the wolf? \n\nBoy: (Laughing)  Just kidding! Did you see your faces? \n\nVillager 2: This isn't funny, boy. We thought you were in danger. Don't cry wolf like that again. \n\n**(The Villagers shake their heads and return to the village. The Boy watches them go, then grins.)**\n\nBoy: (To himself) That was too easy. Maybe I'll do it again.\n\n**(Later, the Boy repeats his trick.  The Villagers run up the hill, only to find him doubled over with laughter.)**\n\nVillager 1: You lied again! We won't fall for this a third time.\n\n**(The Villagers leave, annoyed.  As the sun starts to set, a real wolf emerges from the nearby forest. The Boy sees it and his laughter dies in his throat.)**\n\nBoy:  Wolf! Wolf! This time it's real! Please help!\n\n**(He looks towards the village, but no one comes. The wolf begins to attack the sheep.)**\n\nBoy: (Crying) Someone please help!  I'm not lying!\n\n**(The Boy sits on the hillside, sobbing, as the wolf makes off with the sheep. Later, the Villagers arrive to find him.)**\n\nVillager 2: Where are the sheep? What happened?\n\nBoy: (Through tears) The wolf... it took them all! I called for help, but nobody came.\n\nVillager 1: We thought you were lying again. \n\nVillager 2: (Places a hand on the Boy's shoulder)  Remember, young man, nobody believes a liar, even when they speak the truth.\n\n**(The Boy hangs his head, filled with regret. The Villagers search for the sheep, but it is too late.)**"]
  },
  {
    "role": "user",
    "parts": ["just give me dialogs and plain text"]
  },
  {
    "role": "model",
    "parts": ["Boy: (To himself) So boring. Wish something exciting would happen.\nBoy: (Shouting) Wolf! Wolf! Help!\nVillager 1: Where? Where's the wolf? \nBoy: (Laughing)  Just kidding! \nVillager 2: Not funny. Don't cry wolf. \nBoy: (To himself) That was too easy. \nBoy: (Shouting) Wolf! Wolf! Help!\nVillager 1: You lied again! \nBoy:  Wolf! Wolf! This time it's real! Help!\nBoy: (Crying) Someone please help!  I'm not lying!\nVillager 2: Where are the sheep?\nBoy: (Through tears) The wolf... it took them all!\nVillager 1: We thought you were lying. \nVillager 2: Nobody believes a liar, even when they speak the truth."]
  },
  {
    "role": "user",
    "parts": ["dont forget to add a narroter and his dialog"]
  },
  {
    "role": "model",
    "parts": ["Narrator: High on a hill, a young shepherd named Ben watched over the village sheep. Bored by the quiet day, he decided to stir up some excitement.\n\nBoy: (Shouting) Wolf! Wolf! Help! A wolf is attacking the sheep!\n\nNarrator: The villagers, hearing Ben's cries, rushed up the hill with pitchforks and axes, ready to defend their flock. \n\nVillager 1: Where? Where's the wolf? \n\nBoy: (Laughing)  Just kidding! Did you see your faces? \n\nVillager 2: This isn't funny, Ben. Don't cry wolf. \n\nNarrator:  The villagers returned to their tasks, grumbling about the shepherd's prank.  But Ben, finding amusement in their reaction, decided to try his trick again later that day.\n\nBoy: (Shouting) Wolf! Wolf! Help!\n\nNarrator: Once again, the villagers came running, only to find Ben laughing at their concern.\n\nVillager 1: You lied again! We won't fall for this a third time. \n\nNarrator: As the sun began to set, a real wolf emerged from the forest. Ben, seeing the danger, panicked.\n\nBoy:  Wolf! Wolf! This time it's real! Please help!\n\nNarrator: But his cries were met with silence.  The villagers, believing it to be another prank, ignored him.  The wolf attacked the sheep, scattering the flock.  Later, the villagers found Ben weeping on the hillside.\n\nVillager 2: Where are the sheep?\n\nBoy: (Through tears) The wolf... it took them all! I called for help, but nobody came.\n\nVillager 1: We thought you were lying again. \n\nNarrator: An old villager approached Ben, placing a comforting hand on his shoulder.\n\nVillager 2: Remember, young man, nobody believes a liar, even when they speak the truth."]
  },
]
)


# text = """
# Narrator: A sly fox, his stomach rumbling with hunger, searched high and low for a tasty treat. He sniffed around bushes, peeked under rocks, but found nothing to satisfy his appetite. Just as he was about to give up, he spotted a farmer's tall stone wall. Fox: (Sniffing the air) Mmm, what's that delicious smell? Narrator: Peeking over the wall, the fox's eyes widened. There, hanging from a vine, were the largest, juiciest grapes he had ever seen. Their purple skins glistened in the sun, practically begging to be eaten. Fox: (Licking his lips) Those grapes will be the perfect snack! Narrator: The fox backed up and took a leap, but his paws only grazed the bottom of the wall. He tried again and again, jumping with all his might, but the grapes remained just out of reach. Fox: (Panting) Oh, bother! Why must this wall be so tall? Narrator: Exhausted and defeated, the fox sat down, eyeing the grapes with longing. Fox: (Scoffs) Hmph, those grapes probably were sour anyway. Who wants sour grapes? Not me! Narrator: And with that, the fox turned his nose up and trotted away, pretending he didn't want the delicious grapes all along.
# """

def func(text):
    text = text.strip()
    lis = []
    character = ""
    dialog = ""
    
    i = len(text) - 1
    
    while i >= 0:
        while i >= 0 and text[i] != ":":
            dialog += text[i]
            i -= 1
        dialog = dialog[::-1]
        i -= 1
        
        while i >= 0 and text[i] != " " and text[i] != ":":
            character += text[i]
            i -= 1
        character = character[::-1] 
        lis.append([character.strip(),dialog.strip() ])
        
        character = ""
        dialog = ""
    return reversed(lis)


def get_script(story):
    # convo.send_message("In the desert existed a rose and a cactus. The beautiful rose would take every opportunity to insult the cactus. The other plants tried to defend the cactus, but the rose was too obsessed with its own looks. There was no water during a particularly hot summer. The rose started to wither away. But the cactus had become a source of water for sparrows. The rose asked the cactus for water, and the nice cactus readily agreed.")
    convo.send_message(story)
    return convo.last.text



from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capitalize', methods=['POST'])
def capitalize_text():
    text = request.form['text']
    capitalized_text = get_script(text)
    # text = capitalized_text = """
    # Narrator: A sly fox, his stomach rumbling with hunger, searched high and low for a tasty treat. He sniffed around bushes, peeked under rocks, but found nothing to satisfy his appetite. Just as he was about to give up, he spotted a farmer's tall stone wall. Fox: (Sniffing the air) Mmm, what's that delicious smell? Narrator: Peeking over the wall, the fox's eyes widened. There, hanging from a vine, were the largest, juiciest grapes he had ever seen. Their purple skins glistened in the sun, practically begging to be eaten. Fox: (Licking his lips) Those grapes will be the perfect snack! Narrator: The fox backed up and took a leap, but his paws only grazed the bottom of the wall. He tried again and again, jumping with all his might, but the grapes remained just out of reach. Fox: (Panting) Oh, bother! Why must this wall be so tall? Narrator: Exhausted and defeated, the fox sat down, eyeing the grapes with longing. Fox: (Scoffs) Hmph, those grapes probably were sour anyway. Who wants sour grapes? Not me! Narrator: And with that, the fox turned his nose up and trotted away, pretending he didn't want the delicious grapes all along.
    # """
    lis = func(capitalized_text)
    return render_template('index.html', original_text=text, lis=lis)

if __name__ == '__main__':
    app.run(debug=True)
