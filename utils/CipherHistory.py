from dataclasses import dataclass
from datetime import datetime

@dataclass
class CipherHistory:
    originText: str
    keyA: int = None
    keyB: int = None
    resultText: str = ""
    cipherType: str = ""
    actionType: str = ""
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")