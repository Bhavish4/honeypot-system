from predict_attack import predict_attack

tests = [
    "' OR 1=1 --",
    "<script>alert(1)</script>",
    "wget malware.sh",
    "admin 123456",
    "random normal text"
]

for t in tests:
    attack, confidence = predict_attack(t)
    print(f"Payload: {t}")
    print(f"Attack Type: {attack} | Confidence: {confidence}\n")
