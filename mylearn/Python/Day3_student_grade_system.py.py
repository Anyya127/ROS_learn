student_list=[]

choice=0
confirm="m"
  
class Student:
    def __init__(self, name, num, performance):
        self.name = name
        self.num = num
        self.performance = performance

def main():
    global choice
    global confirm
    
    menu1=[{"功能":"添加学生","编号":1},
           {"功能":"删除学生","编号":2},
           {"功能":"修改学生成绩","编号":3},
           {"功能":"查看学生列表","编号":4},
           {"功能":"查看学生","编号":5},
           {"功能":"退出系统","编号":6}]
    print("欢迎来到学生成绩管理系统！")
    print("请选择功能：")
      
    while True:
        confirm = "m"
        if choice == 0:
            for item in menu1:
                print(f"{item['编号']}: {item['功能']}")
            while True:
                try:
                    choice = int(input(f"请输入功能编号（1-{len(menu1)}）："))
                except ValueError:
                    print("输入无效，请输入1-{len(menu1)}之间的数字。")
                    continue
                if choice in [item['编号'] for item in menu1]:
                    print(f"你选择了：{menu1[choice-1]['功能']}")
                    break
                else:        
                    print("输入无效，请输入1-{len(menu1)}之间的数字。")
        elif choice == 1:
            add_student()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            print("退出系统。")
            choice = 0
            break
    

          
def add_student():
    global confirm
    global choice
    
    while  True:
        if confirm == "q":
            break
        name = input(f"请输入学生姓名：")
        num = input(f"请输入学生学号：")
        performance = float(input(f"请输入学生绩点："))
        student = Student(name, num, performance)
        print(f"请确认\n{student.name}\n{student.num}\n{student.performance}\n是否添加该学生？（y/n）")
        confirm = input().lower()
        if confirm == 'y':
            student_list.append(student)
            print("学生已添加。")
            break
        elif confirm == 'n':
            confirm = input(f"是否重新输入？（y/n）").lower()
            if confirm == 'y':
                continue
            elif confirm == 'n':
                print("操作已取消,返回主菜单。")
                confirm = "q"
                break
            elif confirm == 'q':
                break
        elif confirm == 'q':
            break
    choice = 0
    return choice
            

# def delete_student():
    
    
# def modify_student_grade():
    
    
# def view_student_list():
    
    
# def view_student():
    
    
            
# while True:
if __name__ == "__main__":
    main()       

        
