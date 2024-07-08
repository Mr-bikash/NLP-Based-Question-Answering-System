# chunk_and_store.py
from sentence_transformers import SentenceTransformer
import json
import milvus
from milvus import Milvus, IndexType, MetricType

def chunk_data(data):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    chunks = {}
    for url, text in data.items():
        sentences = text.split('.')
        embeddings = model.encode(sentences, convert_to_tensor=True)
        chunks[url] = list(zip(sentences, embeddings))
    return chunks

def store_in_milvus(chunks):
    client = Milvus()
    client.create_collection({
        "collection_name": "cuda_docs",
        "fields": [
            {"name": "sentence", "type": milvus.DataType.VARCHAR, "params": {"max_length": 512}},
            {"name": "embedding", "type": milvus.DataType.FLOAT_VECTOR, "params": {"dim": 384}}
        ]
    })
    for url, chunk_list in chunks.items():
        sentences, embeddings = zip(*chunk_list)
        client.insert("cuda_docs", [{"name": "sentence", "values": sentences}, {"name": "embedding", "values": embeddings}])
        client.create_index("cuda_docs", {"field_name": "embedding", "index_type": IndexType.HNSW, "metric_type": MetricType.L2})

if __name__ == "__main__":
    with open('crawled_data.json', 'r') as f:
        crawled_data = json.load(f)
    
    chunks = chunk_data(crawled_data)
    store_in_milvus(chunks)
