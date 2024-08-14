from transformers import AutoTokenizer, AutoModel

# โหลดโมเดล BERT ที่ถูก train ด้วย bert-base-uncased tokenizer
model = AutoModel.from_pretrained('bert-base-uncased', from_tf=True, ignore_mismatched_sizes=True)

text = "Hello, how are you today?"

# Case 1: ใช้ tokenizer ที่ถูกต้อง
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
# โมเดลจะทำงานได้ถูกต้อง เพราะใช้ tokenizer ที่สอดคล้องกัน


# Case 2: ใช้ tokenizer ผิด 
wrong_tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')
encoded_input = wrong_tokenizer(text, return_tensors='pt')  
output = model(**encoded_input)