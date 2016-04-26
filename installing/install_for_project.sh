echo "Я надеюсь вы запустили скрипт от админа ^^ "
echo "Добро пожаловать в установку всякого шлака для работы вашего танчика"
echo "Введите имя пользователя вашей распбери" 

read NAME
echo "Господин, " $NAME ", как ваши дела?"

sudo apt-get update && 
sudo apt-get upgrade &&

sudo apt-get install  htop docker python-dev python-setuptools ipython ipython-notebook python-nose python-sympy git python-virtualenv virtualenvwrapper python-pip openjdk-7-jdk nano zsh npm nodejs libzmq-dev scrot &&

# установка прав вашему пользователю для работы с ардуинкой
sudo apt-get install arduino && sudo usermod -a -G tty $USER && sudo usermod -a -G dialout $USER &&

# для виртауленва (при пользовании bash - не обязательно)#
# .bashrc  и .zshrcе
cd ~ &&
export WORKON_HOME=$HOME/.virtualenvs &&
export PROJECT_HOME=$HOME/Devel &&
source /usr/local/bin/virtualenvwrapper.sh &&

# install python3.5.1  под судо
sudo apt-get install libssl-dev openssl &&
cd /opt &&
wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz &&
tar -xzvf Python-3.5.1.tgz &&
rm Python-3.5.1.tgz &&
cd Python-3.5.1 &&
./configure &&
make && 
sudo make install &&
cd .. && rm -rf Python-3.5.1.tgz &&

###########################
sudo apt-get install python python-tk idle python-pmw python-imaging

###########################
echo "Вроде все ок"


# ------------------pyenv  install python
git clone git://github.com/yyuu/pyenv.git ~/.pyenv &&
mkdir -p ~/.pyenv/plugins &&
git clone git://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv &&
git clone git://github.com/yyuu/pyenv-virtualenvwrapper.git ~/.pyenv/plugins/pyenv-virtualenvwrapper &&
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc &&
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc &&
echo 'eval "$(pyenv init -)"' >> ~/.bashrc &&
#bash && ###############################__________________________________когда перезагружает консольку остальные действия могу не производится
. ~/.bashrc &&
pyenv install 3.5.1 &&
pyenv virtualenv 3.5.1 myenv3.5.1 && #  вирт окружение myenv3.5.1
pyenv local myenv3.5.1