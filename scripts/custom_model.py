
from interpreter import interpreter

# 启用 OS 模式
interpreter.os = True

# 设置语言模型参数
interpreter.llm.model = "deepseek-coder"
interpreter.llm.api_base = "https://api.chatmao.org"
interpreter.llm.api_key = "sk-yuPiMTMqxgFhwtvv9223847647Ca48Ad8fC26a46E1C495Ff"

# 启用语言模型的其他特性
interpreter.llm.supports_functions = True
interpreter.llm.context_window = 110000
interpreter.llm.max_tokens = 4096

# 启用视觉支持
interpreter.llm.supports_vision = True

# 启用自动运行和循环模式
interpreter.auto_run = True
interpreter.loop = True
