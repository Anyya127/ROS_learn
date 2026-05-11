import random

def guessing_game():
    print("\n===== 猜数字游戏 =====")
    
    
    print("请选择难度")
    print("1. 简单 (1~20)")
    print("2. 中等 (1~50)")
    print("3. 困难 (1~100)")
    while True:
        try:
            difficulty = int(input("请输入难度（1/2/3）："))
        except ValueError:
            print("输入无效，请输入1、2或3。")
            continue
            
        if difficulty in [1, 2, 3]:
            break
        else:
            print("输入无效，请输入1、2或3。")
            

    max_number = {1: 20, 2: 50, 3: 100}.get(difficulty, 50)  # 默认简单难度
    secret = random.randint(1, max_number)
    history = []  # 记录每次猜的数字和结果
    
    while True:
        guss = int(input(f"请输入一个数字（1~{max_number}）："))
        if guss < secret:
            print("太小了！")
            history.append((guss, "太小了"))
        elif guss > secret:
            print("太大了！")
            history.append((guss, "太大了"))
        else:
            print("恭喜你，猜对了！")
            history.append((guss, "正确"))
            break
        
    print("\n你的猜测历史：")
    for guess, result in history[0:len(history)-1]:  # 不包括最后一次正确的猜测
        print(f"你猜了 {guess}，可惜{result}")
    print(f"正确答案是 {secret}。")
    
    
if __name__ == "__main__":
    guessing_game()