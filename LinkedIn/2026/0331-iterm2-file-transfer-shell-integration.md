# iTerm2 Shell Integration: Seamless File Transfers Between Local and
Remote

2026-03-31

## What is iTerm2 Shell Integration?

iTerm2 is a powerful terminal emulator for macOS that extends beyond
basic terminal functionality. Its shell integration feature creates a
bridge between your local machine and remote servers, enabling seamless
file transfers with simple keyboard shortcuts—no need for `scp` commands
or separate SFTP clients.

## Installing Shell Integration

Installing shell integration is straightforward:

1.  **On your local machine**: Login into remote server using SSH in an
    iTerm2 session, then follow the menu iTerm2 → Install Shell
    Integration

2.  **Critical step for file transfers**: Set the `iterm2_hostname`
    environment variable on the remote server:

``` bash
# Add to ~/.bashrc or ~/.zshrc on remote server
export iterm2_hostname=your-server-hostname
# you can find the hostname by running `hostname` command on the remote server. If that name doesn't work, try using the IP address instead, which can be found with `hostname -i` command.
```

Without `iterm2_hostname` set, iTerm2 cannot determine where files
should be transferred to/from, and the upload/download features will not
work.

## Downloading Files from Remote Server

Once setup, downloading is as simple as a click:

- **Right-click on any filename** in your terminal output (e.g., from
  `ls` command results) and select “Download with scp”
- Alternatively, click on the filename while holding the Cmd key to
  trigger the download
- Works with any file path visible in your terminal—no need to type
  `scp` commands

## Uploading Files to Remote Server

Two easy methods to upload files from your Mac to the remote server:

- **Option+drag-drop**: Hold Option key and drag files from Finder
  directly into iTerm2—they upload via scp automatically
- Files transfer to your current working directory on the remote server
- No need to construct `scp` commands manually

## Why This Matters

Shell integration transforms file management in SSH sessions from a
multi-step command process to single keystrokes, saving my time. I hope
that this help s you streamline your workflow as well!
