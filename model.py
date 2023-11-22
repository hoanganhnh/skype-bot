import os
import sys

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.vectorstores import Chroma


os.environ["OPENAI_API_KEY"] = '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'

class ModelGPT:
  # Enable to save to disk & reuse the model (for repeated queries on the same data)
  def construct_index(self,PERSIST = True):
    if PERSIST and os.path.exists("./persist"):
      print("Reusing index...\n")
      vectorstore = Chroma(persist_directory="./persist", embedding_function=OpenAIEmbeddings())
      index = VectorStoreIndexWrapper(vectorstore=vectorstore)
    else:
      loader = DirectoryLoader("data/")
      if PERSIST:
        index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"./persist"}).from_loaders([loader])
      else:
        index = VectorstoreIndexCreator().from_loaders([loader])
      
    return index    
    
  def create_chain(self):
    index = self.construct_index()
    chain = ConversationalRetrievalChain.from_llm(
      llm=ChatOpenAI(model="gpt-3.5-turbo"),
      retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )
    return chain

model = ModelGPT()
chain = model.create_chain()
chat_history = []
def get_request(query):
  result = chain({"question": query, "chat_history": chat_history})
  print(result['answer'])

  chat_history.append((query, result['answer']))
  return result['answer']
  
# print(get_request("What is BSS ?"))