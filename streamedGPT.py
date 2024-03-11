
import openai
import streamlit as st
import time

# OpenAI API key
openai.api_key = "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"

#INPUT INTERFACE & SUBMIT BUTTON
st.title('Stream ChatGPT responses')
prompt = st.text_input(label="Prompt: ")
submit_button_exist = st.button('Submit')
#CALL TO API
start_time = time.time()
max_response_length = 200
delay_time = 0.10
response = openai.ChatCompletion.create(
    # CHATPG GPT API REQQUEST
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'user', 'content': f'{prompt}'}
    ],
    max_tokens=max_response_length,
    temperature=0,
    stream=True,  # this time, we set stream=True
)
#PRINTING OUTPUT
answer=''

if submit_button_exist is True:
    c = st.empty()
    for event in response:
        c.write(answer)
        event_time = time.time() - start_time
        event_text = event['choices'][0]['delta']
        answer += event_text.get('content', '')
        time.sleep(delay_time)
else: 
  st.write("")