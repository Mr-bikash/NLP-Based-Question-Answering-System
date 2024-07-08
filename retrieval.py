# retrieval.py
from transformers import DPRQuestionEncoder, DPRContextEncoder
import torch
import json

def retrieve_and_rerank(query, chunks):
    query_expanded = query + " " + "related terms"
    
    dpr_question_encoder = DPRQuestionEncoder.from_pretrained('facebook/dpr-question_encoder-single-nq-base')
    dpr_context_encoder = DPRContextEncoder.from_pretrained('facebook/dpr-ctx_encoder-single-nq-base')
    question_embedding = dpr_question_encoder(query_expanded)
    
    results = []
    for url, chunk_list in chunks.items():
        for sentence, embedding in chunk_list:
            similarity = torch.cosine_similarity(question_embedding, embedding, dim=-1)
            results.append((similarity, sentence, url))
    
    results.sort(key=lambda x: x[0], reverse=True)
    return results[:10]

if __name__ == "__main__":
    with open('crawled_data.json', 'r') as f:
        crawled_data = json.load(f)
    
    query = "How to optimize CUDA code?"
    top_results = retrieve_and_rerank(query, crawled_data)
    with open('top_results.json', 'w') as f:
        json.dump(top_results, f)
