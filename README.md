# How to get AlienFX working on Garuda 2025 (Arch)
(I´m focusing on making this work for my Alienware R4 Desktop)
-> For lvl 1 n00bs <-

(This is a bastardized way of using the original package.)<br>
The outdated package alienfx 2.4.3-1 will work. It just needs some TLC.<br>
It is unfortunately dependant on python-future. Python-future is no longer compatible
with Python 3.13.

1.  ## Installing:
        
    1.1     Using Octopi we can install all other dependancies:<br>
            Install python, python-cairo, python-gobject, python-pyusb AND python-fissix<br>

 2.  ## "Fixing" python-future.
        We are modifying the AUR-package to suit our needs. In this lucky case we can
        redirect lib2to3 to fissix instead.<br>
    2.1     Open Terminal (Fish)<br>
    2.2     ``$ mkdir snuffaluffagus`` (for example)<br>
    2.3     ``$ cd snuffaluffagus``<br>
    2.4     ``$ git clone https://aur.archlinux.org/python-future.git``<br>
    2.5     ``$ cd python-future``<br>
    2.6     ``$ nano PKGBUILD`` (or kate or other preffered editor)<br>
    2.7     Insert (at bottom):<br>
            ``   prepare() {``<br>
            ``       cd "$srcdir"/future-$pkgver``<br>
            ``        find . -type f -name "*.*" -exec sed -i 's|lib2to3|fissix|g' {} +``<br>
            ``        }``<br>
    2.8     Save & Exit.<br>
    2.9     ``$ makepkg -sri``<br>
    2.10    Close terminal<br>

 3.  ## Install AlienFX.
        Open Octopi and install.
    
 4.  ## Setting a Theme.
     4.1     Open Terminal (Fish)<br>
     4.2     ``$ sudo alienfx -z``<br>
     4.3     Allow the zonescan. Follow the instructions.<br>
     4.4     ``$ sudo alienfx-gtk``<br>
     4.5     Nevermind the labels on the different "zones". Trial and error till you find a suitable setting.<br>
                I will try to get to updating them. (Don´t forget to press Apply otherwise nothing will happen)<br>
     4.6     When you´re satisfied save your theme. (Lets call it: Starchild)<br>

 5.  ## Making it stick through reboot.
     5.1     Open Terminal (Fish)<br>
     5.2     ``$ sudo nano /usr/local/sbin/alienfx-go.sh`` (creating a bash script, it will be empty)<br>
     5.3     Insert:             (#!-line MUST be the first line of the file)<br>
                ``#!/bin/bash/``<br>
                ``alienfx -t Starchild``<br>
     5.4     Save & Exit.<br>
     5.5     ``$ sudo chmod 0700 /usr/local/sbin/alienfx-go.sh``<br>
     5.6     ``$ sudo nano /etc/systemd/system/alienfx.service``  (creating a systemd unit file, it will be empty)<br>
     5.7     Insert:<br>
                ``[Unit]``<br>
                ``Description=AlienFX Theme from Boot``<br>
                ``[Service]``<br>
                ``ExecStart=/usr/local/sbin/alienfx-go.sh``<br>
                ``[Install]``<br>
                ``WantedBy=multi-user.target``<br>
     5.8     Save & Exit.<br>
    5.9     ``$ systemctl enable alienfx.service``<br>
    5.10    Reboot<br>
