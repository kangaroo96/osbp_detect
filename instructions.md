# Instructions for MacOS

## A. Installation

### 0. Open Terminal (Launchpad -> Terminal)

### 1. Install HomeBrew
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### 2. Install Python3
```
brew install python3
```

### 3. Clone GitHub Repo
```
cd ~/Documents/
git clone https://github.com/kangaroo96/osbp_detect.git
```

### 4. Install Dependencies and Run
```
cd ~/Documents/osbp_detect/
pip3 install -r requirements.txt 
```

## B. Run Software
```
python3 ~/Documents/osbp_detect/gui.py
```
