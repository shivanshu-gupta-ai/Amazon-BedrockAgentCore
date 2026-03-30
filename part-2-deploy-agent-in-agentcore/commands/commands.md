# Setup Commands for Mac

> Ensure your Python version is 3.12 or higher before continuing.

## Step 1: Update Homebrew and install pyenv

Install Homebrew:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Reload the shell and verify Homebrew:

```bash
exec zsh
brew --version
```

Update Homebrew and install pyenv:

```bash
brew update
brew upgrade
brew install pyenv
```

## Step 2: Set up pyenv in your shell

Append pyenv environment configuration to `~/.zshrc`:

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

Reload the shell:

```bash
exec zsh
```

## Step 3: Install Python 3.13

```bash
pyenv versions
pyenv install 3.13
```

## Step 4: Set Python 3.13 as the global default

```bash
pyenv global 3.13
```

## Step 5: Verify the installation

```bash
pyenv versions
python --version
python3 --version
pip --version
```

## Step 6: Upgrade pip and install AWS CLI

```bash
pip install --upgrade pip
pip install awscli --upgrade
```

## Step 7: Configure AWS credentials

```bash
aws configure
```

> Use the credentials provided by your AWS setup.

## Step 8: Create and activate a Python virtual environment

```bash
python -m venv bedrock-env
source bedrock-env/bin/activate
```

## Step 9: Install required Python packages

```bash
pip install --upgrade pip
pip install --upgrade requests urllib3 charset-normalizer
pip install bedrock-agentcore strands-agents bedrock-agentcore-starter-toolkit
```

## Step 10: Verify agentcore installation

```bash
agentcore --help
```

## Step 11: add codefile and configure

```bash
agentcore configure -e myagent.py
```

## Step 12: Deploy

```bash
agentcore deploy
```
