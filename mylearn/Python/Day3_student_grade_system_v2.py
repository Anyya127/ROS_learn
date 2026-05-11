class Student:
    def __init__(self, name: str, student_id: str, gpa: float):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa

    def __str__(self):
        return f"姓名: {self.name} | 学号: {self.student_id} | 绩点: {self.gpa:.2f}"


class GradeSystem:
    def __init__(self):
        self._students: dict[str, Student] = {}

    def run(self):
        self._print_welcome()
        while True:
            self._print_menu()
            choice = self._read_int("请选择功能 (1-6): ", 1, 6)
            if choice is None:
                continue

            match choice:
                case 1: self._add_student()
                case 2: self._delete_student()
                case 3: self._modify_gpa()
                case 4: self._list_all()
                case 5: self._view_student()
                case 6:
                    print("已退出系统。")
                    break

    # ---- menu display ----

    @staticmethod
    def _print_welcome():
        print("\n欢迎来到学生成绩管理系统！")

    @staticmethod
    def _print_menu():
        print("\n" + "-" * 30)
        items = ["添加学生", "删除学生", "修改绩点", "查看全部学生", "查看单个学生", "退出系统"]
        for i, item in enumerate(items, 1):
            print(f"  {i}. {item}")
        print("-" * 30)

    # ---- input helpers ----

    @staticmethod
    def _read_int(prompt: str, lo: int, hi: int) -> int | None:#prompt: str, lo: int, hi: int规定参数类型    -> int | None:规定返回值类型
        try:
            val = int(input(prompt))
            if lo <= val <= hi:
                return val
            print(f"请输入 {lo}-{hi} 之间的数字。")
        except ValueError:
            print("输入无效，请输入数字。")
        return None

    @staticmethod
    def _read_float(prompt: str, lo: float = 0.0, hi: float = 4.0) -> float | None:
        try:
            val = float(input(prompt))
            if lo <= val <= hi:
                return val
            print(f"绩点应在 {lo}-{hi} 之间。")
        except ValueError:
            print("输入无效，请输入数字。")
        return None

    @staticmethod
    def _confirm(prompt: str) -> bool:
        """返回 True 表示用户确认"""
        ans = input(prompt + " (y/n): ").strip().lower()
        return ans == "y"

    # ---- business logic ----

    def _add_student(self):
        print("\n--- 添加学生 ---")
        name = input("姓名: ").strip()
        if not name:
            print("姓名不能为空，已取消。")
            return

        sid = input("学号: ").strip()
        if not sid:
            print("学号不能为空，已取消。")
            return
        if sid in self._students:
            print(f"学号 {sid} 已存在，无法重复添加。")
            return

        gpa = self._read_float("绩点 (0.0-4.0): ")
        if gpa is None:
            print("绩点无效，已取消。")
            return

        student = Student(name, sid, gpa)
        print(f"\n请确认以下信息:\n  {student}")
        if self._confirm("确认添加？"):
            self._students[sid] = student
            print("✓ 学生已添加。")
        else:
            print("已取消添加。")

    def _delete_student(self):
        print("\n--- 删除学生 ---")
        sid = input("请输入要删除的学生学号: ").strip()
        if sid in self._students:
            print(f"找到: {self._students[sid]}")
            if self._confirm("确认删除？"):
                del self._students[sid]
                print("✓ 学生已删除。")
            else:
                print("已取消。")
        else:
            print(f"未找到学号为 {sid} 的学生。")

    def _modify_gpa(self):
        print("\n--- 修改绩点 ---")
        sid = input("请输入学生学号: ").strip()
        student = self._students.get(sid)
        if student is None:
            print(f"未找到学号为 {sid} 的学生。")
            return

        print(f"当前: {student}")
        new_gpa = self._read_float("新绩点 (0.0-4.0): ")
        if new_gpa is None:
            print("已取消。")
            return

        if self._confirm(f"确认将绩点从 {student.gpa:.2f} 修改为 {new_gpa:.2f}？"):
            student.gpa = new_gpa
            print("✓ 绩点已更新。")
        else:
            print("已取消。")

    def _list_all(self):
        print("\n--- 全部学生 ---")
        if not self._students:
            print("(暂无学生记录)")
            return
        for i, s in enumerate(self._students.values(), 1):
            print(f"  [{i}] {s}")

    def _view_student(self):
        print("\n--- 查看学生 ---")
        sid = input("请输入学号: ").strip()
        student = self._students.get(sid)
        if student:
            print(f"  {student}")
        else:
            print(f"未找到学号为 {sid} 的学生。")


if __name__ == "__main__":
    GradeSystem().run()