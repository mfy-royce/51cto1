# ! /usr/bin/python
# encoding: utf-8

"""
author:Max
contact:mfy-111@163.com
@file: envs_config.py
@time:  20:24
@welcom to learn ai
"""
def envsConfig():
    context = """ 
    conda info --envs \ conda env list      # 要查看所有环境的列表
    conda create --name env_name python=3.5     # 创建一个名为“env_name”的新环境，其中包含Python 3.5
    conda create --name new_env_name --clone old_env_name       # 备份当前conda环境`old_env_name`到`new_env_name`
    conda activate env_name \ source activate env_name      # 激活某个环境
    conda deactivate \ source deactivate        # 停用环境并返回基础环境
    conda env remove -n env_name        # 删除某个环境conda env remove -n 环境名conda install package-name称
    
    conda list      # 列出当前conda环境下所有package及版本
    conda install package-name
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge 
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/

    config pycharm : settings --> scheme font templates interpreter 
    """
    print(context)

def codeStyle():
    """

    jjjjjjj
    """
    context = """ https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/contents/
                    https://www.runoob.com/w3cnote/google-python-styleguide.html
                   https://github.com/mfy-royce 
    config pycharm : settings --> github git 
    git-bash :  git config --global user.name  mfy-royce
                git config --global user.email mfy-111@163.com
    """
    print(context)

def gitConfig():
    """
    git-bash :  git config --global user.name  mfy-royce
                git config --global user.email mfy-111@163.com
                git config --list

                ssh-keygen -t rsa -C "mfy-111-mfy@163.com"
                git clone git@47.94.6.102:20200116322/course-info.git
                git add --a
                git commit  -m "测试"
                git push -u origin master
    """
if __name__ =="__main__":
    # envsConfig()
    #     # codeStyle()
    help(codeStyle)

