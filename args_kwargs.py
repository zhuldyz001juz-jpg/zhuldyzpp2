def show_items(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


show_items(
    "Python",
    "OOP",
    level="beginner",
    course="KBTU"
)