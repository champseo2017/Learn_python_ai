from transformers import AutoTokenizer, AutoModel

# โหลดโมเดล BERT ที่ถูก train ด้วย bert-base-uncased tokenizer
model = AutoModel.from_pretrained('bert-base-uncased', from_tf=True)

text = "Hello, how are you today?"

# Case 1: ใช้ tokenizer ที่ถูกต้อง
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
# โมเดลจะทำงานได้ถูกต้อง เพราะใช้ tokenizer ที่สอดคล้องกัน

print(f'Encoded input: {encoded_input}')
print(f'Output type: {type(output)}')
print(f'Output keys: {output.keys()}')
print(f'Last hidden state shape: {output.last_hidden_state.size()}')
print(f'Last hidden state values:')
print(output.last_hidden_state)