# VS Code Git Workflow (for this project)

This guide explains **how we use Git with VS Code** for this project.  
It’s written for people who may be new to Git or GitHub.

Please follow this workflow — it prevents broken repos and last-minute panic.

---

## What you need (one-time setup)

- **VS Code**
- **Git installed**
  - **Windows:** install *Git for Windows*
  - **Linux:** usually already installed (`git --version` to check)
- A **GitHub account**
- Accept the **collaborator invite** to this repo

> ⚠️ You cannot push to the repo until you accept the GitHub invite.

---

## First-time setup: clone the repo

### Option A (recommended): Clone via VS Code
1. Open **VS Code**
2. Press **Ctrl+Shift+P**
3. Type **Git: Clone**
4. Choose **Clone from GitHub**
5. Sign in to GitHub if prompted
6. Select this repository
7. Choose a folder and open it

VS Code will automatically connect Git and GitHub.

> This method does **not** require SSH keys — VS Code handles authentication.

---

## Daily workflow (how we work safely)

### Always pull before you start
Before coding:
- Open **Source Control** (branch icon on the left)
- Click **Pull** / **Sync** if available  
  *(or click the circular arrows in the bottom bar)*

---

## 🚫 Important rule: never commit directly to `main`

The `main` branch is **protected**.

All work must be done on your **own branch**, then merged via a Pull Request.

---

## Create your own branch

1. In the bottom-left of VS Code, click the branch name (`main`)
2. Select **Create new branch…**
3. Name it using this format:

feature-<yourname>-<what-you-did>


Examples:
- `feature-nyx-parser`
- `feature-sam-scheduler`
- `feature-alex-cli`

VS Code will switch to your new branch automatically.

---

## Make changes
Edit files and save normally.

---

## Commit your changes

1. Open **Source Control**
2. Review the changed files (click to see diffs)
3. Write a clear commit message, e.g.:
   - `Parse constraints section`
   - `Add greedy scheduler`
4. Click **Commit**

> ✅ Keep commits small and focused.

---

## Push your branch

After committing, VS Code will show **Publish Branch** or **Push**.

- Click **Publish Branch / Push**

Your branch is now on GitHub.

---

## Open a Pull Request (PR)

After pushing, VS Code may offer **Create Pull Request** — click it if you see it.

Otherwise:
1. Go to the GitHub repo in your browser
2. Open **Pull Requests**
3. Click **New Pull Request**
4. Set:
   - **base:** `main`
   - **compare:** your branch
5. Create the PR

Post a short message in the group chat like:
> PR up: `feature-…` — ready for review

---

## Merging

Once approved:
- Merge the PR on GitHub
- In VS Code:
  - Switch back to `main`
  - Pull latest changes

---

## Common problems & fixes

### ❌ “I can’t push / permission denied”
- Make sure you accepted the repo invite
- Make sure you’re logged into the **correct GitHub account** in VS Code:
  - Accounts icon (bottom-left) → Sign in

---

### ❌ “My branch is behind `main`”
Fix:
1. Switch to `main`
2. Pull latest
3. Switch back to your branch
4. Merge `main` into your branch:
   - **Ctrl+Shift+P → Git: Merge Branch… → main**
5. Commit if prompted, then push again

---

### ❌ VS Code can’t find Git
- Install Git
- Restart VS Code

---

## Emergency fallback (terminal only if needed)

Open the VS Code terminal and run:

```bash
git status
git pull
git checkout -b feature-yourname-thing
git add <files>
git commit -m "message"
git push -u origin feature-yourname-thing
```
