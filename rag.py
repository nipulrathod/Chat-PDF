import os
import signal
import sys

import google.generativeai as genai
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')

def signal_handler(sig, frame):
    print("\nThanks for using this application.")
    sys.exit(0)
    
signal.signal(signal.SIGINT, signal_handler)

def generate_rag_prompt(query, context):
    escaped = context.replace("'","").replace('"',"").replace("\n"," ")
    prompt = ("""
              You are helpful and informative bot that answers questions using text from the reference context included below. \
                Be sure to respond in a complete sentence, being comprehensive, including all relevent background information. \
                However, You are talking to a non-technical audience, so be sure to break down complicated conceots and \
                strike a friendly and conversional tone, \
                If the context is irrelevant to the answer, you may ignore it.
                    QUESTION: '{query}'
                    CONTEXT: '{context}'
                    
                    ANSWER:
              """).format(query=query, context=context)
    return prompt

def get_relevant_context_from_db(query):
    context = ""
    embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = Chroma(persist_directory="./chroma_db_nccn", embedding_function=embedding_function)
    search_results = vector_db.similarity_search(query, k=6)
    for result in search_results:
        context += result.page_content + "\n"
    return context
    
def generate_answer(prompt):
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel(model_name='gemini-pro')
    answer = model.generate_content(prompt)
    return answer.text
    
welcome_text = generate_answer('Can you quickly introduce yourself?')
print(welcome_text)
    
while True:
    print("----------------------------------------------------------------\n")
    print("What would you like to ask?")
    query = input("Query: ")
    context = get_relevant_context_from_db(query)
    prompt = generate_rag_prompt(query=query, context=context)
    answer = generate_answer(prompt=prompt)
    print(answer)
    