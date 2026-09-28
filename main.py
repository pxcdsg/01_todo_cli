import json
from pathlib import Path


DATA_FILE = Path(__file__).parent / "tasks.json"


def load_tasks():
    """从 tasks.json 读取任务；文件不存在时返回空列表。"""
    if not DATA_FILE.exists():
        return []

    try:
        text = DATA_FILE.read_text(encoding="utf-8")
        return json.loads(text)
    except json.JSONDecodeError:
        print("tasks.json 格式有问题，先当作空列表处理。")
        return []


def save_tasks(tasks):
    """把任务列表写入 tasks.json。"""
    text = json.dumps(tasks, ensure_ascii=False, indent=2)
    DATA_FILE.write_text(text, encoding="utf-8")


def add_task(tasks):
    """添加一条任务。"""
    title = input("请输入任务内容：").strip()
    if not title:
        print("任务内容不能为空。")
        return

    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"已添加：{title}")


def list_tasks(tasks):
    """显示全部任务。"""
    if not tasks:
        print("当前没有任务。")
        return

    for index, task in enumerate(tasks, start=1):
        status = "x" if task["done"] else " "
        print(f"{index}. [{status}] {task['title']}")


def delete_task(tasks):
    """按编号删除一条任务。"""
    if not tasks:
        print("当前没有任务可以删除。")
        return

    list_tasks(tasks)
    text = input("请输入要删除的编号：").strip()

    if not text.isdigit():
        print("请输入数字编号。")
        return

    index = int(text) - 1
    if index < 0 or index >= len(tasks):
        print("编号不存在。")
        return

    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"已删除：{removed['title']}")


def main():
    tasks = load_tasks()

    while True:
        print("\n1. 添加任务")
        print("2. 查看任务")
        print("3. 删除任务")
        print("4. 退出")
        choice = input("请选择：").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("再见。")
            break
        else:
            print("请输入 1 到 4 之间的数字。")


if __name__ == "__main__":
    main()
