from Student import *


class managerSystem(object):
    def __init__(self):
        self.student_list = []

    def run(self):
        self.load_student()

        while True:
            self.show_menu()

            menu_num = int(input("输入序号"))

            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.delete_student()
            elif menu_num == 3:
                self.modify_student()
            elif menu_num == 4:
                self.search_student()
            elif menu_num == 5:
                self.show_student()
            elif menu_num == 6:
                self.save_student()
            elif menu_num == 7:
                break

        # * 1显示菜单

    def show_menu(self):
        print(" ")
        # * 2添加

    def add_student(self):
        print("请添加学生")
        # *1输入
        name = input("请输入姓名")
        id = int(input("请输入id"))
        tel = input("请输入tel")
        # * 2创建对象
        student = Student(name, id, tel)
        # *3添加至列表
        self.student_list.append(student)
        # * 3删除

    def delete_student(self):
        del_name = input("请输入删除学生的姓名")
        for i in self.student_list:
            if i.name == del_name:
                print("已删除:"+i.name)
                self.student_list.remove(i)
                break
        else:
            print("没有这个学生")
        # * 4修改

    def modify_student(self):
        mod_name = input("请输入学生姓名")
        for i in self.student_list:
            if i.name == mod_name:
                mod = int(input("请选择修改项\n1姓名\n2id\n3tel\n"))
                if mod == 1:
                    name = input("请输入名字")
                    i.name = name
                elif mod == 2:
                    id = int(input("请输入id"))
                    i.id = id
                elif mod == 3:
                    tel = input("请输入tel")
                    i.tel = tel
                k = Student(i.name, i.id, i.tel)
                self.student_list.remove(i)
                self.student_list.append(k)
                break
        else:
            print("没有这个学生")
        # * 5查询

    def search_student(self):
        index_name = input("请输入学生的姓名")
        for i in self.student_list:
            if i.name == index_name:
                print("姓名:"+i.name)
                print("id:"+str(i.id))
                print("tel:"+i.tel)
                break
        else:
            print("没有这个学生")
        # * 6显示全部

    def show_student(self):
        for i in self.student_list:
            print(i.name)
            print(i.id)
            print(i.tel)

        # * 7保存

    def save_student(self):
        with open('student.data', 'w') as f:
            new_list = [i.__dict__ for i in self.student_list]
            f.write(str(new_list))
        # *8 加载

    def load_student(self):
        try:
            with open('student.data', 'r', encoding="utf-8") as f:
                data = f.read()
        except:
            with open('student.data', 'w', encoding="utf-8") as f:
                data = f.read()
        # with open('student.data', 'a+') as f:
        #     data = f.read()
        try:
            new_list = eval(data)
        except:
            data_list = [{'name': 'koishi', 'id': 1, 'tel': '20'}]
            with open('student.data', 'w', encoding="utf-8") as f:
                f.write(str(data_list))
            with open('student.data', 'r', encoding="utf-8") as f:
                data = f.read()
            new_list = eval(data)
        self.student_list = [
            Student(i["name"], i["id"], i["tel"]) for i in new_list]
