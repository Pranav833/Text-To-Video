# # Adjust imports based on actual module structure
# from langchain_community.llms import CTransformers
# from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChain
# # import torch
# # from torch import autocast
# # from diffusers import DiffusionPipeline 

# def load_llm(max_tokens, user_input):
#     llm = CTransformers(
#         # model="TheBloke/Llama-2-7B-Chat-GGML",
#         model='E:/3rd year roject/SDAM/Final/models/ggml-model-q8_0.bin',
#         model_type="llama",
#         max_new_tokens=max_tokens,
#         temperature=0.7
#     )
    

#     prompt_template = f"You are a digital marketing and SEO expert and your task is to write an article on the given topic: {user_input}. The article must be under 800 words. The article should not be too lengthy."
    
#     llm_chain = LLMChain(
#         llm=llm,
#         prompt=PromptTemplate.from_template(prompt_template)
#     )
#     return llm_chain



# '''
# pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", use_safetensors=True)
# pipeline.to("cuda")
# image = pipeline("wolf eats sheep and boy cries").images[0]
# image.save('generatedimage.png')
    
#     '''

# if __name__ == '__main__':
#     print("Hello")
#     user_input = "origami"
#     llm_call = load_llm(max_tokens=800, user_input=user_input)
    
#     # Pass input as a list
#     result = llm_call([user_input])
    
#     print(result)



from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_experimental.chat_models import Llama2Chat
from langchain_community.llms import HuggingFaceTextGenInference

llm = HuggingFaceTextGenInference(
    inference_server_url="http://127.0.0.1:8080/",
    max_new_tokens=512,
    top_k=50,
    temperature=0.1,
    repetition_penalty=1.03,
)

model = Llama2Chat(llm=llm)

from langchain_core.messages import SystemMessage
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)

template_messages = [
    SystemMessage(content="You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{text}"),
]
prompt_template = ChatPromptTemplate.from_messages(template_messages)

llm = HuggingFaceTextGenInference(
    inference_server_url="http://127.0.0.1:8080/",
    max_new_tokens=512,
    top_k=50,
    temperature=0.1,
    repetition_penalty=1.03,
)

model = Llama2Chat(llm=llm)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
chain = LLMChain(llm=model, prompt=prompt_template, memory=memory)


print(
    chain.run(
        text="What can I see in Vienna? Propose a few locations. Names only, no details."
    )
)

print(chain.run(text="Tell me more about #2."))
