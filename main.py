from templates import generate_readme

print("=== AI README Generator ===")

name = input("Enter your name: ")
bio = input("Enter your bio: ")
skills = input("Enter skills (comma separated): ")
projects = input("Enter projects (comma separated): ")
github_username = input("Enter your GitHub username: ")

readme = generate_readme(name, bio, skills, projects,github_username)

with open("GENERATED_README.md", "w", encoding="utf-8") as file:
    file.write(readme)
print("\n✅ README generated successfully!")
print("Check GENERATED_README.md")