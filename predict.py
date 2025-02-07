import torch
import pickle
from core import to_bert_ids, use_model

#if __name__ == "__main__":    
# load and init
pkl_file = open('trained_model/data_features.pkl', 'rb')
data_features = pickle.load(pkl_file)
answer_dic = data_features['answer_dic']
    
# BERT
model_setting = {
    "model_name":"bert", 
    "config_file_path":"trained_model/config.json", 
    "model_file_path":"trained_model/pytorch_model.bin", 
    "vocab_file_path":"bert-base-chinese-vocab.txt",
    "num_labels":25  # 分幾類  23
}  

# ALBERT
# model_setting = {
#     "model_name":"albert", 
#     "config_file_path":"trained_model/config.json", 
#     "model_file_path":"trained_model/pytorch_model.bin", 
#     "vocab_file_path":"albert/albert_tiny/vocab.txt",
#     "num_labels":149 # 分幾類
# }

#
model, tokenizer = use_model(**model_setting)  #開啟需要時間
model.to(torch.device('cpu')) #放入CPU
model.eval()

#
def bert(q_inputs):
    for q_input in q_inputs:
        bert_ids = to_bert_ids(tokenizer,q_input)
        assert len(bert_ids) <= 512
        input_ids = torch.LongTensor(bert_ids).unsqueeze(0)

        # predict
        outputs = model(input_ids)
        predicts = outputs[:2]
        predicts = predicts[0]
        max_val = torch.max(predicts)
        label = (predicts == max_val).nonzero().numpy()[0][1]
        ans_label = answer_dic.to_text(label)
        
        return ans_label
        #print()
        

