def generate_readme(name, bio, skills, projects, github, theme):
    skills_list = [s.strip() for s in skills.split(",")]
    projects_list = [p.strip() for p in projects.split(",")]

    skills_md = "\n".join([f"- {s}" for s in skills_list])
    projects_md = "\n".join([f"- {p}" for p in projects_list])

    theme_color = "tokyonight" if theme == "dark" else "default"

    return f"""# 👋 Hi, I'm {name}

### 💫 About Me
{bio}

---

### 🛠️ Tech Stack
{skills_md}

---

### 🚀 Projects
{projects_md}

---

### 📊 GitHub Stats
![Stats](https://github-readme-stats.vercel.app/api?username={github}&show_icons=true&theme={theme_color})

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username={github}&layout=compact&theme={theme_color})

---

### 🌐 Connect with Me
- 💼 LinkedIn: https://linkedin.com/in/YOUR-LINK
- 📧 Email: your@email.com

---

⭐ Generated with AI README Generator
"""