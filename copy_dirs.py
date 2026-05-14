import shutil

try:
    shutil.copytree("ref_repo/app-base-fullstack-main/backend", "backend")
    shutil.copytree("ref_repo/app-base-fullstack-main/fontend", "frontend")
    print("Copied successfully.")
except Exception as e:
    print(f"Error: {e}")
