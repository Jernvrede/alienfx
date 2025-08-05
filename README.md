# How to get AlienFX working on Garuda 2025 (Arch)
(Desktop Alienware R4)
-> For lvl 1 n00bs <-

The outdated package alienfx 2.4.3-1 will work. It just needs some TLC.
It is unfortunately dependant on python-future. Python-future is no longer compatible
with Python 3.13.

## 1.  Installing:
        
    1.1     Using Octopi we can install all other dependancies:
            Install python, python-cairo, python-gobject, python-pyusb AND python-fissix

## 2.  "Fixing" python-future.
        We are modifying the AUR-package to suit our needs. In this lucky case we can
        redirect lib2to3 to fissix instead.

    2.1     Open Terminal (Fish)
    2.2     $ mkdir snuffaluffagus (for example)
    2.3     $ cd snuffaluffagus
    2.4     $ git clone https://aur.archlinux.org/python-future.git
    2.5     $ cd python-future
    2.6     $ nano PKGBUILD (or kate or other preffered editor)
    2.7     Insert (at bottom):
               prepare() {
                    cd "$srcdir"/future-$pkgver
                    find . -type f -name "*.*" -exec sed -i 's|lib2to3|fissix|g' {} +
                    }
    2.8     Save & Exit.
    2.9     $ makepkg -sri
    2.10    Close terminal

## 3.  Install AlienFX.
    Find it in Octopi and install.

## 4.  Setting a Theme.

    4.1     Open Terminal (Fish)
    4.2     $ sudo alienfx -z
    4.3     Allow the zonescan. Follow the instructions.
    4.4     $ sudo alienfx-gtk
    4.5     Nevermind the labels on the different "zones". Trial and error till you find a suitable setting.
            I will try to get to updating them. (Don´t forget to press Apply otherwise nothing will happen)
    4.6     When you´re satisfied save your theme. (Lets call it: Starchild)

## 5.  Making it stick through reboot.

    5.1     Open Terminal (Fish)
    5.2     $ sudo nano /usr/local/sbin/alienfx-go.sh (creating a bash script, it will be empty)
    5.3     Insert:             (#!-line MUST be the first line of the file)
                #!/bin/bash/
                alienfx -t Starchild
    5.4     Save & Exit.
    5.5     $ sudo chmod 0700 /usr/local/sbin/alienfx-go.sh
    5.6     $ sudo nano /etc/systemd/system/alienfx.service  (creating a systemd unit file, it will be empty)
    5.7     Insert:
                [Unit]
                Description=AlienFX Theme from Boot
                [Service]
                ExecStart=/usr/local/sbin/alienfx-go.sh
                [Install]
                WantedBy=multi-user.target
    5.8     Save & Exit.
    5.9     $ systemctl enable alienfx.service
    5.10    Reboot
