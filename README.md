# Viewer for MuJoCo in Python

Interactive renderer to use with the official Python bindings for MuJoCo.

Starting with version 2.1.2, MuJoCo comes with native Python bindings officially supported by the MuJoCo devs.  

If you have been a user of `mujoco-py`, you might be looking to migrate.  
Some pointers on migration are available [here](https://mujoco.readthedocs.io/en/latest/python.html#migration-notes-for-mujoco-py).

## Install

```sh
git clone https://github.com/ruziniuuuuu/mujoco-python-viewer.git
cd mujoco-python-viewer
pip install .
```

## Usage

```bash
lwmj examples/humanoid.xml # 替换为你的mjcf文件路径
```

Double-click on a geom and hold `Ctrl` to apply forces (using right mouse button) and torques (using left mouse button).

![ezgif-2-6758c40cdf](https://user-images.githubusercontent.com/16384313/161459985-a47e74dc-92c9-4a0b-99fc-92d1b5b04163.gif)

Press `ESC` to quit.  
Other key bindings are shown in the overlay menu (Press `H` or hold `Alt`).
