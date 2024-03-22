span style="color:red">Error:</span> This environment is externally managed.
<span style="color:red">Solution:</span> To install Python packages system-wide, try brew install xyz, where xyz is the package you are trying to install.
If you wish to install a non-brew-packaged Python package, create a virtual environment using python3 -m venv path/to/venv. Then use path/to/venv/bin/python and path/to/venv/bin/pip.
If you wish to install a non-brew packaged Python application, it may be easiest to use pipx install xyz, which will manage a virtual environment for you. Make sure you have pipx installed.
<span style="color:purple">Note:</span> If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
<span style="color:cyan">Hint:</span> See PEP 668 for the detailed specification.