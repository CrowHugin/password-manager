## how to set up:

download the module inside the [release](https://github.com/CrowHugin/password-manager/releases/) page

Use:
```bash
curl -L -o password_manager https://raw.githubusercontent.com/CrowHugin/password-manager/main/dist/main
```

Then give it the permission to run with:
```bash
chmod u+x ~/password_manager
```

you can find the stored passwords within: 
`~/password_manager/index.json`

---
## How to use it:

***There are three options you can use to use:***

`-a` or `--add` to add an email, a password and a website into the storage file  
`-v` or `--view` to view any required info  
`-c` or `--create` to create a password (must be less than 21 character long)

***These three options can / must be use with:***

`-em` or `--email` to put an email within the options `-a` and `-v`  
`-p` or `--password` to put a password within the options `-a` and `-v`  
`-w` or `--website` to put a website within the options `-a` and `-v`

***Do not use:***

`-drun` or `--dry_run` is only used for test.
This option will create a folder named `pass` inside the folder you launch the script. 

---

Please remind  I'm still learning and this project isn't one to take too seriously.

I'm doing it because it's fun :)

