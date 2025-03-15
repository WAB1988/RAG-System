from flask import Flask, render_template, request, jsonify
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
import os

app = Flask(__name__)

# Settings control global defaults
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Groq(model="llama3-70b-8192", api_key="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")

# Initialize the RAG system
def initialize_rag():
    if not os.path.exists('data'):
        os.makedirs('data')
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    return index.as_query_engine()

# Create query engine
query_engine = initialize_rag()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def process_query():
    data = request.json
    user_query = data.get('query', '')
    
    try:
        response = query_engine.query(user_query)
        return jsonify({'response': str(response)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 