from unsloth import FastModel
import torch

# ✅ Unsloth 모델 불러오기
model, tokenizer = FastModel.from_pretrained(
    model_name = "unsloth/Meta-Llama-3-8B-Instruct-bnb-4bit",
    max_seq_length = 2048,
    load_in_4bit = True,
)

# ✅ 한글 질문 입력
prompt = "한국의 수도는 어디인가요?"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

# ✅ 모델 추론
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=50)

# ✅ 결과 출력
print("🦥 모델 응답:")
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
