# install zsh and oh-my-zsh
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# add alias autoformat for autoformatting, typical usage: autoformat **/*.py
echo "alias autoformat='autoformatfun() { autoflake --in-place --exclude alembic --remove-all-unused-imports \$@ && isort \$@ && black \$@ };autoformatfun'" >> ~/.zshrc

# add alias jn for jupyter notebook
jupyter nbextension install https://github.com/drillan/jupyter-black/archive/master.zip --user
jupyter contrib nbextension install --user
jupyter nbextension enable jupyter-black-master/jupyter-black
jupyter nbextension enable execute_time/ExecuteTime

echo "alias jn='jupyter notebook --allow-root --ip 0.0.0.0 --no-browser --notebook-dir /code/notebooks'" >> ~/.zshrc

# seed the history file
echo ": 1569311365:0;autoformat **/*.py" >> ~/.zsh_history
echo ": 1569311395:0;jn" >> ~/.zsh_history
