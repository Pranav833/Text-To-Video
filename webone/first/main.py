# from openai import OpenAI
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from gtts import gTTS
from moviepy.editor import VideoClip, concatenate_videoclips, AudioFileClip, ImageSequenceClip, TextClip, CompositeVideoClip, vfx
from PIL import Image
import os
from moviepy.editor import concatenate_audioclips
from moviepy.editor import ImageClip
from moviepy.audio.fx import audio_fadein, audio_fadeout
from moviepy.editor import *
from django.core.files.storage import default_storage
from urllib.parse import urljoin
import urllib.request
import google.generativeai as genai



api_key_1 = ""
api_key_2 = ""
import fitz

def text_transform(text):
    a = text
    a = a.replace(' ','')
    a = a.replace('?', '')
    a = a.replace('.', '')
    a = a.replace('!', '')
    a = a.replace('\"', '')
    return a

def extract_text_from_pdf(pdf_file_path):
    text = ""
    try:
        pdf_file_path = "media/" + pdf_file_path
        with fitz.open(pdf_file_path) as pdf_document:
            for page_num in range(pdf_document.page_count):
                page = pdf_document.load_page(page_num)
                text += page.get_text()
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    return text

def text_to_audio(text):
    tts = gTTS(text=text, lang='en', slow = False)
    tts.save('./audio/'+text_transform(text) + ".mp3")
    return tts


# def get_words(sentences):
#     prompt = f"{sentences}\n give subject/import noun or meaning (in maximum 2 words) for each sentence and give numbering for each line"
#     def get_completion(prompt, model="gpt-3.5-turbo"):
#         messages = [{"role": "user", "content": prompt}]
#         completion = client.chat.completions.create(
#             model=model, messages=messages, temperature=0,
#         )
#         return completion.choices[0].message.content
    
#     answer = get_completion(prompt)
#     print(f"IMP = \n{answer}")

#     words = answer.strip().split('\n')
#     words_array = [line.split(' ', 1)[1].strip() for line in words]
#     words_set = set()
#     words_array = [x for x in words_array if x not in words_set and not words_set.add(x)]
#     return words_array



# def create_summary(article):
#     prompt = f"{article}\n summerize this into 10 lines and give numbering for each line "
#     # print(prompt)

#     def get_completion(prompt, model="gpt-3.5-turbo"):
#         messages = [{"role": "user", "content": prompt}]
#         completion = client.chat.completions.create(
#             model=model, messages=messages, temperature=0,
#         )
#         return completion.choices[0].message.content

#     answer = get_completion(prompt)
#     print(f"English = \n{answer}")

#     imp_words = get_words(answer)

#     sentences = answer.strip().split('\n')
#     sent_array = [line.split(' ', 1)[1].strip() for line in sentences]
#     sent_set = set()
#     sent_array = [x for x in sent_array if x not in sent_set and not sent_set.add(x)]

#     return [imp_words,sent_array]







def get_summary(story):
    genai.configure(api_key=api_key_1)

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
    genai.configure(api_key=api_key_1)
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

    # temp = [['Hungry fox searches', 'Fox eyes grapes', 'Jumping for grapes', 'Fox gives up', 'Sour grapes excuse'], ["Driven by hunger, a fox searched for food, eventually finding a farmer's wall adorned with luscious grapes", 'The fox leaped repeatedly, desperately trying to reach the tempting fruit, but his efforts were in vain', 'Exhausted and defeated, he abandoned his pursuit, rationalizing that the grapes were probably sour anyway', '']]
    # return temp
    story_sum = get_summary(article)
    # print(story_sum)
    sent_list = split_sentences(story_sum)

    word_string = create_word(story_sum)
    # print(word_string)
    word_list = split_words(word_string)

    return [word_list, sent_list]




# def webscraping(val):
#     querytext = val.replace(' ', '+')
#     url = "https://www.bing.com/images/search?q=" + querytext + "&qft=+filterui:license-L2_L3_L5_L6&form=IRFLTR&first=1"
#     response = requests.get(url)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')

#         img_cont_divs = soup.find_all('div', class_='img_cont hoff')

#         if img_cont_divs:

#             div = img_cont_divs[0]
#             image_tags = div.find_all('img')
#             img_tag = image_tags[0]
#             image_url = img_tag.get('src')

#             image_url = urljoin(url, image_url)

#             image_content = requests.get(image_url).content
#             image_filename = f'images/temp.png'

#             with open(image_filename, 'wb') as image_file:
#                 image_file.write(image_content)

#             resize_image()

#             file_path = '.images/temp.png'

#             if os.path.exists(file_path):
#                 os.remove(file_path)
#             else:
#                 pass
#     else:
#         print(f"Failed to retrieve the page. Status code: {response.status_code}")



def webscraping(val):
    querytext = val.replace(' ', '+')
    url = "https://www.google.com/search?q="+ querytext +"&sca_esv=5bdde8b43c3acd18&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjgl6mOzMmEAxVAt1YBHQaVCIoQ0pQJegQIAxAE&biw=1536&bih=703&dpr=1.25"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    count = 1


    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        for img in soup.find_all('img'):
            if count == 1:
                img_url = img['src']
                if img_url.startswith('/'):
                    img_url = urllib.parse.urljoin(url, img_url)
                image_filename = f'./temp.png'
                urllib.request.urlretrieve(img_url, f"images/temp.png")
                resize_image()

                file_path = '.images/temp.png'

                if os.path.exists(file_path):
                    os.remove(file_path)
                    
                print("image saved successfully")
                break
            count += 1
    else:
        print("failed to retrieve")



def resize_image(image_folder='./images',output_folder='./images2',size=(640,480)):
    img_path = os.path.join('./images','temp.png')
    img = Image.open(img_path)
    img_resized = img.resize(size)
    output_path = os.path.join(output_folder,'temp.png')
    img_resized.save(output_path)

def generate_subtitles(sentence):
    lis = []
    s = ""
    
    lines = sentence.split(',')
    
    for line in lines:
        q = line.split()
        
        if(len(q)) < 3:
            s = line
        else:
            qq = ""
            if s != "":
                qq = s + line
                s = ""
            else:
                qq = line
            qqn = qq.split()
            if len(qqn) > 8:
                s = " ".join(qqn[8:])
                qq = " ".join(qqn[:8])
            lis.append(qq)
    
    if s != '':
            lis.append(s)
    
    
    if((len(lis[-1].split())) < 3):
        # print('khj')
        lis[-2] = lis[-2]+ " "+ lis[-1]
        lis.pop(len(lis)-1)
        
    return lis



def image_to_video(duration):
    image_path = "./images2/temp.png"
    image_clip = ImageClip(image_path, duration=duration)
    black_screen = ColorClip(size=image_clip.size, color=[0, 0, 0], duration=duration)
    final_clip = CompositeVideoClip([black_screen, image_clip.set_position("center")])
    return final_clip




# def generate_video(c,a):
#     # print(c)
#     # print("\n\n")
#     # print(a)

#     all_audios = []
#     all_videos = []


#     # background_music = AudioFileClip(os.path.join(default_storage.location, "music/bg_music.mp3"))
#     # bl = []

#     # for i in range(10):
#     #     bl.append(background_music)


#     # for sentence, all_subs in b.items():
#     for index in range(len(a)):
#     # for sentence in a:
#         sentence = a[index]
#         print("*")
#         print(sentence)


#         if sentence == "":
#             continue
#         duration = 0

#         webscraping(c[index])

#         text_to_audio(sentence)
#         audio = AudioFileClip("./audio/" + text_transform(sentence) + ".mp3")

#         all_audios.append(audio)
#         duration += audio.duration

#         vid = image_to_video(audio.duration)
#         all_videos.append(vid)

#     final_audio_clip = concatenate_audioclips(all_audios)
#     # final_bg_audio_clip = concatenate_audioclips(bl)
#     increased_audio_clip = final_audio_clip.volumex(2.0)
#     # decreased_bg_audio_clip = final_bg_audio_clip.volumex(0.1)
#     # decreased_bg_audio_clip = decreased_bg_audio_clip.subclip(0, increased_audio_clip.duration)

#     final_audio_clip = CompositeAudioClip([increased_audio_clip])
#     final_video_clip = concatenate_videoclips(all_videos)
#     final_clip = final_video_clip.set_audio(final_audio_clip).set_duration(final_audio_clip.duration)
#     final_clip = final_clip.speedx(1.1)
#     return final_clip



def generate_video(c,a):
    # print(c)
    # print("\n\n")
    # print(a)

    all_audios = []
    all_videos = []


    # background_music = AudioFileClip(os.path.join(default_storage.location, "music/bg_music.mp3"))
    # bl = []

    # for i in range(10):
    #     bl.append(background_music)


    # for sentence, all_subs in b.items():
    for index in range(len(a)):
    # for sentence in a:
        sentence = a[index]
        print("*")
        print(sentence)
        if sentence == "":
            continue
        duration = 0
        if(index < len(c)):
            webscraping(c[index])
        setofsubs =generate_subtitles(sentence) 
        for sub in setofsubs:
            text_to_audio(sub)
            audio = AudioFileClip("./audio/" + text_transform(sub) + ".mp3")

            all_audios.append(audio)
            duration += audio.duration

            vid = subtitle(sub, audio.duration)
            all_videos.append(vid)

        # vid = image_to_video(audio.duration)
        # all_videos.append(vid)

    final_audio_clip = concatenate_audioclips(all_audios)
    # final_bg_audio_clip = concatenate_audioclips(bl)
    increased_audio_clip = final_audio_clip.volumex(2.0)
    # decreased_bg_audio_clip = final_bg_audio_clip.volumex(0.1)
    # decreased_bg_audio_clip = decreased_bg_audio_clip.subclip(0, increased_audio_clip.duration)

    final_audio_clip = CompositeAudioClip([increased_audio_clip])
    final_video_clip = concatenate_videoclips(all_videos)
    final_clip = final_video_clip.set_audio(final_audio_clip).set_duration(final_audio_clip.duration)
    final_clip = final_clip.speedx(1.1)
    return final_clip




def subtitle(title, duration,lang='en'):
    image_path = "./images2/temp.png"
    image_clip = ImageClip(image_path, duration=duration)
    text = title
    # text_clip = TextClip(text, fontsize=15, color='white', size=(image_clip.w, image_clip.h)).set_duration(duration)
    if lang == 'mr' or lang == 'hi':
        text_clip = TextClip(text, fontsize=15, color='white',bg_color='black',font='./MANGAL.ttf').set_duration(duration)
    elif lang in ['bn','ml','kn','te','ta','gu']:
        text_clip = TextClip(text, fontsize=15, color='white', bg_color='black', font='./Nirmala.ttf').set_duration(duration)
    elif lang == 'ur':
        text_clip = TextClip(text, fontsize=15, color='white', bg_color='black', font='./asunaskh.ttf').set_duration(duration)
    else:
        text_clip = TextClip(text, fontsize=15, color='white', bg_color='black').set_duration(duration)


    text_clip = text_clip.set_position(('center', 'bottom'))

    final_clip = CompositeVideoClip([image_clip, text_clip])
    return final_clip