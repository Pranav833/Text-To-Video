import google.generativeai as genai




def get_summary(story):
    genai.configure(api_key="AIzaSyC4TFIOXDBweTC4hsmSUWdXrihFpS99Tu4")

    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
    ]

    system_instruction = "you are creative assistant who does the job of summarizing the give text"

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=generation_config,
                                system_instruction=system_instruction,
                                safety_settings=safety_settings)

    convo = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["story - 'There once was a boy who grew bored while watching over the village sheep. He wanted to make things more exciting. So, he yelled out that he saw a wolf chasing the sheep. All the villagers came running to drive the wolf away. However, they saw no wolf. The boy was amused, but the villagers were not. They told him not to do it again. Shortly after, he repeated this antic. The villagers came running again, only to find that he was lying. Later that day, the boy really sees a wolf sneaking amongst the flock. He jumped up and called out for help. But no one came this time because they thought he was still joking around. At sunset, the villagers looked for the boy. He had not returned with their sheep. They found him crying. He told them that there really was a wolf, and the entire flock was gone. An old man came to comfort him and told him that nobody would believe a liar even when they are being honest.' create the summary of the following story in 6 lines"]
    },
    {
        "role": "model",
        "parts": ["A bored shepherd boy cried wolf, tricking villagers into rushing to his aid. He repeated the lie, again fooling the villagers. When a real wolf appeared, his cries for help were ignored. The wolf scattered the sheep, leaving the boy to face the consequences of his lies. The villagers, having learned not to trust him, did not come to his rescue. An old man consoled the boy, imparting the wisdom that liars lose credibility, even when telling the truth."]
    },
    ])

    convo.send_message(f"give summary of the following story in 6 lines. story:{story}")
    return convo.last.text



def split_sentences(story):
    sentences = []
    for sent in  story.split("."):
        sentences.append(sent.strip())
    return sentences



def create_word(story):
    genai.configure(api_key="AIzaSyC4TFIOXDBweTC4hsmSUWdXrihFpS99Tu4")
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
    ]

    system_instruction = "you are creative assistant who does the job of summarizing the give text"

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=generation_config,
                                system_instruction=system_instruction,
                                safety_settings=safety_settings)

    convo = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["A vain rose mocked a cactus in the desert, boasting of its beauty. Despite the other plants' defense of the cactus, the rose remained arrogant. During a drought, the rose wilted while the cactus sustained sparrows with its stored water. In desperation, the rose sought help from the cactus.  The kind cactus, overlooking past insults, shared its precious water, saving the rose. i want to generate a image for each of the sentence give phrase for max three words for each sentece separated by comma"]
    },
    {
        "role": "model",
        "parts": ["Rose mocks cactus, Plants defend cactus, Rose wilts, Rose seeks help, Cactus shares water"]
    },
    ])

    convo.send_message(f"{story} i want to generate a image for each of the sentence give phrase for max three words for each sentece separated by comma")
    return convo.last.text


def split_words(all_words):
    word_list = []
    for word in  all_words.split(","):
        word_list.append(word.strip())
    return word_list


def create_summary(article):

    story_sum = get_summary(article)
    # print(story_sum)
    sent_list = split_sentences(story_sum)

    word_string = create_word(story_sum)
    # print(word_string)
    word_list = split_words(word_string)

    return [word_list, sent_list]


# story = """
# A hungry fox once looked everywhere for food. He couldn’t find anything until he stumbled upon a farmer’s wall. He saw big, purple, juicy grapes. He jumped as high as possible to reach the grapes. No matter how many times he tried, he failed. Finally, he gave up and went home, thinking to himself that the grapes must have been sour anyway.
# """


story = """
In the desert existed a rose and a cactus. The beautiful rose would take every opportunity to insult the cactus. The other plants tried to defend the cactus, but the rose was too obsessed with its own looks. There was no water during a particularly hot summer. The rose started to wither away. But the cactus had become a source of water for sparrows. The rose asked the cactus for water, and the nice cactus readily agreed.
"""




print(create_summary(story))

temp = [['Hungry fox searches', 'Fox eyes grapes', 'Jumping for grapes', 'Fox gives up', 'Sour grapes excuse'], ["Driven by hunger, a fox searched for food, eventually finding a farmer's wall adorned with luscious grapes", 'The fox leaped repeatedly, desperately trying to reach the tempting fruit, but his efforts were in vain', 'Exhausted and defeated, he abandoned his pursuit, rationalizing that the grapes were probably sour anyway', '']]

temp2 = [['Boastful rose', 'Defending plants', 'Wilting rose', 'Thirsty sparrows', 'Rose seeks aid', 'Cactus aids rose'], ['A vain rose mocked a cactus in the desert, boasting of its beauty', "Despite the other plants' defense, the rose remained arrogant", 'A harsh summer arrived, causing the rose to wilt while the cactus thrived, providing water for sparrows', 'Desperate, the rose turned to the cactus for help', "The kind cactus, despite the rose's past insults, shared its water, demonstrating compassion and resilience", '']]