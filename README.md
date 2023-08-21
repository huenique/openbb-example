# OpenBB Example

Original example from [https://github.com/OpenBB-finance/examples](https://github.com/OpenBB-finance/examples)

## Platform-specific notes

Here is the underlying web engine each platform uses you might need to install.

### Linux

PyWry is required on linux.

Install PyWry

```sh
pip install pywry --upgrade
```

Pywry uses gtk-rs and its related libraries for window creation and Wry also needs WebKitGTK for WebView.

To activate interactive plots/tables in pywry window, please make sure the following packages are installed:

Arch Linux / Manjaro:

```sh
sudo pacman -S webkit2gtk
```

Debian / Ubuntu:

```sh
sudo apt install libwebkit2gtk-4.0-dev
```

Fedora / CentOS / AlmaLinux:

```sh
sudo dnf install gtk3-devel webkit2gtk3-devel
```
