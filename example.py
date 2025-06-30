# 課題１（「hello world」と出力）
print("Hello, world!")

# 課題２（greet関数を実装し、「こんにちは」と出力する）
def greet():
    print("こんにちは")
greet()

# 課題3（nameを引数に取り、「私の名前は{name}です」と出力するprint_name関数を実装）
def print_name(name):
    print("私の名前は"+name+"です")
print_name("Yohida")

# 課題４（「おはようございます」という文字列を戻り値として返すget_greet関数を実装し、戻り値をprint関数で出力）
def get_greet():
     return "おはようございます"
r = get_greet()
print(r)

# 課題5(a, bを引数に取り、その足し算の結果を戻り値として返すadd関数を実装し、関数を呼び出して結果をprint関数で出力)
def add(a,b):
    return a+b
a = add(2,4)
print(a)