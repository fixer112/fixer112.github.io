import json
from pathlib import Path

# Load updated profile data
with open("assets/profile.json", "r", encoding="utf-8") as f:
    profile = json.load(f)


def social_link(icon, url):
    if url:
        return f'<a href="{url}" class="text-white me-3" target="_blank"><i class="{icon} fa-lg"></i></a>'
    return ''


def render_skills(skills):
    return ''.join(f'<li class="list-inline-item mb-2"><i class="fas fa-check"></i> {skill}</li>' for skill in skills)


def render_projects(projects):
    html = ''
    for project in projects:
        link_html = f'<a href="{project["link"]}" class="btn btn-primary btn-sm mt-2" target="_blank"><i class="fas fa-external-link-alt"></i> View Project</a>' if project.get(
            "link") else ''
        html += f'''
        <div class="col-md-6 col-lg-4">
          <div class="card project-card h-100">
            <div class="card-body">
              <h5 class="card-title">{project["name"]}</h5>
              <p class="card-text">{project["description"]}</p>
              <p class="card-text"><small>{project["impact"]}</small></p>
              {link_html}
            </div>
          </div>
        </div>
        '''
    return html


def render_experience(experiences):
    html = ''
    for exp in experiences:
        html += f'''
        <div class="mb-4">
          <h5>{exp["title"]} @ {exp["company"]}</h5>
          <p><em>{exp["duration"]}</em></p>
          <ul>
            {''.join(f"<li>{resp}</li>" for resp in exp["responsibilities"])}
          </ul>
        </div>
        '''
    return html


def render_notable_work(works):
    html = ''
    for work in works:
        html += f'''
        <div class="mb-4">
          <h5>{work["name"]}</h5>
          <p>{work["description"]}</p>
        </div>
        '''
    return html


# Flatten all projects
project_list = [proj for org in profile.get(
    "key_projects", []) for proj in org.get("projects", [])]

# Combine all relevant skills
all_skills = (
    profile["technical_skills"].get("languages_frameworks", []) +
    profile["technical_skills"].get("backend_technologies", []) +
    profile["technical_skills"].get("project_management", []) +
    profile["technical_skills"].get("monitoring_debugging", []) +
    profile["technical_skills"].get("databases", [])
)

# HTML template
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{profile["name"]} - Portfolio</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" rel="stylesheet">
  <style>
    body {{ font-family: 'Roboto', sans-serif; background: #f8f9fa; }}
    header {{ background: #343a40; color: #fff; padding: 60px 0 40px; text-align: center; }}
    header img {{ width: 120px; height: 120px; object-fit: cover; border-radius: 50%; border: 4px solid #fff; margin-bottom: 20px; }}
    section {{ padding: 60px 0; }}
    .skills-list i {{ margin-right: 8px; color: #0d6efd; }}
    .project-card:hover {{ box-shadow: 0 4px 24px rgba(0,0,0,0.08); }}
    footer {{ background: #343a40; color: #fff; text-align: center; padding: 30px 0; }}
  </style>
</head>
<body>
  <header>
    <img src="assets/images/profile.jpg" alt="Profile Picture">
    <h1>{profile["name"]}</h1>
    <p class="lead">Senior Backend Developer</p>
    <div>
      {social_link("fab fa-github", profile.get("github", ""))}
      {social_link("fab fa-linkedin", profile.get("linkedin", ""))}
    </div>
  </header>

  <section id="about">
    <div class="container">
      <h2 class="mb-4"><i class="fas fa-user"></i> About Me</h2>
      <p>{profile["professional_summary"]}</p>
    </div>
  </section>

  <section id="skills" class="bg-light">
    <div class="container">
      <h2 class="mb-4"><i class="fas fa-tools"></i> Skills</h2>
      <ul class="list-inline skills-list">
        {render_skills(all_skills)}
      </ul>
    </div>
  </section>

  <section id="experience">
    <div class="container">
      <h2 class="mb-4"><i class="fas fa-briefcase"></i> Experience</h2>
      {render_experience(profile.get("professional_experience", []))}
    </div>
  </section>

  <section id="projects" class="bg-light">
    <div class="container">
      <h2 class="mb-4"><i class="fas fa-folder-open"></i> Key Projects</h2>
      <div class="row g-4">
        {render_projects(project_list)}
      </div>
    </div>
  </section>

  <section id="other-work">
    <div class="container">
      <h2 class="mb-4"><i class="fas fa-lightbulb"></i> Other Notable Work</h2>
      {render_notable_work(profile.get("other_notable_work", []))}
    </div>
  </section>

  <section id="contact" class="bg-light">
    <div class="container">
      <h2 class="mb-4"><i class="fas fa-envelope"></i> Contact</h2>
      <ul class="list-unstyled">
        <li><i class="fas fa-envelope me-2"></i>{profile["email"]}</li>
        <li><i class="fas fa-phone me-2"></i>{profile["phone"]}</li>
        <li><i class="fas fa-map-marker-alt me-2"></i>{profile.get("location", "")}</li>
        <li><i class="fas fa-globe me-2"></i><a href="{profile.get("url", "#")}" target="_blank">{profile.get("url", "#")}</a></li>
      </ul>
    </div>
  </section>

  <footer>
    <div>© 2025 {profile["name"]}</div>
  </footer>
</body>
</html>
"""

# Write to file
output_file = "index.html"
Path(output_file).write_text(html_template, encoding="utf-8")
output_file
