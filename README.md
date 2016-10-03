# Terminator Keyboard Shortcuts and Options



## Keybindings

|Description|Shortcut|
|------|------|
|Split terminals Horizontally.|Ctrl+Shift+O|
|Split terminals Vertically.|Ctrl+Shift+E|
|Move parent dragbar Right.|Ctrl+Shift+Right|
|Move parent dragbar Left.|Ctrl+Shift+Left|
|Move parent dragbar Up.|Ctrl+Shift+Up|
|Move parent dragbar Down.|Ctrl+Shift+Down|
|Hide/Show Scrollbar.|Ctrl+Shift+S|
|Search within terminal scrollback|Ctrl+Shift+F|
|Move to next terminal within the same tab, use Ctrl+PageDown to move to the next tab. If cycle_term_tab is False, cycle within thesame tab will be disabled|Ctrl+Shift+N or Ctrl+Tab|
|Move to previous terminal within the same tab, use Ctrl+PageUp to move to the previous tab. If cycle_term_tab is False, cycle withinthe same tab will be disabled|Ctrl+Shift+P or Ctrl+Shift+Tab|
|Move to the terminal above the current one.|Alt+Up|
|Move to the terminal below the current one.|Alt+Down|
|Move to the terminal left of the current one.|Alt+Left|
|Move to the terminal right of the current one.|Alt+Right|
|Copy selected text to clipboard|Ctrl+Shift+C|
|Paste clipboard text|Ctrl+Shift+V|
|Close the current terminal.|Ctrl+Shift+W|
|Quits Terminator|Ctrl+Shift+Q|
|Toggle between showing all terminals and only showing the current one (maximise).|Ctrl+Shift+X|
|Toggle between showing all terminals and only showing a scaled version of the current one (zoom).|Ctrl+Shift+Z|
|Open new tab|Ctrl+Shift+T|
|Move to next Tab|Ctrl+PageDown|
|Move to previous Tab|Ctrl+PageUp|
|Swap tab position with next Tab|Ctrl+Shift+PageDown|
|Swap tab position with previous Tab|Ctrl+Shift+PageUp|
|Increase font size. Note: this may require you to press shift, depending on your keyboard|Ctrl+Plus (+)|
|Decrease font size. Note: this may require you to press shift, depending on your keyboard|Ctrl+Minus (-)|
|Restore font size to original setting.|Ctrl+Zero (0)|
|Toggle fullscreen|F11|
|Reset terminal state|Ctrl+Shift+R|
|Reset terminal state and clear window|Ctrl+Shift+G|
|Group all terminals so that any input sent to one of them, goes to all of them.|Super+g|
|Remove grouping from all terminals.|Super+Shift+G|
|Group all terminals in the current tab so input sent to one of them, goes to all terminals in the current tab.|Super+t|
|Remove grouping from all terminals in the current tab.|Super+Shift+T|
|Open a new window (note: unlike in previous releases, this window is part of the same Terminator process)|Ctrl+Shift+I|
|Spawn a new Terminator process|Super+i|


## Options

|Description|Option|
|------|------|
|Show summary of options|-h, --help|
|Show the version of the Terminator installation|-v, --version|
|Start with a maximised window|-m, --maximise|
|Start with a fullscreen window|-f, --fullscreen|
|Instruct the window manager not to render borders/decoration on the Terminator window (this works well with -m)|-b, --borderless|
|Hide the Terminator window by default. Its visibility can be toggled with the hide_window keyboard shortcut (Ctrl-Shift-Alt-a by default)|-H, --hidden|
|Force the Terminator window to use a specific name rather than updating it dynamically based on the wishes of the child shell.|-T, --title|
|Specifies the preferred size and position of Terminator's window; see x(7).|--geometry=GEOMETRY|
|Runs the specified command instead of your default shell or profile specified command|-e, --command=COMMAND|
|Runs the rest of the command line instead of your default shell or profile specified command.|-x, --execute COMMAND [ARGS]|
|Set the terminal's working directory|--working-directory=DIR|
|Set a custom WM_WINDOW_ROLE property on the window|-r, --role=ROLE|
|Start Terminator with a specific layout. The argument here is the name of a saved layout.|-l, --layout=LAYOUT|
|Enable debugging output (please use this when reporting bugs). This can be specified twice to enable a built-in python debugging server.|-d, --debug|
|If this is specified as a comma separated list, debugging output will only be printed from the specified classes.|--debug-classes=DEBUG_CLASSES|
|If this is specified as a comma separated list, debugging outut will only be printed from the specified functions. If this is specified in addition to--debug-classes, only the intersection of the two lists will be displayed|--debug-methods=DEBUG_METHODS|
