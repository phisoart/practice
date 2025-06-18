text = "hello world"
color_code = "\033[33m"  # 노란색
reset_code = "\033[0m"

border = "+" + "-" * (len(text) + 2) + "+"
content = f"| {text} |"

print(color_code + border)
print(content)
print(border + reset_code)