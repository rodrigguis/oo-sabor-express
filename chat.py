
import sys
from langchain_core.prompts import ChatPromptTemplate 
from langchain_openai import ChatOpenAI 

model = ChatOpenAI(model="gpt-4o", temperature=0)

sent_messages =[]

print(f' Ola, eu sou o Superbot, e sou um especialista em musica Rap.')
while True:
    messages = [
        ('system', 'Ola, sou o SuperBot eu sou especialista em musica Rap.'), 
        *sent_messages,
        ('user', '{user_input}'), 
    ]

    print(messages)
    
    prompt = ChatPromptTemplate.from_messages(messages)

    chain = messages | model

    user_input = input('>')

    if user_input == 'q': 
        import sys; sys.exit(0)

    response_ai = model.invoke({'user_input' : user_input})

    sent_messages.append(('user', user_input))
    sent_messages.append(('ai', response_ai.content))

    print(response_ai.content)