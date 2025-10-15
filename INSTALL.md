# How to use some Tools

## `./scripts/check_gitattributes.sh`

To check if all files have a corresponding rule in .gitattributes, this script can be used in **bash**:

```sh
missing_attributes=$(git ls-files | git check-attr -a --stdin | grep 'text: auto' || printf '\n')

if [ -n "$missing_attributes" ]; then
  printf '%s\n%s\n' '.gitattributes rule missing for the following files:' "$missing_attributes"
else
  printf '%s\n' 'All files have a corresponding rule in .gitattributes'
fi
```

You can also use the checked-in script which has more features.

```bash
./scripts/check_gitattributes.sh
```
OR
```bash
../dev-configs/scripts/check_gitattributes.sh
```

Run with `--help` for the available options.

Requires Git and Bash.
