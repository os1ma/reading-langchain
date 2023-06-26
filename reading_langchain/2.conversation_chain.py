import openai
from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage

load_dotenv()

openai.log = "debug"

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("hi!")
memory.chat_memory.add_ai_message("whats up?")

# Memory のチュートリアルの通り以下のように ConversationChain を使うと、
# role: user に全ての履歴が含まれてしまい、Chat Completions API の使い方として適切ではなくなる
conversation = ConversationChain(llm=chat, memory=memory)
conversation_result = conversation.predict(input="Hi there!")
print(conversation_result)

# 自前で履歴を与えると、role: assistant を活用した、Chat Completions API として適切なプロンプトになる
messages = memory.chat_memory.messages
messages.append(HumanMessage(content="Hi there!"))
raw_chat_result = chat(messages)
print(raw_chat_result.content)
