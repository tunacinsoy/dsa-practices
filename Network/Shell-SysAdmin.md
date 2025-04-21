```bash
# Check the ownership of a folder or a file.
ls -l <folder_path>
```
---
```bash
grep -rl '<text_that_needs_to_be_replaced>' . | xargs sed -i -e \ 's/<text_that_needs_to_be_replaced/<text_to_replace>/g'
```
If we do not know which files contain replacement text -> `grep` searches all of the files for the text, and it does it recursively (`-r`), and outputs only the names of the files that contain the searched text `(-l)`; then `xargs` is used to execute a command from cli; `sed` is used for stream editing, and `-i` flag edits file in place so that they will be updated; and `-e` flag is used to specify the command to be executed. `s/<text_that_needs_to_be_replaced/<text_to_replace>/g'` `s` for substitute. and `g` for replacing all occurrences in each line, not the first line.

```
sed -i 's/<text_to_be_replaced>/<new_text>/g' <file_name>
```
If we know which file contain replacement text -> Replace a text within a given file name

``` 
find ./ -type f -exec sed -i -e \
's/<your_dockerhub_user>/<your actual docker hub user>/g' {} \;
```
find all files (`-type f`) within the current directory, and for each of them, execute (`-exec`) stream editor (`sed`) command. Within this command, modify files in place (`-i`), and execute the following option after `-e`; `s` stands for substitute, followed by the text to be substituted, and then the substitution text, followed by `g`(all occurrences in each file will be replaced), then `{}` will be filled with the file names that will be found by `find` (so, it will be like `sed -i -e 's/<your_dockerhub_user>/mydockeruser/g' ./file1.txt`).

```
xdg-open <file_name>
```
open a picture/image.

```
sudo chown newowner:newgroup filename
```
Change ownership of a file.

```
find . -name <file_name "outputs.tf">
```
find the location of a specific file conveniently.

```
mkdir -p /home/user/projects/my_project
```
If `/home/user/projects` does not already exist, the `-p` flag will ensure that `mkdir` creates both `/home/user/projects` and `/home/user/projects/my_project` directories. If any of these directories already exist, they will be left unchanged, and the command will proceed without error.

```bash
# Return IPv4 records
dig +short A <domain_name google.com>

# Return IPv6 records
dig +short AAAA <domain_name google.com>
```
Return the IP address of a website.

```bash
grep -ir "image:" ./manifests/blog-app |\ awk {'print $3'} | sort -t: -u -k1,1 > ./images
```
This command searches through the `./manifests/blog-app` directory for lines containing "image:", extracts the third field from these lines (which is assumed to be the image name or tag), sorts them uniquely by the part before the colon (`:`), and saves the result to the `./images` file.

---
```bash
# ssh into one of the machines hosted on any platform that has external ip address.
ssh -p 22 <user_name tuna>@<external_ip_address 4.185.25.147>
```
---
```bash
# Check who has sudo privileges 
sudo -v 
```
---
```shortcut
# Opens up history of commands, and they can be copied for later use
Ctrl + Shift + R
```
---
> The notation `git(1)` refers to the section of the Unix or Linux manual where you can find information about the `git` command. In this case, the number `1` indicates that `git` is a **user command** found in section 1 of the manual.
> 
> - `1`: Executable programs or shell commands
> - `2`: System calls (functions provided by the kernel)
> - `3`: Library calls (functions within program libraries)
> - `4`: Special files (usually found in `/dev`)
> - `5`: File formats and conventions
> - `6`: Games and screensavers
> - `7`: Miscellaneous
> - `8`: System administration commands
> 
> To view the `git(1)` manual, you can run `man 1 git` in your terminal.

> Note that port numbers 0–1023 are restricted and can only be used by the
> root user, so it is better to avoid choosing one of those and pick something else, if it
> is not already in use by a different process. For instance, port number 8001 is usually free and is frequently used for local HTTP servers.

> Usually, most system log files of a UNIX system can be found under the
> `/var/log` directory.

---
```bash
# The `journalctl -xe` command is used to view system logs in real time on Linux systems that use `systemd` as their init system. 
# -x for extra details, -e for jump to end of the file, where recent logs occurred.
journactl -xe
```
---
```bash
# Search keyword within a directory
# search recursively (`-r`)
# Show line numbers (`-n`) and file names (`-w`).
grep -rnw '.' -e 'stderr' | fzf
```
---
```shortcut
Compose Key(alt gr) + e + = # prints €
```

> By default, all UNIX systems support three special and standard filenames: /dev/stdin, /dev/stdout, and /dev/stderr, which can also be accessed using the file descriptors 0, 1, and 2, respectively. These three file descriptors are also called standard input, standard output, and standard error, respectively.
> 
> For instance, when we type `cat 1.txt`,  the argument that `cat` takes is the stdin, and then `cat` writes the content of it to its `stdout`.
> 
> Or, if I type `cat non_existent_file 2> errors.txt` , this would write the `no such file or directory` error message to errors.txt file, since we redirect its stderr output to that file.
> 
> When we use `ls > 1.txt` we are actually redirecting `ls` stdout to 1.txt file.  Or when we use pipes such as:
> 
> `ls -a | grep 'Desktop'`  We are actually passing the stdout of `ls -a` as a stdin for `grep` command.

> There are three process categories: user processes, daemon processes, and kernel processes. User processes run in user space and usually have no special access rights. Daemon processes are programs that can be found in the user space and run in the background without the need for a terminal. Kernel processes are executed in kernel space only and can fully access all kernel data structures.

```bash
# view kernel processes, daemon processes, and user-space processes
# for cheat sheet: https://gist.github.com/ericandrewlewis/4983670c508b2f6b181703df43438c37
top
```
---
```bash
# Count the lines of the output that is generated by the first command
ls | wc -l
```
---
```bash
# shows the details of all network interfaces (show ip address)
ifconfig
```
---
```bash
# Show all listening TCP and UDP connections
netstat -tuln

# Alternatively, use
ss -tuln
```
---
```bash
# See all exported variables and grep the one that is searched, and forward the stdout to 1.txt file
export -p | grep 'ARGO' > 1.txt

# Alternatively,
printenv
```

> In a big endian representation, bytes are read from left to right, while little endian reads bytes from right to left. For the 0x01234567 value, which requires 4 bytes for storing, the big endian representation is 01 | 23 | 45 | 67; 
> whereas the little endian representation is 67 | 45 | 23 | 01.

```bash
# Check system architecture and os details
uname -a
```

```bash
# Create a symlink (a pointer to a file that is located somewhere else, that is defined in target parameter)
ln -s [TARGET] [SYMLINK_NAME]

# for instance:
ln -s /home/user/docs /home/user/link_to_docs
```
``
```bash
# see the last 20 lines
tail-n 20 filename.txt

# continuously monitor the lines added to filename.txt, useful for displaying new logs
tail -f filename.txt
```
---
```bash
# Check how many directories there are in the current folder
find . -mindepth 1 -maxdepth 1 -type d | wc -l
```
---
```shell
# Normally, # is the comment character, however, when it is followed by !
# it becomes a `shebang` line, which is recognizd by the OS as a directive to the interpreter that will be used to execute the script.
#!/bin/sh
```