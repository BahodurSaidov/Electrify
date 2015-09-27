Web2Executable
==============

What is it?
-----------

Web2Executable is a friendly command line and GUI application that can transform your Nodejs (or any other JS/HTML) app into an standalone executable. It can export to Mac OS X, Windows and Linux all from one platform, so no need to go out and buy expensive hardware.

It's powered by the very awesome project [NWJS](https://github.com/nwjs) and PySide, is open source, and is just dang awesome and easy to use.

If you have an idea for a feature, please create a new issue with a format like this: "Feature - My Awesome New Feature", along with a good description of what you'd like the feature to do.

If you got some value out of using my app, consider donating a dollar to keep me caffeinated :) 

<a href='https://pledgie.com/campaigns/26899'><img alt='Click here to lend your support to: Web2Executable Donations and make a donation at pledgie.com !' src='https://pledgie.com/campaigns/26899.png?skin_name=chrome' border='0' ></a>

On the other hand, if you have any annoyances with the application and want to contribute to making it better for everyone, please file an issue with "Annoyance:" as the first part of the title. Sometimes it's hard to know what is annoying for people and input is much appreciated :)

Downloads
---------

###CMD

[Windows 7+ Download](http://www.mediafire.com/download/r9rawa9qorlfa79/Web2ExeWin-CMD.zip)

[Mac OS X 10.6+ download](http://www.mediafire.com/download/esyz3z3ij0qrt64/Web2ExeMac-CMD.zip)

[Ubuntu 14.04 download](http://www.mediafire.com/download/vet95whim6g8x55/Web2ExeLinux-CMD.zip)

###GUI

####Mac OS X

[Mac OS X 10.7+ download - v0.2.4b](http://www.mediafire.com/download/vv1g29x5l324sge/Web2ExeMac-v0.2.4b.zip)

[Mac OS X 10.7+ download - v0.2.3b](http://www.mediafire.com/download/xq55xg0xnxrl0a9/Web2ExeMac-v0.2.3b.zip)

[Mac OS X 10.7+ download - v0.2.2b](http://www.mediafire.com/download/skxz77undtxvp5o/Web2ExeMac-v0.2.2b.zip)


You can just put the app where ever you want and double click to run it.

####Windows

[Windows 7+ installer download - v0.2.6b](http://www.mediafire.com/download/7en3z4dcv3ssrdz/Web2Exe-Setup.zip)

[Windows 7+ download - v0.2.6b](http://www.mediafire.com/download/un39rt9ddq8jvol/Web2ExeWin-v0.2.6b.zip)

[Windows 7+ download - v0.2.5b](http://www.mediafire.com/download/6nmp09ruxy62l72/Web2ExeWin-v0.2.5b-url.zip)

[Windows 7+ download - v0.2.4b](http://www.mediafire.com/download/oe2fdtaadw13ar8/Web2ExeWin-v0.2.4b.zip)



Double click the Web2Exe.exe file inside the extracted folder.

####Linux

[Ubuntu 14.04 - v0.2.6b](http://www.mediafire.com/download/1rv5ubl6v68sgvx/Web2ExeLinux-v0.2.6b.zip)

[Ubuntu 14.04 - v0.2.5b](http://www.mediafire.com/download/seuu5bnwhc8dbd4/Web2ExeLinux-v0.2.5b.zip)

[Ubuntu 14.04 - v0.2.3b](http://www.mediafire.com/download/74t8hhsf3mo00je/Web2ExeLinux-v0.2.3b.zip)


Give the executable permissions to execute and then run it:

```
chmod +x web2exe
./web2exe
```

It's probably better for linux users to install the requirements and run the python script as instructed below.


Getting Started
---------------

###Using Prebuilt Binaries

When using the prebuilt binaries for Windows, Mac, or Ubuntu, there are NO dependencies or extra applications needed. Simply download Web2Exe for the platform of your choice, extract, and double click the app/exe/binary to start. This applies to both the command-line version and the GUI version.

**NOTE!**: Some people report needing the Microsoft Visual C++ 2008/2010 SP1 and regular Redistributable package. I don't have a machine to test this, but just know that you might need the package if the application won't open or spits out the following error:

```
Error: The application has failed to start because the side by side configuration is incorrect please see the application event log or use the command line sxstrace.exe tool for more detail.
```


### Run from Python Source

Requires the pyside library and python 2.X. If you want to replace the icon in the Windows Exe's, this will do it automatically with the latest code if you have PIL or Pillow installed. I've only tested the code on python 2.7.3-2.7.9, so I can't speak about any lower version, but it should work as long as PySide is supported.

####GUI

Install dependencies **PIL or Pillow** for icon and icns exporting.

Initiate submodules:

```
git submodule update --init --recursive
```

Run with:

```
python main.py
```

It's a pretty simple app. Just point it the the directory that your web application lives, customize the options (the two marked with a star are the only ones required) and then choose your export options. The app will export under YOUR_OUTPUT_DIR/YOUR_APP_NAME. 

####Command line interface

Dependencies: configobj (install with pip) and Pillow if you want icon replacement (not necessary)

Run the command_line.py with the --help option to see a list of export options. Optionally, if you don't want to install python, there are builds for Mac and Windows in the command_line_builds folder of this repository.

Example usage (if using the prebuilt binary, replace `python command_line.py` with the exe name):

```
python command_line.py /var/www/html/CargoBlaster/ --main html/index.html --export-to linux-x64 windows mac --width 900 --height 700 --nw-version 0.10.5
```

###GUI Instructions

To use Web2Exe:
  1. Choose a project folder with at least one html or php file. The name of the export application will be autogenerated from the folder that you choose, so change it if you so desire.
  2. Modify the options as needed.
  3. Choose at least one export platform and then the Export button should enable (as long as the field names marked with a star are filled out and all files in the fields exist).
  4. Click the export button and once it's done, click the "Open Export Folder" button to go to the folder where your exported project will be.

Features
--------

- Cross platform to Mac, Windows, Linux
- Working media out of the box (sound and video)
- Easy to use and straightforward
- Streamlined workflow from project -> working standalone exe
- Same performance as Google Chrome
- Works with Phaser; should work with other HTML5 game libraries
- Export web applications to all platforms from your current OS
- Ability to specify a node-webkit version to download
- Automatic insertion of icon files into Windows exe's or Mac Apps by filling out the icon fields as necessary
- A command line utility with functionality equivalent to the GUI. Useful for automated builds.
- Compression of executables with upx

Planned New Features
--------------------

- The ability to add external files to the project
- Minifying JS and HTML


FAQ
---

### Web2Executable says the export is completed, but there's nothing in the output folder.

This is an issue with the app's error reporting. It will sometimes fail silently and I'm currently working to address the issue. However, from issues filed about this problem, it's likely you have some node_modules that were inproperly removed. Be sure to remove node modules installed with npm using `npm uninstall <package-name>`.

### The export button is greyed out, what do I do?

There are a couple things you can do. The first is to make sure all starred fields are filled out. The second is to make sure all of the files in the filled out fields actually exist. The third is to check out the error.log file located in the same directory as the Web2Exe executable for Windows and Linux, and for Mac, in the Web2Exe.app/Contents/Resources/ folder.

### How do I include external files?

You must provide support for this yourself using javascript and nodejs. You can get the path of the current executable with `path.dirname( process.execPath );` and then load files relative to that path. 

### When exporting to Linux, I get an error about libudev.so.0

This is an known issue with nw.js/node-webkit. See [here](https://github.com/nwjs/nw.js/wiki/The-solution-of-lacking-libudev.so.0) for information on how to work around this issue.

### How do I use option X?

All of the options for node-webkit are documented in node-webkit's manifest file specification. It is located [here](https://github.com/rogerwang/node-webkit/wiki/Manifest-format).

### What is the downloads folder for and where should I keep it?

The downloads folder is where Web2Exe stores the node-webkit versions in zip or tar format. This location should be chosen as a central location, because Web2Exe will reuse the files to create executables every time the export button is pressed. It will also save time by not having to redownload the node-webkit files over and over.

The Web2Executable/files/downloads folder is a good place to keep your downloads or any place that **isn't your project's directory**.

### Where is the default downloads location and how can I change it back?

For right now, the default location is in Web2Executable/files/downloads (Web2Executable.app/Contents/MacOS/files/downloads for Mac OSX).

This location is stored on a by project basis, so it will load what you have set for a particular project from the package.json file. Right now, the only way to change it back to the default is to open the package.json file with a text editor and remove the download_dir option from it.

### How do I use the icon replacement?

The icon replacement works by filling out the fields "Window Icon", "Exe Icon", or "Mac Icon". If "Window Icon" is filled out and the others aren't, Web2Exe will automatically use this field instead of "Exe Icon" or "Mac Icon" depending on if you export to Mac or Windows.

If you fill "Exe Icon" out, this will be used to replace the icon inside the node-webkit exe from the default compass icon if you export to Windows. Only pngs and jpegs are supported right now.

If you fill out "Mac Icon", this will convert the icon from png or jpeg to icns and copy it into the Mac app folder (or just copy if the icon is already in icns format). Of course, this is only when exporting to Mac.

### Why don't you replace icons for Linux?

Linux executables don't use icons, so there's nothing to replace. If you want to set an icon for when the app is running for Linux, simply fill out the "Window Icon" field.

What's New?
----------------------

v0.2.6b
- Fixed issue with not treating trust anchors as a list

v0.2.5b (Windows Only)
- Hopefully fixed windows 10 issues
- Added ability to specify a url to resources

v0.2.4b
- Added persistent user data so that the installer works properly for Windows

v0.2.3b
- Unicode Support!
- Fixed a bug that was causing certian builds to bring up the nwjs default window
- Fixed a bug with OS X menus not updating previous projects
- .desktop file generation for linux builds

v0.2.2b
- Fixed a few bugs with image loading
- Added icns viewing support when adding OS X icons.

v0.2.1b
- UPX Compression to executables
- UI rework for future additions
- Open project moved to file menu
- Output folder moved to export options
- Recent files can be viewed in the file menu

v0.2.0b
- Kiosk mode + emulation
- Project name separate from manifest name
- Better error detection (per field)
- Info.plist is updated to reflect app name and version
- Bug fixes!

v0.1.17b
- Support for nwjs 0.12.0!! 

v0.1.16b
- Fixed an issue with copying files on windows

v0.1.15b
- Fixed some issues with copying external files

v0.1.12b
- Added new options that were requested and made the window wider to accommodate.

v0.1.11b
- fixed a bug that overwrote the index.html path if it was not in the root directory

v0.1.10b
- added the ability to specify an icon for both mac and windows export applications

v0.1.9b
- made UI more compact for small screens
- fixed Mac issue with not loading! Yay!

v0.1.8b
- added an "Open to export folder" button that makes things a little easier to navigate to.
- attempted to fix Mac OS X issues with crashing

v0.1.7b
- added better download management so there is no redownloading things. Also a bunch of bugs were fixed up.

v0.1.6b

- added the ability to get newer NodeWebkit versions automatically from the changelog of node-webkit. Also fixed compatibility with 0.10.X.

v0.1.4b

- fixed an issue where index.html would be found with absolute path, which would cause a "require not found" error

v0.1.3b

- Added the ability to choose node-webkit versions if 0.9.2 is not what you want*
- Modified the UI slightly for people with smaller monitors
- Added a force-download option to overwrite files

*Note: If you have already downloaded, say, 0.9.2 of webkit, then you select 0.8.5, you will have to select "Force download" in order to update the files properly. I'm not sure how to reliably/efficiently detect and store multiple versions of the node-webkit files.

v0.1.2b

- Fixed an issue with icon copying
- Fixed a bug that overwrote existing package.json files.



Screenshots
-----------

v0.2.1b Linux
![ScreenshotLinux](http://i.imgur.com/ImFtEMi.png)

v0.1.13b Mac OS X

![ScreenshotMac2](http://i.imgur.com/JgKfYIm.png)

v0.1.9b Mac OS X

![ScreenshotMac](http://i.imgur.com/Kdd6DcC.png)


License
-------

The MIT License (MIT)

Copyright (c) 2015 SimplyPixelated

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
