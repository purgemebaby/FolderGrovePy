
<div align="center">
    <img src="https://i.imgur.com/SMVjsy3.png" alt="logo" width="150" height="150px"/>
    <br>
    <a href="https://www.python.org/">
        <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" alt="forthebadge made-with-python"/>
    </a>
    <h3>A CLI tool to setup your projects faster ;) !!!</h3>
</div>

<div align="center">
    <p></p>
</div>

---

<h2 align="center">🌳 What is Folder Grove?</h2>
<p>
<strong>Folder Grove</strong> is a tool that helps you instantly set up the folder structure for your projects. It allows you to pre-save multiple templates with project structures in a single text file, with the depth and number of folders you desire.

Folder Grove features:
- Compatibility with Windows and Linux
- An user-friendly and easy-to-use CLI
- Interactive terminal
- An option to display a <strong>directory tree</strong> of your saved templates
</p>

---

<h2 align="center">🎥  Tool Showcase</h2>


<h3>Option 1: Create a new Project</h3>

![option1](https://github.com/purgemebaby/FolderGrovePy/blob/main/img/option%201.gif)

<h3>Option 2: Save a Template</h3>

![option2](https://github.com/purgemebaby/FolderGrovePy/blob/main/img/option%202.gif)

<h3>Option 3: Load a Template</h3>

![option3](https://github.com/purgemebaby/FolderGrovePy/blob/main/img/option%203.gif)

<h3>Option 4: See Tree (Templates)</h3>

![option4](https://github.com/purgemebaby/FolderGrovePy/blob/main/img/option%204.gif)

<br>

---


<h2 align="center">🤓How to Install and Start</h2>
<h3 align="center">1. 📋 Requirements</h3>

First of all, ensure you have the following software installed and updated:
- **Python 3.8 or higher**: You can check your Python version with `python --version` or `python3 --version`.
- **Poetry**: A dependency management tool for Python. You can install Poetry following the instructions in the [official documentation](https://python-poetry.org/docs/).

<h3 align="center">2. 🚀 Installation</h3>
<h4 align="center">2.1 📥 Downloading </h4>

You can download Folder Grove by **cloning this repository**:

```shell
git clone https://github.com/purgemebaby/FolderGrovePy.git
```

To run the app, you need to grant **execution permission**:
```shell
chmod +x FolderGrovePy/folder_grove/main.py
```

<h4 align="center">2.2 👩‍💻 Creating and Activating a Virtual Environment. </h4>

**Poetry** will handle the virtual environment for you. Go into the project's directory and run:

```sh
poetry install
```

This command will install all necessary dependencies specified in the **pyproject.toml** file and create a virtual environment.

To **activate** the virtual environment created by **Poetry**, use:

```shell
poetry shell
```
This will open a new shell session within the virtual environment.



<h4 align="center">2.3 🏃 Running the app </h4>

To use the app, simply run main.py:
```shell
python main.py
```

**Note**: You can creat a symlink to the script in your home directory for convenience.




<h3 align="center">4. ⚙️ Configuration file. </h3>

There is a **config.json** in `FolderGrovePy/folder_grove/config` where you can adjust the saving template location and your projects creation directory. By default, **config.json** looks like this:

```JSON
{
    "creationPath": "pwd",
    "savingPath": "default"
}

```

- **creationPath**: path where projects are created. If set to *"pwd"*, the script will create the project in your current working directory.
- **savingPath**: path to a ``.txt`` file where templates are saved. If set to *"default"*, the script will use `template.txt` file (located in ``FolderGrovePy/folder_grove/config``) to read and save the templates you create.

If you want to change these values, make sure you use ***absolute paths***. Restrain from using `~`. For example:

```JSON
{
    "creationPath": "/home/user/Downloads",
    "savingPath": "/home/user/fg_templates.txt"
}

```

---
