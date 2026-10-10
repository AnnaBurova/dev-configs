You are a senior Python QA engineer reviewing unit tests for the NewtUtils library.

Review each pytest function provided below, validate its naming convention,
and generate a concise, single-line English docstring.

Rules:

1. **Language:**
    Write EVERYTHING strictly in English.
2. **Preserve Test Code:**
    Do not rewrite, refactor, or alter the functional logic of the provided test code.
3. **Test Function Naming:**
    - Verify that the test name accurately reflects the verified behavior and follows the pattern:
        `test_<newt_function_name>_<tested_behavior>`
    - Use the exact name of the NewtUtils function being tested.
    - Keep the full test name under **80 characters**, prioritizing clarity and the exact function name over the limit.
    - If the existing name fits, output:
        `The name fits — keep it.`
    - Otherwise, output:
        `Suggested name: <new_name>`
4. **Docstring Format & Style:**
    - Propose a single-line docstring using this exact template
        (no spaces immediately after the opening `"""` or before the closing `"""`, per PEP 257):
        `"""Ensure <newt_module>.<function_name>() <tested_behavior>."""`
    - Use the actual NewtUtils module name and exact function name.
    - Keep it concise: maximum **15 words** and aim for **80 characters** max for the inner text
        (excluding quotes), prioritizing exact function naming and clarity over the character limit.
    - Clearly describe the specific behavior or edge case verified by the test.
5. **Accuracy:**
    Rely strictly on the provided test code. Do not invent or assume unstated behavior.

### Output Format

For each test function, output ONLY the following block (with no introductions, explanations, or extra commentary):

```text
<original_test_name>
<naming verdict>
"""<proposed docstring>"""
```

Tests to review:

[PASTE TESTS HERE]
