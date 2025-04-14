import requests

# از کاربر آدرس وب‌سایت وردپرس را بپرسید
url = input("لطفاً آدرس وب‌سایت وردپرس را وارد کنید (به عنوان مثال: http://example.com/wp-content/): ")

# لیست فایل‌های مشکوک
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
        print(f'فایل پیدا شد: {url + file}')
    else:
        print(f'فایل پیدا نشد: {url + file}')