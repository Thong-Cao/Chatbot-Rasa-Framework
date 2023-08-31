import streamlit as st
from rasa_nlu.model import Interpreter
import logging
import pprint
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter
#from rasa_nlu.evaluate import run_evaluation
import pandas as pd
# Import your chatbot engine here
# For this example, we'll just use a simple echo bot
logfile = 'nlu_model.log'
import numpy as np



logging.basicConfig(filename=logfile, level=logging.DEBUG)
nlu_model_path = r"D:\machine_learning\ml_chatbot_finance\Rasa_chatbot\model\chatbot_ver2\nlu"
excel_file = r"D:\machine_learning\ml_chatbot_finance\Rasa_chatbot\data_0505_train.xlsx"


logging.basicConfig(filename=logfile, level=logging.DEBUG)
NLU_CONF = 0.5
interpreter = Interpreter.load(nlu_model_path)
df_data = pd.read_excel(excel_file, dtype={'ID': np.float})


print("Your bot is ready to talk! Type your messages here or send 'stop'")
st.header('Chatbot tài chính - Pomodoro')
st.markdown('Link truy cập: http://surl.li/gvagn')
question = st.text_input("Enter your message here")

Button = st.button("Hỏi", type="primary")
if Button:
    question = question.lower()
    id = interpreter.parse(question)

    intent = id["intent"]["name"]
    conf = id["intent"]["confidence"]
    if intent != None and conf >= NLU_CONF:
        df_id = df_data[df_data['ID'] == float(intent[1:])]
        df_res_dropna = df_id.dropna(subset=['response'])
        df_res_dropna['link'] = df_res_dropna['link'].fillna(0)
        full_res = ''
        for res in df_res_dropna.index:
            if df_res_dropna['link'][res] != 0:
                full_res = full_res + df_res_dropna['response'][res] + '\n' + df_res_dropna['link'][res] + '\n'
            else:
                full_res = full_res + df_res_dropna['response'][res] + '\n' 
    else:
        full_res = 'tôi chưa hiểu ý của bạn, bạn có thể nói rõ hơn không?'
    st.header(full_res)





