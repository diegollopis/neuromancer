# neuromancer
A fancy name for a python script that automates all steps of a git commit into a single command, streamlining your workflow by combining multiple git commands and following the rules of a semantic commit message.

# Features
- Automates the process of:
  - Adding files (`git add .`)
  - Committing changes (`git commit -m "your message"`)
  - Pushing to the current branch (`git push`)
- Customizable commit messages
- Easy to integrate with your existing workflow

# Requirements

- **Python 3** must be installed on your system.

# How to Use
- Clone this repository.
- Go to repo that you want to commit changes and type 

```
python3 /path/to/your/repository/app.py commit_type commit_message
```

# Setting up an Alias

To make the script easier to run, you can create an alias for app.py. This allows you to use a short command instead of typing the full path every time.

## macOS (Bash)
Open the terminal and edit the .bash_profile:
```
nano ~/.bash_profile
```

Add the following line:
```
alias alias_name="python3 /path/to/your/repository/app.py"
```

alias_name can be any name that you like. For example, 

```
alias neuromancer="python3 /path/to/your/repository/app.py"
```

Save and exit (Ctrl+O, Enter, Ctrl+X), then reload the profile:
```
source ~/.bash_profile
```

## macOS (oh-my-zsh)

Edit the .zshrc file:
```
nano ~/.zshrc
```

Add the following line:
```
alias alias_name="python3 /path/to/your/repository/app.py"
```

Save and exit (Ctrl+O, Enter, Ctrl+X), then reload the profile:
```
source ~/.zshrc
```

# Usage Example

After setting up the alias, you can commit and push changes with a single line:

```
alias_name commit_type commit_message
```

An example would be:
```
neuromancer refactor improve function code
```

# Important

Only few commit types are allowed: feat, fix, docs, style, refactor, test and chore.

If you have doubts which one is more adequate for the occasion, use the command below:

```
alias_name_you_choose help
```

# Contributing
Feel free to contribute to this project by submitting pull requests or opening issues.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
