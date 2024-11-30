# 创建一个函数来演示所有字典操作
def demonstrate_dictionary_operations():
    print("\n1. 创建字典")
    # 创建一个字典
    person = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    print(f"初始字典: {person}")

    print("\n2. 访问值")
    name = person["name"]
    age = person["age"]
    print(f"获取name的值: {name}")
    print(f"获取age的值: {age}")

    print("\n3. 添加和修改值")
    # 添加新键值对
    person["country"] = "USA"
    print(f"添加country后: {person}")
    # 修改现有值
    person["city"] = "Chicago"
    print(f"修改city后: {person}")

    print("\n4. 复制字典")
    # 使用copy()方法
    new_person = person.copy()
    print(f"使用copy()方法复制的新字典: {new_person}")
    # 使用dict()函数
    another_person = dict(person)
    print(f"使用dict()函数复制的新字典: {another_person}")

    print("\n5. 获取items()")
    items_list = list(person.items())
    print(f"字典的items列表: {items_list}")

    print("\n6. 检查键是否存在")
    if "name" in person:
        print("'name'存在于字典中")
    if "email" not in person:
        print("'email'不存在于字典中")

    print("\n7. 获取所有键")
    keys_list = list(person.keys())
    print(f"字典的所有键: {keys_list}")

    print("\n8. 获取所有值")
    values_list = list(person.values())
    print(f"字典的所有值: {values_list}")

    print("\n9. 更新字典")
    person.update({"profession": "Doctor", "email": "john@example.com"})
    print(f"更新后的字典: {person}")

    print("\n10. 删除特定键值对")
    del person["email"]
    print(f"删除email后的字典: {person}")

    print("\n11. 清空字典")
    new_person.clear()
    print(f"清空后的new_person字典: {new_person}")

    print("\n12. 原始字典的最终状态")
    print(f"person字典: {person}")

# 执行演示
demonstrate_dictionary_operations()