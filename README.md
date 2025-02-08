# MLops-project


# environment
conda create -n visa python=3.8 -y

conda activate visa

pip install -r requirements.txt

# Github commands
git add .

git commit -m "Updated"

git push origin main

nano ~/.zshrc  # For zsh users
# or
nano ~/.bashrc  # For bash users

export LIBOMP_DIR="/opt/homebrew/opt/libomp/lib"
export DYLD_LIBRARY_PATH="$LIBOMP_DIR:$DYLD_LIBRARY_PATH"

source ~/.zshrc  # Or `source ~/.bashrc` for bash users

# workflow

1.constants
2.entity
3.components
4.pipeline
5.Main file
