# Make.com Automation Workflows

Three automated workflows for maintaining and distributing echo-payload.

---

## Flow A — Repo Creation Pipeline

**Trigger:** Manual or Notion page update webhook

```
Module 1: Webhook / Notion Watch Database
Module 2: Notion — Get Page Content
Module 3: Canva Pro — Generate Images (Bulk Create)
  └─ Hero banner (1200×630), Social preview, Packet cards (800×800 x10)
Module 4: GitHub — Create Repository (public, topics set)
Module 5: GitHub — Commit Multiple Files (all 50+ files)
Module 6: GitHub — Upload visual assets to assets/
Module 7: Facebook — Post launch announcement + hero image
```

---

## Flow B — Content Update Pipeline

**Trigger:** Notion page updated

```
Notion Watch → Get diff → Router:
  Route A: Packets changed → Canva regenerate packet cards
  Route B: Docs only → skip Canva
  Route C: Both → regenerate all
→ GitHub commit → Facebook update post
```

---

## Flow C — Community Engagement

**Trigger:** GitHub webhook (issue labeled "good first issue" OR first-time contributor PR merged)

```
GitHub Webhook → Router:
  Branch A: New issue → Canva issue card → Facebook post
  Branch B: Contributor → Canva thank-you card → Facebook post
```

---

## Webhook Setup

```
GitHub: https://hook.make.com/[your-webhook-id]
Events: Issues, Pull Requests, Push

Notion: Make Watch Database module
Database ID: [echo-payload build sheet ID]
Poll interval: 15 minutes
```
