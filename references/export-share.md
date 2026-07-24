# Export and Share — procedure

Read this only when the user selects **Export visual** or **Share Before/After** at
Compare & Finish. Nothing here is needed for a normal glowup pass.

Both actions operate on the real Before and Final After captures. Never reconstruct
output from memory or present invented terminal text as a capture.

## Export visual

The selection authorizes creating the file and opening it locally. Do not ask for another
confirmation, and do not ask which format — choose it:

- `glowup-before-after.png` for a single-screen comparison or compact storyboard.
- `glowup-before-after.pdf` when the captures are long, several states must remain
  legible, or explanatory notes materially improve the comparison.

Composition:

- **Display:** label both captures and place them side by side only when each stays
  legible; otherwise stack them at the same scale or use separate PDF pages.
- **Flow:** compose a short storyboard of the key states. Offer a recording in addition
  to the visual artifact only when timing, motion, or key sequences matter.
- Use the same command, data, terminal dimensions, font scale, and theme where possible.
  Crop irrelevant shell chrome, not evidence.

Use available deterministic capture or rendering tools. A temporary HTML or SVG renderer
may produce the PNG or PDF, but it is not the exported artifact and should be removed
afterward. Do not install a renderer without approval. If neither format can be produced,
offer SVG or the separate source captures before falling back to Markdown.

Open the file in the appropriate local viewer as soon as it is written, before giving a
recap or doing another selected action. If local opening is unavailable, provide one clear
clickable path and the exact command for opening it. Opening locally never authorizes
uploading, publishing, or sharing. Markdown may accompany the visual for copyable details
and accessibility, but it is not the default export or the file opened first. HTML may
wrap exported captures but is never the source of truth.

If Export and Commit are both selected, keep the export outside the target repository
unless the user explicitly approves adding it.

## Share Before/After

Prepare the comparison even if Export was not also selected. Reuse the existing evidence,
redact it, and create a share-ready PNG. If the primary export is a PDF, create a
representative PNG for sharing. Open the PNG immediately so the user can inspect it.

Add a small "made with glowup" line and install command to the card frame glowup itself
draws (title, border, footer) — never inside the captured tool's own output, which stays
exactly what the target produced.

### Hosting the image so the composer opens with it inline

`gh gist create` cannot take a binary file directly (it rejects PNGs). Work around it:

1. Create the secret gist with a placeholder text file.
2. `git clone` the returned gist URL.
3. `git add` / `commit` / `push` the PNG into it as a normal blob — git has no binary
   restriction even though the `gist create` shortcut does.
4. Get the raw image URL with `gh api gists/<id>`. Pattern:
   `https://gist.githubusercontent.com/<user>/<gist-id>/raw/<blob-sha>/<filename>`

Then open the composer with `title` and `body` pre-filled as URL-encoded query params,
the body containing the markdown image link to that raw URL:

```text
https://github.com/katrinalaszlo/glowup/discussions/new?category=show-and-tell&title=<encoded>&body=<encoded-markdown-image>
```

If gist creation or push fails for any reason, fall back to opening the plain composer URL
and revealing the PNG beside it for manual drag-and-drop rather than blocking the share.

The gist must never be left public — it is secret (unlisted), created solely to host this
image.

### What goes in the post

Only a concise title naming the tool or task, and the inline Before/After image. Put only
the image in the body. Do not add context questions, change summaries, biographies, links,
audit notes, or transcripts unless the user asks. Do not create an Issue or publish a
text-only fallback.

Opening the composer — pre-filled or not — is not publishing. Obtain explicit approval
before any tool submits the Discussion, then immediately open the published page. Never
treat Export alone as permission to share publicly.
