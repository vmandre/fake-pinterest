# fake-pinterest


# 🐍 Setting Up a Python Virtual Environment on Linux

Follow these steps to create and manage a Python virtual environment on Linux.

---

## 📚 Table of Contents

- [1. Install Python and venv Module](#-1-install-python-and-venv-module)
- [2. Create the Virtual Environment](#-2-create-the-virtual-environment)
- [3. Activate the Virtual Environment](#-3-activate-the-virtual-environment)
- [4. Install Packages Inside the Virtual Environment](#-4-install-packages-inside-the-virtual-environment)
- [5. Deactivate the Virtual Environment](#-5-deactivate-the-virtual-environment)
- [6. Install requirements.txt](#-6-install-requirementstxt)
- [7. Create Database](#-7-create-database)
- [8. Run the app](#-8-run-the-app)

---

## ✅ 1. Install Python and venv Module

First, ensure you have Python and the `venv` module installed:

```bash
sudo apt update
sudo apt install python3 python3-venv
```

You can verify Python installation:

```bash
python3 --version
```

---

## ✅ 2. Create the Virtual Environment

Navigate to your project directory:

```bash
cd /path/to/your/project
```

Then create a virtual environment:

```bash
python3 -m venv .venv
```

> This will create a `.venv/` folder inside your project.

---

## ✅ 3. Activate the Virtual Environment

Activate the virtual environment using:

```bash
source .venv/bin/activate
```

You should see your shell prompt change to:

```bash
(.venv) user@machine:~/yourproject$
```

---

## ✅ 4. Install Packages Inside the Virtual Environment

Now you can install packages locally without affecting your system-wide Python:

```bash
pip install package-name
```

Example:

```bash
pip install requests flask
```

---

## ✅ 5. Deactivate the Virtual Environment

When you're done working:

```bash
deactivate
```

This will return your shell to the system environment.

---

## ✅ 6. Install requirements.txt

To install all required packages in one shot:

```bash
pip install -r requirements.txt
```

It's the same as:
```bash
pip install flask-sqlalchemy flask-login flask-bcrypt email_validator flask flask-wtf
```

---

## ✅ 7. Create Database

```bash
python3 create_database.py
```

---
---

## ✅ 8. Run the app

```bash
python3 main.py
```

---