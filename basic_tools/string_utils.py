import re
def extract_phone_email(text: str) -> dict:
    if not isinstance(text, str): raise TypeError("输入必须为字符串")
    phone_pattern = r"1[3-9]\d{9}"
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return {"phones": list(set(re.findall(phone_pattern, text))), 
            "emails": list(set(re.findall(email_pattern, text)))}

def clean_text(text: str) -> str:
    if not isinstance(text, str): raise TypeError("输入必须为字符串")
    return re.sub(r"\s+", " ", text).strip()