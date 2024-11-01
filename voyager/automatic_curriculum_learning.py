class Curriculum:
    def __init__(self):
        self.level = 1

    def get_task(self):
        return f"Task for level {self.level}"

    def level_up(self):
        self.level += 1
        print(f"Level up! Current level: {self.level}")

# 自動カリキュラムの例
curriculum = Curriculum()
print(curriculum.get_task())
curriculum.level_up()
print(curriculum.get_task())

