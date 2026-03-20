# Contributing to Awesome Robot Vision

Thank you for your interest in contributing! This list aims to be the most comprehensive and up-to-date collection of resources for **robot vision** research.

## Table of Contents

- [What to Contribute](#what-to-contribute)
- [How to Contribute](#how-to-contribute)
- [Entry Format](#entry-format)
- [Quality Guidelines](#quality-guidelines)
- [Pull Request Checklist](#pull-request-checklist)
- [Code of Conduct](#code-of-conduct)

---

## What to Contribute

We welcome additions of:

- **Methods and frameworks** for robot vision tasks (pose estimation, grasping, depth estimation, SLAM, etc.)
- **Datasets** used for training or evaluating robot vision systems
- **Toolkits and libraries** that support robot vision development
- **Benchmarks and simulation environments** for evaluation
- **Survey papers** providing a structured overview of a sub-field

We are **not** looking for:

- General computer vision work with no clear robotics application
- Duplicates of existing entries
- Projects that are not publicly accessible or described in a paper/report

---

## How to Contribute

1. **Fork** this repository.
2. **Create a branch** from `main` with a descriptive name, e.g. `add-<project-name>`.
3. **Edit `README.md`** to add your entry in the appropriate section table, following the [Entry Format](#entry-format) below.
4. **Submit a pull request** against the `main` branch.

A GitHub Actions workflow will automatically check your PR for formatting issues. Please address any failures before requesting a review.

---

## Entry Format

Each entry must be a row in the relevant Markdown table. The table has three columns:

```markdown
| Name | Highlights | References |
|------|-----------|------------|
| [Project Name](https://official-website.com/) | [Venue Year] One-sentence description of what makes this project notable | [arXiv](https://arxiv.org/abs/XXXX.XXXXX) · [GitHub](https://github.com/org/repo) · [Website](https://official-website.com/) |
```

### Column rules

| Column | Required | Description |
|--------|----------|-------------|
| **Name** | ✅ | A Markdown link `[Name](URL)` pointing to the project's official website or primary resource |
| **Highlights** | ✅ | `[Venue Year]` tag (if published) followed by a single concise sentence describing what distinguishes this project |
| **References** | ✅ | At least one reference link (arXiv, GitHub, or Website). Multiple links separated by ` · ` |

### Reference link labels

Use these standard labels for consistency:

- `[arXiv](...)` — preprint or paper
- `[GitHub](...)` — source code / dataset repository
- `[Website](...)` — official project page
- `[HF](...)` — HuggingFace model/dataset card
- `[PDF](...)` — direct PDF link when no arXiv page exists

---

## Quality Guidelines

- **Relevance**: The project must be directly applicable to robot vision or a closely related sub-field.
- **Accessibility**: The project (or at minimum its paper/description) must be publicly available.
- **Conciseness**: The Highlights column should be one sentence. Avoid marketing language.
- **Accuracy**: Double-check all links before submitting. Broken links will cause the automated check to fail.
- **Placement**: Add the entry to the most appropriate existing section. If no section fits, propose a new one in your PR description and we will discuss it.

---

## Pull Request Checklist

Before submitting your PR, confirm the following:

- [ ] The project is relevant to robot vision
- [ ] The entry follows the three-column table format exactly
- [ ] The **Name** column contains a valid Markdown link
- [ ] The **References** column contains at least one working link
- [ ] The **Highlights** description is one sentence and starts with a `[Venue Year]` tag (if applicable)
- [ ] No existing entry for this project is present in the list
- [ ] All links in your addition are reachable (not 404)
- [ ] The PR title clearly describes what is being added, e.g. `Add FooNet to 6D Object Pose Estimation`

---

## Code of Conduct

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/) Code of Conduct. By participating, you agree to uphold a welcoming and respectful environment for everyone.

If you have questions or suggestions that are not suitable for a pull request, feel free to open an [issue](https://github.com/han-xudong/awesome-robot-vision/issues).
