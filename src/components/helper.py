# Imports various Python libraries and modules
import pandas as pd
import numpy as np
# import langchain
import nltk
import transformers, torch
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
import openai
import tempfile


# use 'api_key' 
openai.api_key = 'your api key'



def analyze_file(file_path, labels):
    try:
        # Loads data using the SimpleDirectoryReader
        documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

        # Check if a storage context can be loaded from the directory
        # If not, create a new index, and persist it to the directory
        try:
            storage_context = StorageContext.from_default(persist_dir="./storage")
            index = load_index_from_storage(storage_context)
        except:
            index = GPTVectorStoreIndex.from_documents(documents)

        index.storage_context.persist()

        # Executes a query using the query engine
        query_engine = index.as_query_engine()
        response = query_engine.query("Classify every Sentence As Either " + labels + ", Please provide the sentences itself beside the labels.")
        return response
    except Exception as e:
        return str(e)


def analyze_text(text, labels):
    # Create a temporary file and write the text to it
    with tempfile.NamedTemporaryFile(delete=False, mode="w") as temp_file:
        temp_file.write(text)

    return (analyze_file(temp_file.name, labels))
    


# Example usage
#print(analyze_file("data/reviews.txt", "Positive and negative"))