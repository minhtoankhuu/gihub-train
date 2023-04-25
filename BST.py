class Student:
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.id}, {self.name}, {self.grade}"


class Node:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add_student(self, student):
        self.root = self.add_node(self.root, student)

    def add_node(self, node, student):
        if node is None:
            return Node(student)
        elif student.id < node.student.id:
            node.left = self.add_node(node.left, student)
        elif student.id> node.student.id:
            node.right = self.add_node(node.right, student)
        else:
            # Tên học sinh đã tồn tại
            pass
        return node

    def remove_student(self, id):
        self.root = self.remove_node(self.root, id)

    def remove_node(self, node, id):
        if node is None:
            return None
        elif id < node.student.id:
            node.left = self.remove_node(node.left, id)
            return node
        elif id > node.student.id:
            node.right = self.remove_node(node.right, id)
            return node
        else:
            # Tìm thấy nút chứa thông tin học sinh cần xóa
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Tìm kiếm nút lớn nhất bên trái của nút cần xóa
                max_left = node.left
                while max_left.right is not None:
                    max_left = max_left.right
                # Thay thế thông tin của nút cần xóa bằng thông tin của nút lớn nhất bên trái
                node.student = max_left.student
                # Xóa nút lớn nhất bên trái
                node.left = self.remove_node(node.left, max_left.student.id)
            return node

    def find_student(self, id):
        node = self.root
        while node is not None:
            if node.student.id == id:
                return node.student
            elif id < node.student.id:
                node = node.left
            else:
                node = node.right
        return None

    def __str__(self):
        return self.print_tree(self.root)

    def print_tree(self, node):
        if node is None:
            return ""
        else:
            return self.print_tree(node.left) + str(node.student) + "\n" + self.print_tree(node.right)



bst = BST()
while True:
    print("\n=== Quản lý học sinh ===")
    print("1. Thêm học sinh")
    print("2. Xóa học sinh")
    print("3. Tìm kiếm học sinh")
    print("4. Hiển thị danh sách học sinh")
    print("0. Thoát chương trình")
    choice = input("Lựa chọn của bạn: ")
    if choice == "1":
        id = input("Nhập ID học sinh: ")
        name = input("Nhập tên của học sinh: ")
        grade = input("Nhập điểm số của học sinh: ")
        if   not grade.isdigit():
            print("Điểm số phải là số nguyên dương.")
        elif bst.find_student(id) is not None:
            print("ID học sinh đã tồn tại.")
        else:
            bst.add_student(Student(id, name, int(grade)))
            print(f"Đã thêm học sinh {id} vào danh sách.")
    elif choice == "2":
        # Xóa học sinh
        id = input("Nhập tên học sinh cần xóa: ")
        if bst.find_student(id) is None:
            print("Không tìm thấy học sinh có ID là", id)
        else:
            bst.remove_student(id)
            print(f"Đã xóa học sinh có {id} khỏi danh sách.")
    elif choice == "3":
        # Tìm kiếm học sinh
        id = input("Nhập ID học sinh cần tìm kiếm: ")
        student = bst.find_student(id)
        if student is None:
            print("Không tìm thấy học sinh có ID là", id)
        else:
            print("Thông tin học sinh:")
            print(student)
    elif choice == "4":
        # Hiển thị danh sách học sinh
        print("Danh sách học sinh:")
        print(bst)
    elif choice == "0":
        # Thoát chương trình
        break
    else:
        print("Lựa chọn không hợp lệ.")