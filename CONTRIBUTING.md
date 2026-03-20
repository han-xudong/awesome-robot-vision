# Contributing to Awesome Robot Vision

Thank you for your interest in contributing! This guide explains how to add or improve entries so the list stays consistent and high-quality.

---

## Table of Contents

- [How to Contribute](#how-to-contribute)
- [Entry Requirements](#entry-requirements)
- [Table Format](#table-format)
- [Publication Venue Tags](#publication-venue-tags)
- [Pull Request Checklist](#pull-request-checklist)
- [Reporting Issues](#reporting-issues)

---

## How to Contribute

1. **Fork** this repository and create a new branch from `main`.
2. Make your changes following the guidelines below.
3. Open a **Pull Request** with a clear title and description of what you added or changed.
4. Automated checks will run on your PR. Please fix any failures before requesting review.

---

## Entry Requirements

Before adding an entry, please verify that:

- The project is **directly relevant** to robot vision (pose estimation, grasping, scene understanding, SLAM, depth estimation, robot learning with visual input, etc.).
- The project has a **public code repository** (GitHub, GitLab, etc.) or an official website.
- The project has reached a **minimum level of maturity** — it should have a paper, be actively maintained, or be a widely adopted library/dataset.
- There is **no duplicate** of the entry already in the list.

---

## Table Format

All entries **must** follow the three-column table format used throughout the README:

```markdown
| Name | Highlights | References |
|---|---|---|
| **[Project Name](https://github.com/owner/repo)** | One-sentence description of what it does. **[VENUE YEAR]** | [GitHub](https://github.com/owner/repo) · [arXiv](https://arxiv.org/abs/XXXX.XXXXX) · [Website](https://example.com) |
```

### Column rules

| Column | Requirements |
|---|---|
| **Name** | Bold + hyperlinked to the primary project page (GitHub or official website). |
| **Highlights** | One concise sentence describing the project's contribution, ending with a **`[VENUE YEAR]`** tag in bold. |
| **References** | Links separated by ` · `. Include as many as are available: `[GitHub]`, `[arXiv]`, `[Website]`, `[HF]` (HuggingFace). |

---

## Publication Venue Tags

Every entry's **Highlights** column must end with a bolded venue tag:

- Use the **official accepted venue**, not arXiv (arXiv is a preprint server, not a publication).
- Format: `**[ABBREV YEAR]**` — e.g., `**[CVPR 2024]**`, `**[RA-L 2023]**`, `**[RSS 2025]**`.
- Common abbreviations:

  | Full Name | Abbreviation |
  |---|---|
  | IEEE/CVF Conference on Computer Vision and Pattern Recognition | CVPR |
  | International Conference on Computer Vision | ICCV |
  | European Conference on Computer Vision | ECCV |
  | Neural Information Processing Systems | NeurIPS |
  | International Conference on Learning Representations | ICLR |
  | Robotics: Science and Systems | RSS |
  | Conference on Robot Learning | CoRL |
  | IEEE Int'l Conf. on Robotics and Automation | ICRA |
  | IEEE/RSJ Int'l Conf. on Intelligent Robots and Systems | IROS |
  | IEEE Robotics and Automation Letters | RA-L |
  | IEEE Transactions on Robotics | T-RO |
  | International Journal of Robotics Research | IJRR |
  | ACM SIGGRAPH / ACM Transactions on Graphics | ACM ToG / SIGGRAPH |
  | IEEE Transactions on Pattern Analysis and Machine Intelligence | TPAMI |

- If a project is **preprint-only** (no confirmed publication yet), write `**[Preprint]**`.
- If a project has **no paper** (pure library/toolbox), omit the tag entirely.

### How to find the venue

Check these sources in order:
1. The project's **GitHub README** (usually has a citation or "accepted at X" note).
2. The official **project website** or paper page.
3. The **HuggingFace model card**.
4. Search on [Papers With Code](https://paperswithcode.com) or [Semantic Scholar](https://www.semanticscholar.org).

---

## Pull Request Checklist

Before submitting your PR, confirm the following:

- [ ] Entry follows the **three-column table format** exactly.
- [ ] Project name in the **Name** column is bold and linked.
- [ ] Highlights are **one concise sentence** ending with a **venue tag**.
- [ ] Venue has been **verified** from an authoritative source (not inferred from arXiv alone).
- [ ] All **links work** (GitHub, arXiv, website, HuggingFace).
- [ ] Entry is placed in the **correct section** and in a logical position within the table.
- [ ] No **duplicate** entry exists for the same project.
- [ ] Spelling and grammar are correct.

---

## Reporting Issues

If you notice a broken link, incorrect venue, or missing entry, please [open an issue](https://github.com/han-xudong/awesome-robot-vision/issues) with:

- The name of the entry with the problem.
- A short description of the issue.
- (Optionally) the correct information or a suggested fix.
