# Pirate-ship model log

This folder is one run per model. Each run was asked to build a cinematic pirate ship and to check it with screenshots.

Audited 2026-09-22 from session logs (Cursor transcripts, Codex rollouts, Antigravity brains). None of these folders still contain an image file. Screenshots, when they were taken, went to a temp directory or `/tmp` and were not kept here. A prompt that says "capture screenshots" is not evidence. A screenshot counts only when the session log shows a real capture call (`browser_take_screenshot`, Playwright `page.screenshot` / `canvas.screenshot`, or Chrome "Took a screenshot"), not the instruction text and not a tool-schema line that only defines `screenshot()`.

## Current record

| Folder | Scene file | Screenshots | What the log shows |
| --- | --- | --- | --- |
| `astra-h` | `index.html` | yes | Codex, 2026-09-04. Playwright `page.screenshot` (18 calls), including `work/first.png` and `final-close.png`, `final-desktop.png`, `final-opposite.png`, `final-portrait.png`, `final-square.png`. |
| `astra-lw` | `index.html` | no | Codex, 2026-09-07. Session exists. No capture call. |
| `astra-xh` | `index.html` | yes | Codex, 2026-09-07. Playwright `page.screenshot` (30 calls). Named files include `astra-xh-final-desktop.png`, `astra-xh-final-detail.png`, `astra-xh-final-opposite.png`, `astra-xh-final-portrait.png`, `astra-xh-final-stern.png`, `astra-xh-final-wide.png`. |
| `gem-3.1-pro` | `index.html` | not confirmed | Antigravity, 2026-08-23. Wrote `test_browser.py`, which calls `page.screenshot(path="screenshot.png")`. The log has that script text once and no "Took a screenshot" event. `screenshot.png` is not in the folder. |
| `gem-3.7` | `index.html` | yes | Antigravity, 2026-08-23. 11 "Took a screenshot" events. |
| `gem-3.8f` | `index.html` | yes | Antigravity, 2026-09-02. 6 "Took a screenshot" events. Copies were named `screenshot5.png` and `screenshot6.png` inside this folder at the time; those files are gone now. |
| `gk_4.5-h` | `index.html` | yes | Cursor, 2026-08-25. `browser_take_screenshot`. Named files include `pirate-ship-test-1.png` through later `pirate-ship-final-*.png`, `pirate-ship-verify-a.png`, `pirate-ship-verify-b.png`, `pirate-ship-done.png`, `pirate-ship-establishing.png`, `pirate-ship-complete.png`. |
| `gk_4.6-h` | `index.html` | yes | Cursor, 2026-08-25. Named `gk46h-view1.png`, `gk46h-view2.png`, `gk46h-final.png`, `gk46h-orbit.png`, `gk46h-gallery.png`. |
| `gk_4.6-m` | `index.html` | yes | Cursor, 2026-08-25. The finished run saved `gk46-view1.png`, `gk46-view2.png`, `gk46-view3.png`. Two earlier chats in the parent project stopped before any screenshot. |
| `gk_4.7-h` | `index.html` | yes | Cursor, 2026-09-21. Eight named shots: `hero.png`, `side.png`, `hero2.png`, `hero3.png`, `close.png`, `final-hero.png`, `final.png`, `final2.png`. Shots led to less ocean foam, sails pulled off the mast tops, camera pulled back, a rock removed from the opening view, softer hills, brighter sails. Console was empty. |
| `luna` | `index.html` | yes | Codex, 2026-08-22. 42 `screenshot({fullPage:false})` calls. Later same-folder sessions on 2026-08-23 did not add shots. |
| `mimo-v2.6pro` | `index.html` | yes | Codex, 2026-09-21. Playwright screenshots, including `pirate-wide-2.png`, `pirate-close.png`, `pirate-final-wide.png`, `pirate-final-close.png`, `pirate-verified-wide.png`, `pirate-verified-close.png`. |
| `muse-1.3s` | none | no | Empty folder. No ship file and no ship-build screenshot. |
| `opus-4.6` | `index.html` | yes | Antigravity, 2026-08-23. 5 "Took a screenshot" events. |
| `opus-5.5-med-cursor` | `pirate_ship.html` | yes | Cursor, 2026-09-22. Playwright shots in `/tmp/pirate-build/` (`s1_*.png`, `v_*.png`, `w_*.png`, `x_*.png`) plus 2 `browser_take_screenshot` calls. Shots were used to judge foam streaks, wake shape, and water color. |
| `sol-h` | `index.html` | unknown | No session log names this folder. Do not treat it as the missing `sol` run below. |
| `sol-m` | `index.html` | no | Codex, 2026-09-07. Two sessions. No capture call. |
| `sol-mx` | none | no | Codex, 2026-09-07. Session exists. Folder is empty. No capture call. |
| `sol-xh` | `index.html` | no | Codex, 2026-09-07. Session exists. No capture call. |
| `sol6-max` | `index.html` | no | Codex, 2026-09-22. Session exists. No capture call. |
| `sol6-xhigh` | `pirate-ship.html` | no | Codex, 2026-09-22. Session exists. No capture call. |
| `sonnet-4.6` | `pirate_ship.html` | yes | Antigravity, 2026-08-23. 3 "Took a screenshot" events. |

Runs that were asked for and do not have a folder now:

| Requested folder | Screenshots | What the log shows |
| --- | --- | --- |
| `sol` | yes | Codex, 2026-08-23, wrote `testing_LLMs/sol` and took 32 `screenshot({fullPage:false})` calls. That directory is not in this folder now. |
| `luna6-max` | no | Codex, 2026-09-22. Session exists. No capture call. No `luna6-max` directory. This is separate from `luna`. |

## Rule for the next agent

If you build or change a ship in this directory, append one row to the log below before you finish. Do not edit older rows. Do not mark screenshots "yes" because the prompt required them. Mark "yes" only if you actually captured images, and name the files.

Copy this row:

```
| YYYY-MM-DD | folder | model | screenshots yes/no | count | filenames | what the shots changed | console |
```

## Work log

| Date | Folder | Model | Screenshots | Count | Filenames | What the shots changed | Console |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-22 | `luna` | Codex session for `luna` | yes | 42 | not named in the call (`fullPage:false`) | not recorded in this audit | not recorded |
| 2026-08-23 | `sol` | Codex session for `sol` | yes | 32 | not named in the call (`fullPage:false`) | not recorded in this audit | not recorded |
| 2026-08-23 | `gem-3.7` | Antigravity | yes | 11 | Chrome temp `screenshot.png` | not recorded in this audit | not recorded |
| 2026-08-23 | `sonnet-4.6` | Antigravity | yes | 3 | Chrome temp `screenshot.png` | not recorded in this audit | not recorded |
| 2026-08-23 | `opus-4.6` | Antigravity | yes | 5 | Chrome temp `screenshot.png` | not recorded in this audit | not recorded |
| 2026-08-23 | `gem-3.1-pro` | Antigravity | not confirmed | 0 confirmed | script targets `screenshot.png`, file absent | script written, run not shown | not recorded |
| 2026-08-25 | `gk_4.5-h` | Grok 4.5 | yes | 15 mentions | `pirate-ship-test-*.png`, `pirate-ship-final-*.png`, `pirate-ship-verify-a.png`, `pirate-ship-verify-b.png`, `pirate-ship-done.png`, `pirate-ship-establishing.png`, `pirate-ship-complete.png` | not recorded in this audit | not recorded |
| 2026-08-25 | `gk_4.6-h` | Grok 4.6 | yes | 5 named | `gk46h-view1.png`, `gk46h-view2.png`, `gk46h-final.png`, `gk46h-orbit.png`, `gk46h-gallery.png` | not recorded in this audit | not recorded |
| 2026-08-25 | `gk_4.6-m` | Grok 4.6 | yes | 3 named | `gk46-view1.png`, `gk46-view2.png`, `gk46-view3.png` | not recorded in this audit | not recorded |
| 2026-09-02 | `gem-3.8f` | Antigravity | yes | 6 | `screenshot5.png`, `screenshot6.png` (removed since) | hull height, framing, sail and flag visibility | not recorded |
| 2026-09-04 | `astra-h` | Codex `astra-h` | yes | 18 | `work/first.png`, `final-close.png`, `final-desktop.png`, `final-opposite.png`, `final-portrait.png`, `final-square.png` | not recorded in this audit | not recorded |
| 2026-09-07 | `astra-lw` | Codex `astra-lw` | no | 0 |  |  |  |
| 2026-09-07 | `astra-xh` | Codex `astra-xh` | yes | 30 | `astra-xh-final-desktop.png`, `astra-xh-final-detail.png`, `astra-xh-final-opposite.png`, `astra-xh-final-portrait.png`, `astra-xh-final-stern.png`, `astra-xh-final-wide.png` | not recorded in this audit | not recorded |
| 2026-09-07 | `sol-m` | Codex `sol-m` | no | 0 |  |  |  |
| 2026-09-07 | `sol-mx` | Codex `sol-mx` | no | 0 | empty folder |  |  |
| 2026-09-07 | `sol-xh` | Codex `sol-xh` | no | 0 |  |  |  |
| 2026-09-21 | `mimo-v2.6pro` | Xiaomi MiMo v2.6 Pro via Codex | yes | several | `pirate-wide-2.png`, `pirate-close.png`, `pirate-final-wide.png`, `pirate-final-close.png`, `pirate-verified-wide.png`, `pirate-verified-close.png` | not recorded in this audit | console and page errors were collected in the Playwright script |
| 2026-09-21 | `gk_4.7-h` | Grok 4.7 | yes | 8 | `hero.png`, `side.png`, `hero2.png`, `hero3.png`, `close.png`, `final-hero.png`, `final.png`, `final2.png` | foam reduced, sails moved off mast tops, camera pulled back, near rock removed, hills softened, sail lighting lifted | empty |
| 2026-09-22 | `opus-5.5-med-cursor` | Opus 5.5 medium | yes | 2 browser shots plus Playwright series | `/tmp/pirate-build/s1_*.png`, `v_*.png`, `w_*.png`, `x_*.png` | foam streaks, wake wedge, water color | `THREE.Clock` deprecation, then clean |
| 2026-09-22 | `sol6-max` | Codex `sol6-max` | no | 0 |  |  |  |
| 2026-09-22 | `sol6-xhigh` | Codex `sol6-xhigh` | no | 0 |  |  |  |
| 2026-09-22 | `luna6-max` | Codex `luna6-max` | no | 0 | no folder created |  |  |
| 2026-09-22 | `sol-h` | unknown | unknown |  | no session names this folder |  |  |
| 2026-09-22 | `muse-1.3s` | Muse Spark 1.3 setup only | no | 0 | no scene file |  |  |
