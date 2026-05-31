# Publishing to JetBrains Marketplace

This is a one-time form submission. After it's approved, users find the theme via
**Settings → Plugins → Marketplace → search "GuydAI"** in any JetBrains IDE.

## Before you start

You'll need:
- A JetBrains account (the same one you use to sign in to PyCharm — free).
- The latest `GuydAI-Theme.jar` from this repo's root (currently **v1.2.0**, ~9.7 KB).
- ~5 minutes for the form.

## Steps

### 1. Sign in to the Marketplace
Open <https://plugins.jetbrains.com/> and click **Sign In** (top right).
Use your existing JetBrains account.

### 2. Upload
Click your avatar → **Upload Plugin** (or go to <https://plugins.jetbrains.com/plugin/add>).
- **File:** `GuydAI-Theme.jar` from the repo root.
- The Marketplace reads `plugin.xml` and pre-fills: name, version, vendor, description,
  change notes, category, icon, since-build. You should NOT need to edit those.

### 3. Fill in the listing fields
The form will show some fields the `.jar` can't pre-fill. Use these:

| Field | Value |
|---|---|
| **Short description** *(≤120 chars, shown in search results)* | `Cyber dark theme with electric-blue & hot-pink neon accents on pure-black chrome, plus a navy + gold editor color scheme.` |
| **Tags** | `theme`, `dark`, `cyberpunk`, `neon`, `color-scheme` |
| **License** | `MIT` |
| **License URL** | `https://github.com/GuydAI/guydai-theme/blob/main/LICENSE` |
| **Source code URL** | `https://github.com/GuydAI/guydai-theme` |
| **Bug tracker URL** | `https://github.com/GuydAI/guydai-theme/issues` |
| **Documentation URL** | `https://github.com/GuydAI/guydai-theme#readme` |
| **Vendor name** | `GuydAI` |
| **Vendor URL** | `https://guydai.com` |
| **Vendor email** | `admin@guydai.com` |

### 4. Add screenshots
Upload from `preview/`:
1. `side-by-side.png` — navy vs pure-black editor schemes (lead shot).
2. `pure-black.png` — the standalone pure-black variant.
3. `cyber-ice.png` — the original Cyber Ice + navy editor shot.

You can add up to 5. The `.html` files in `preview/` are sources you can re-render
at any time if you want more variations.

### 5. Submit for moderation
Click **Submit**. JetBrains reviews first-time plugins manually — usually
**1-3 business days**. You'll get an email when it's live. After that, future
version uploads are auto-approved as long as `plugin.xml` doesn't change in
suspicious ways.

## Pushing a new version later

Once approved, releasing an update is a 30-second flow:

1. Edit files under `src/`, bump `<version>` in `plugin.xml`, update `<change-notes>`.
2. `./build.ps1`
3. Marketplace → your plugin's page → **Update Plugin** → upload the new `.jar`.

### Updating while still in initial moderation

If you want to ship a new version *before* the first review finishes (e.g. you
uploaded v1.1.2 and want moderators to see v1.2.0 instead):

1. Build the new `.jar` (`./build.ps1`).
2. Marketplace → your plugin's page → **Update Plugin** → upload the new `.jar`.
3. The newer build supersedes the pending one — moderators review whatever the
   latest version is, and you generally keep your queue position.

You don't lose the existing listing or have to re-submit the form.

The Marketplace also offers a **command-line publish** via `gradle-intellij-plugin`
or `intellijPlatform` — overkill for a theme plugin, but worth knowing if you ever
want CI to auto-publish on a Git tag.

## Things people sometimes ask

- **Plugin ID conflict?** Our ID is `com.guydai.theme`. Marketplace will reject a
  duplicate, but that ID is unique to your domain so you're fine.
- **Pricing?** Leave it as **Free**. JetBrains takes ~30% if you ever charge, and
  no one pays for themes anyway.
- **Why "Theme" not "UI"?** Marketplace's theme browser specifically pulls from
  the `<category>Theme</category>` declaration in `plugin.xml`. We set it.
- **Does Marketplace need the GitHub repo to stay public?** No — but if it goes
  private, the in-IDE Overview screenshot (`raw.githubusercontent.com`) will 404.
