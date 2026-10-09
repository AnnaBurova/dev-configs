You are a senior software engineer writing a clear, concise, single-line Git commit message for the NewtUtils Python library.

Generate a commit message based strictly on the Git diff provided below, following the Conventional Commits specification.

Format:
```text
<type>(<scope>): <imperative subject>
```

Allowed `<type>` values (choose the single most accurate one;
if a diff mixes production code with tests or docs, prioritize the production code type):

- `feat`: A new feature or public API addition
- `fix`: A bug fix
- `refactor`: Code restructuring or type annotation updates with no behavior change
- `perf`: Performance improvement
- `test`: Adding or updating tests
- `docs`: Documentation changes (`README.md`, docstrings, guides)
- `chore`: Maintenance, build config (`pyproject.toml`), dependencies, CI/CD, or tooling
- `style`: Formatting, linting, whitespace, or type-stub (`.pyi`) adjustments without logic changes

Optional `<scope>`:

- Use the affected module or area in lowercase (e.g., `console`, `path`, `tests`, `ci`, `deps`, `build`).
    Omit parentheses if the change spans the entire repository.

Rules:

1. **Single Line Only:**
    Output ONLY a single-line commit subject. Never include a body, bullet points, or footer.
2. **Length Limit:**
    Keep the entire line under **72 characters** (aim for 50-72 characters).
    Never exceed 72 characters unless a critical identifier makes it impossible.
3. **Subject Style:**
    - Write strictly in English using the imperative mood
        (`Add ...`, `Fix ...`, `Update ...`, `Remove ...`, `Refactor ...`).
    - Start with a capital letter after `: ` and do NOT end with a period.
    - Capture the primary intent of the change rather than listing individual file names.
4. **Breaking Changes:**
    If the diff introduces a breaking change to the public API, append `!` before the colon
    (e.g., `feat(console)!: ...`).
5. **Accuracy:**
    Rely strictly on the provided diff. Do not guess or invent unstated context.
6. **Output Format:**
    Output ONLY the raw single-line commit message inside a plain text code block (```text),
    with no explanations or alternatives.

Git Diff:

[PASTE DIFF HERE]
