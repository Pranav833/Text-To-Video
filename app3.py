from langchain_community.llms import CTransformers
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
import time


def generate_summary():
    start_time = time.time()

    story = """

    There once was a boy who grew bored while watching over the village sheep. He wanted to make things more exciting. So, he yelled out that he saw a wolf chasing the sheep. All the villagers came running to drive the wolf away. However, they saw no wolf. The boy was amused, but the villagers were not. They told him not to do it again. Shortly after, he repeated this antic. The villagers came running again, only to find that he was lying. Later that day, the boy really sees a wolf sneaking amongst the flock. He jumped up and called out for help. But no one came this time because they thought he was still joking around. At sunset, the villagers looked for the boy. He had not returned with their sheep. They found him crying. He told them that there really was a wolf, and the entire flock was gone. An old man came to comfort him and told him that nobody would believe a liar even when they are being honest.

    """
    print("8")
    llm = CTransformers(model='TheBloke/Llama-2-7B-Chat-GGML',model_type='llama',local_files_only = True)
    print("8")
    print(llm.invoke('convert the story in dialog form also add narrator where necessary and also give title and moral story: {story}'))

    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")

    print("8")
    template = """[INST] 
    <<SYS>>
    You are a creative assistant and you have to convert the story in dialog form also add narrator where necessary and also give title and moral
    <</SYS>>
    user prompt: {prompt}
    [/INST]
    """
    print("8")
    prompt = PromptTemplate.from_template(template)
    # print("8")
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    # print("8*")
    response = llm_chain.invoke(story)
    # print("8")
    print(response)
    # print("8")


    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")