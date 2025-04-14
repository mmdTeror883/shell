import requests


url = input("plese link site : http://example.com/wp-content/): ")

suspicious_files = [
    'wp-config.php',
    'insert.php',
    'shell.php',
    'eval.php','insert.php',
'shell.php',
'eval.php',
'cmd.php',
'test.php',
'fetch.php',
'upload.php',
'notify.php',
'system.php',
'reverse.php',
'readme.php',
'wp-load.php',
'shell_exec.php',
'backdoor.php',
'find.php',
'copy.php',
'ping.php',
'config.php',
'malware.php',
'secure.php',
'sql.php',
'scan.php',
'get.php',
'admin.php',
'script.php',
'hack.php',
'check.php',
'debug.php',
'info.php',
'log.php',
'data.php',
'auth.php',
'run.php',
'hidden.php',
'install.php',
'module.php',
'execute.php',
'keylogger.php',
'catch.php',
'mod.php',
'remote.php',
'zip.php',
'temp.php',
'uploadify.php',
'cron.php',
'phpshell.php',
'command.php',
'ajax.php',
]

for file in suspicious_files:
    response = requests.get(url + file)
    if response.status_code == 200:
        print(f'scan The file was found ok: {url + file}')
    else:
        print(f'File not found: {url + file}')
