# neuromancer
Just a fancy name for a python script that automates all the steps of a git commit into a single terminal command, streamlining your workflow, saving you time and effort by combining multiple git commands into one.

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
- Go to the repo that you want to commit changes and type 

```
python3 /path/to/your/repository/app.py commit_type commit_message
```

# Setting up an Alias

To make it easier to run the script, you can create an alias for app.py. This allows you to use a short command instead of typing the full path every time.

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
alias commit_type commit_message
```

An example would be:
```
neuromancer refactor improve function code
```

# Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the functionality or fix bugs.

# License

This project is licensed under the MIT License - see the LICENSE file for details.

```
This README covers the essential details, including installation, usage, and alias setup for macOS, Windows, and oh-my-zsh environments. If you need more customization or additional sections, let me know!
```
