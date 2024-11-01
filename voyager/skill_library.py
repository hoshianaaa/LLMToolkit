class SkillLibrary:
    def __init__(self):
        # スキルライブラリはスキル名と実行する関数のペアで構成される辞書で管理します
        self.skills = {}

    def add_skill(self, name, function):
        """スキルをライブラリに追加"""
        self.skills[name] = function
        print(f"Skill '{name}' added to library.")

    def execute_skill(self, name, *args, **kwargs):
        """スキルを実行"""
        if name in self.skills:
            print(f"Executing skill '{name}'...")
            return self.skills[name](*args, **kwargs)
        else:
            print(f"Skill '{name}' not found in library.")
            return None

# サンプルスキル関数を定義します
def gather_resources():
    print("Gathering resources...")

def build_structure(structure_type):
    print(f"Building {structure_type} structure...")

# スキルライブラリのインスタンスを作成します
skill_library = SkillLibrary()

# スキルをライブラリに追加します
skill_library.add_skill("gather_resources", gather_resources)
skill_library.add_skill("build_structure", build_structure)

# スキルを実行します
skill_library.execute_skill("gather_resources")
skill_library.execute_skill("build_structure", "wooden house")

