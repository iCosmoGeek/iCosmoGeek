# GitHub Actions Workflows

This repository uses GitHub Actions for automated publishing and deployment.

## Workflows

### 1. `hugo-deploy.yml` - Hugo Site Deployment
**Purpose:** Automatically builds and deploys your Hugo site to GitHub Pages

**Triggers:**
- ✅ **Push to main branch** - Deploys immediately when you push changes
- ✅ **Hourly schedule** - Runs every hour to publish scheduled posts
- ✅ **Manual trigger** - Can be triggered manually from GitHub Actions tab

**How it works:**
- Builds your Hugo site with all posts dated <= current time
- Deploys to GitHub Pages automatically
- Posts with future dates are excluded until their scheduled time

### 2. `publish-weekly.yml` - Weekly Roundup Generator
**Purpose:** Generates weekly roundup posts from Google Sheets

**Triggers:**
- Every Monday at 8 AM PT
- Manual trigger

### 3. `share-on-social.yml` - Social Media Sharing
**Purpose:** Shares posts to LinkedIn, X (Twitter), and Facebook

**Triggers:**
- Manual trigger only

## Scheduling Blog Posts

To schedule a post for future publication:

1. Create your post with a future date in the front matter:
   ```markdown
   +++
   title = "My Post Title"
   date = "2025-10-25T14:30:00-08:00"  # Oct 25 at 2:30 PM PST
   draft = false
   +++
   ```

2. Push to GitHub
3. The post will automatically publish at the scheduled time (within 1 hour)

### Time Format Examples:
- `"2025-10-23T08:00:00-08:00"` - 8:00 AM PST
- `"2025-10-23T14:30:00-08:00"` - 2:30 PM PST
- `"2025-10-23T20:15:00-08:00"` - 8:15 PM PST

### Important Notes:
- Posts are published during the next hourly build after their scheduled time
- Maximum delay: 59 minutes from scheduled time
- Set `draft = false` for posts to be published
- Use correct timezone offset (`-08:00` for PST, `-07:00` for PDT)

## First-Time Setup

### Enable GitHub Pages:
1. Go to repository Settings → Pages
2. Under "Source", select "GitHub Actions"
3. Save

That's it! Your site will now deploy automatically.

## Manual Deployment

To manually trigger a deployment:
1. Go to Actions tab
2. Select "Deploy Hugo site to Pages"
3. Click "Run workflow"
4. Select branch (main)
5. Click "Run workflow"
