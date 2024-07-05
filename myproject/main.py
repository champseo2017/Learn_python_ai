import torch
import torch.nn.functional as F

"""
การสร้าง one-hot encoding ใน PyTorch

"""
# ข้อความตัวอย่างและ token ที่สอดคล้อง
text = "Tokenizing text is a core task of NLP."
tokenized_text = list(text)
print("Tokenized text:", tokenized_text)

# สร้าง dictionary ที่แมป token ไปเป็น index (ID)
token2idx = {tk: idx for idx, tk in enumerate(sorted(set(tokenized_text)))}
print("Token-to-index mapping:", token2idx)

# แปลง tokenized text เป็น IDs
input_ids = [token2idx[tk] for tk in tokenized_text]
print("Input IDs:", input_ids)

# แปลง input_ids เป็น tensor ด้วย torch.tensor()
input_ids_tensor = torch.tensor(input_ids)

# สร้าง one-hot encodings ด้วย F.one_hot()
vocab_size = len(token2idx)  # จำนวนมิติ = ขนาดของ vocabulary 
one_hot_encodings = F.one_hot(input_ids_tensor, num_classes=vocab_size)

print("One-hot encodings shape:", one_hot_encodings.shape)
print("One-hot encodings:")
print(one_hot_encodings)