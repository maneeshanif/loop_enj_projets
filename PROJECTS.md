# Project 1 - In-Session Loop Monitoring

**Difficulty:** easy · **Uses:** Concept 4 (in-session loop)

**Build.** Start a long task in your repo (for example, a script that sleeps for a while and then writes a file). Set up an in-session loop that checks every minute whether the task has finished, and tells you the moment it has.

**Done when** the loop notices the task finished, says so once, and you can stop it cleanly, and you never sat watching the terminal.

---

# Project 2 - Conditional Loop: Make Tests Pass Then Stop

**Difficulty:** easy to medium · **Uses:** Concept 5 (conditional loop), Concept 11 (maker-checker)

**Build.** Put 2 or 3 small failing tests in your repo. Build a loop that keeps working until the tests pass, but let a *command* (the test runner), not the agent, decide when it is done. Cap it at, say, 6 tries.

**Done when** the loop stops because the tests actually passed, not because it hit the cap. If it keeps hitting the cap, your stop condition or your prompt needs work. That is the lesson.

---

# Project 3 - The Morning Brief with Memory

**Difficulty:** medium · **Uses:** Concept 6 (unattended schedule), Concept 12 (the spine)

**Build.** Make a scheduled loop that runs once, reads a `progress.md`, gathers something simple from the repo (open `TODO` comments, or the last day's commits), writes a short summary, and updates `progress.md` with what it found and the date.

**Done when** you run it twice and the second run clearly builds on the first, meaning it does not repeat what it already recorded. That proves your spine works. If the second run starts from nothing, your loop has no memory yet.

---

# Project 4 - Fix Loop with Real Checker

**Difficulty:** medium to hard · **Uses:** Concept 8 (worktree), Concept 9 (skill), Concept 11 (maker-checker)

**Build.** A smaller version of the Part 5 loop. Write a short skill with your fix steps, and a reviewer agent that replies `PASS` or `FAIL`. Take one real bug, have the implementer draft a fix in its own checkout (worktree or branch), and let the reviewer grade it. Open a PR only on `PASS`.

**Done when** two things are both true: a good fix gets a `PASS` and a PR, *and* a deliberately bad fix you plant gets a `FAIL` with reasons. If the reviewer passes the bad fix, your checker is too soft, so tighten it. A checker that approves everything is no checker.

---

# Project 5 - Codify the Body

**Difficulty:** medium to hard · **Uses:** the [dynamic-workflows interlude](#11b-codify-the-body), Concepts 8 and 11

**Build.** Take the fix loop you built in Project 4 and codify its body. On the Claude Code approach, describe it in plain words: "use a workflow to draft fixes for these three issues in parallel worktrees, and have a reviewer grade each one." Let the runtime write and run the script. When a run does what you want, save it from the `/workflows` view as a `/command`. On the OpenCode approach, write the same thing as a shell script: a `for` loop over the candidates, `&`/`wait` for the fan-out, and the reviewer's exit code as the checker. Run it twice.

**Done when** two things are true. First, one command (or one script) runs the whole draft-and-review body, meaning several candidates, isolated checkouts, and a verdict for each, with no step-by-step prompting from you. Second, you have proved the interlude's warning on your own machine: start a fresh session (or a fresh shell) and confirm the workflow remembers nothing from its last run. Then name what it would need to become a loop: a heartbeat to fire it, and a progress file its agents write. If you can name those two, you understand the difference between an engine and a loop. (Dynamic workflows are a research preview, so where this project and the live docs disagree, the docs win.)

---

# Project 6 - The Doorbell Loop

**Difficulty:** medium · **Uses:** Concept 7 (event-driven), Concept 10 (connectors)

**Build.** Make your throwaway repo review its own pull requests. On the OpenCode approach, run `opencode github install` and accept the workflow it generates. On the Claude Code approach, create a Routine with a GitHub pull-request trigger (the [appendix](#appendix-routines) walks through the filters). Then open a PR that contains one planted bug, such as an off-by-one or a deleted null check, and wait.

**Done when** the PR gets a review you never asked for, and the review flags the planted bug. If the review misses it, tighten the prompt and push again. The push fires the loop once more through the synchronize event, and that re-fire is the event heartbeat working. With Projects 1 to 3, this completes all four heartbeats: in-session, conditional, scheduled, and event-driven.

---

# Project 7 - Break It on Purpose

**Difficulty:** medium · **Uses:** [Observability](#observability), Concept 13 (cost), Concept 14

**Build.** Take your Project 3 loop. First, measure one beat: note roughly how many tokens a run reads and writes, and multiply by your cadence to get a monthly cost, which is Concept 13's math on your own loop. Then sabotage it: point the prompt at a file that does not exist, or give it a success condition it can never meet (with a limit set). Let it fire on schedule and fail. Now diagnose the failure using only what the loop left behind, meaning the log line and `progress.md`, without replaying the full run.

**Done when** three things are true. You can say what failed, and when, from the spine alone. The loop left a clear "needs a human" note instead of failing silently. And you know your loop's monthly cost at its current cadence. If it failed silently, fix that before anything else by adding the log line. You are rehearsing the overnight failure now, while it is cheap and you are watching.

---

# Project 8 - Your Own Daily Loop (Capstone)

**Difficulty:** capstone · **Uses:** all six parts

**Build.** Pick one real, boring, recurring chore in a project you actually work on: a dependency audit, a docs-freshness check, a changelog draft, a lint sweep. Build the full loop: heartbeat, worktree, skill, maker-checker, connector, and the spine. Add budget guards. Let it run.

**Done when** it has run unattended for a week and you trust what it ships *because you read it*, not because you stopped reading. Then answer Concept 15 honestly: did your understanding of the project keep up with what the loop changed? If not, slow the loop down until it does. (When it fails overnight, and it will, work through [When an unattended loop fails](#observability) before you blame the model.)

---

# Project 9 - Rehearse a Routine for Free

**Difficulty:** easy · **Uses:** A1, A3 (one-off schedules), A5 (reading runs)

**Build.** In a throwaway repo, create a routine whose prompt does one small, checkable thing, for example summarizing yesterday's commits onto a `claude/summary` branch. Do not put it on a repeating schedule. Fire it with a one-off run (`/schedule tomorrow at 9am, …` or *Run now*) and read the full transcript, not the status column. Then change the prompt so the task must fail, by having it read a file that does not exist, and fire it once more.

**Done when** you have seen two green runs: one whose transcript shows success, and one whose transcript shows failure. You should be able to say, in one sentence, why the status column could not tell them apart. That sentence is the A5 lesson: green means the session ended without an infrastructure error, nothing more.

---

# Project 10 - The Secrets Drill

**Difficulty:** easy to medium · **Uses:** A4 (secrets), A2 (the environment)

**Build.** Write a prompt that needs one secret. A dummy token is fine, because the drill is about where the value lives, not what it unlocks. First run: put the token in a gitignored `.env` file and fire the routine. Watch it fail to find the value, and read the transcript to see what Claude tried instead. Second run: move the token into the environment-variables panel, and add the one prompt line the appendix recommends: *"credentials are available as environment variables; do not look for a `.env` file."*

**Done when** the second run reads the token from the environment, and you can explain the mechanical reason the first run could not: gitignored files never reach GitHub, so the fresh cloud clone never contains them.

---

# Project 11 - Build the Two-Routine Gate

**Difficulty:** medium to hard · **Uses:** A3 (the API trigger), A4 (the gate), A6 (the checklist)

**Build.** Routine A, on a one-off schedule, drafts something reviewable: a `claude/` branch, or a short summary posted through a connector. Routine B has an API trigger and performs one small follow-up action. Store B's bearer token the moment it is shown, because it is shown once. Review A's draft yourself. Then approve it by firing B with the `curl` call from A3.

**Done when** three things are true: B ran only because you fired it, B's transcript shows the action actually happened, and you have run the A6 checklist over both routines, with connectors pruned, unrestricted pushes off, and a state file chosen. This is the human gate from Part 5, and now you have built it out of real parts.

---

# Project 12 - Build a Dreaming Loop (Capstone)

**Difficulty:** capstone · **Uses:** Concept 12 (spine and improvement loop), Concept 11 (maker-checker), Concept 6 (schedule), Part 5 (human gate)

**Build.** You need a loop that has already run for a week and left dated entries in `progress.md` (Project 3 or Project 8 gives you one). Now build a second loop over it. On a weekly schedule, it reads all log entries since the date in its own `dreaming-state.md`, looks for any failure or correction that appears more than once, and drafts the smallest rules-file or skill change that would prevent it, as a PR on a `claude/` branch, never a direct commit. The PR description must cite its evidence: which runs, how often, and why this line stops it. Have it also propose one deletion: a rule no recent run needed. Finish by updating `dreaming-state.md`.

**Done when** three things are true. The PR's proposed change traces to real, cited log entries, not a plausible-sounding guess. A deliberately planted repeated failure in the logs (add one by hand) gets caught and turned into a proposal. And nothing changed in your rules file without you merging it. If the loop proposes changes with no evidence attached, tighten the prompt: an improvement loop that guesses is worse than no improvement loop, because its guesses steer every future run.