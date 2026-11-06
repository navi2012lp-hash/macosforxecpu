import os
if os.path.exists(r"D:\.git"):
    print("Git repository already exists on USB drive")
else:
    print("No .git directory found - USB drive is not yet a git repository")