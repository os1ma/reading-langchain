from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# __call__ を使った呼び出し方
messages = [HumanMessage(content="Hello!")]
call_result = chat(messages)
print(call_result.content)

# predict を使った呼び出し方
predict_result = chat.predict("Hello!")
print(predict_result)
