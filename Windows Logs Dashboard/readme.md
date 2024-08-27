
# Windows Logs Dashboard

A Desktop application that retrieves and displays Windows Event Logs (default upto 5 latest entries) with interactive charts to visualize log severity distributions.

## Features

- **Log Viewing**: View logs from Application, System, and Security categories in a structured table format.

- **Severity Charts**: Interactive pie charts to visualize log severity distributions.

## Note

1. To increase the number of log entries, modify line 21 in app.py. (The package would need to be rebuild)

```Python3
for event in events[:5]:
```

2.If time format error occurs, use the following command to adjust accordingly

```Powershell
Get-Date
```

3. Run as Administrator for access to Security logs.

## Prerequisites

Only if modifying app.py

- Flask
- pywin32 (for win32evtlog)
- pyutils
- pyInstaller

To build executable; -

```Powershell
pyinstaller --onefile --name=my_flask_exe app.py

pyinstaller my_flask_exe.spec

```
After PyInstaller finishes, you can find the standalone executable in the dist directory.

## Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/en/3.0.x/)
- [PyInstaller Documentation](https://pyinstaller.org/en/stable/index.html)
- [pywin32 Documentation](https://pypi.org/project/pywin32/)
