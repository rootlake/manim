#!/bin/bash

# Coloured output
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}================================${NC}"
echo -e "${BLUE}  Welcome to Manim First Time!  ${NC}"
echo -e "${BLUE}================================${NC}"
echo
echo -e "${GREEN}This script will set up everything you need for Manim automatically.${NC}"
echo -e "${GREEN}Just sit back and let it handle the installation!${NC}"
echo

# Function to check if a command exists
check_command() {
    if ! command -v "$1" &> /dev/null; then
        return 1
    fi
    return 0
}

# Function to install Homebrew on macOS
install_homebrew() {
    echo -e "${YELLOW}Installing Homebrew (macOS package manager)...${NC}"
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    # Add Homebrew to PATH for current session
    if [[ -f "/opt/homebrew/bin/brew" ]]; then
        export PATH="/opt/homebrew/bin:$PATH"
    elif [[ -f "/usr/local/bin/brew" ]]; then
        export PATH="/usr/local/bin:$PATH"
    fi
}

# Function to install Python
install_python() {
    echo -e "${YELLOW}Installing Python 3...${NC}"
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS - use Homebrew
        if ! check_command "brew"; then
            install_homebrew
        fi
        brew install python
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux - use package manager
        if check_command "apt"; then
            sudo apt update
            sudo apt install -y python3 python3-pip python3-venv
        elif check_command "yum"; then
            sudo yum install -y python3 python3-pip
        elif check_command "dnf"; then
            sudo dnf install -y python3 python3-pip
        else
            echo -e "${RED}Unsupported Linux distribution. Please install Python 3.8+ manually.${NC}"
            exit 1
        fi
    else
        echo -e "${RED}Unsupported operating system. Please install Python 3.8+ manually.${NC}"
        exit 1
    fi
}

# Function to install ffmpeg
install_ffmpeg() {
    echo -e "${YELLOW}Installing ffmpeg...${NC}"
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS - use Homebrew
        if ! check_command "brew"; then
            install_homebrew
        fi
        brew install ffmpeg
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux - use package manager
        if check_command "apt"; then
            sudo apt install -y ffmpeg
        elif check_command "yum"; then
            sudo yum install -y ffmpeg
        elif check_command "dnf"; then
            sudo dnf install -y ffmpeg
        else
            echo -e "${RED}Please install ffmpeg manually for your Linux distribution.${NC}"
            exit 1
        fi
    else
        echo -e "${RED}Please install ffmpeg manually for your operating system.${NC}"
        exit 1
    fi
}

# Safe deactivate function
safe_deactivate() {
    if [ -n "$VIRTUAL_ENV" ]; then
        echo -e "${YELLOW}Deactivating virtual environment...${NC}"
        deactivate
    fi
}

echo -e "${BLUE}Step 1: Checking and installing system requirements...${NC}"
echo

# Check and install Python
if ! check_command "python3"; then
    echo -e "${RED}❌ Python 3 not found. Installing...${NC}"
    install_python
else
    python_version=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    echo -e "${GREEN}✅ Python $python_version is available${NC}"
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
python_major=$(python3 -c 'import sys; print(sys.version_info.major)')
python_minor=$(python3 -c 'import sys; print(sys.version_info.minor)')

if [ "$python_major" -lt 3 ] || ([ "$python_major" -eq 3 ] && [ "$python_minor" -lt 8 ]); then
    echo -e "${RED}❌ Python version too old ($python_version). Need 3.8+. Installing...${NC}"
    install_python
fi

# Check and install pip
if ! check_command "pip3"; then
    echo -e "${RED}❌ pip3 not found. Installing...${NC}"
    if [[ "$OSTYPE" == "darwin"* ]]; then
        if ! check_command "brew"; then
            install_homebrew
        fi
        brew install python  # This includes pip3
    else
        install_python  # This includes pip3
    fi
else
    echo -e "${GREEN}✅ pip3 is available${NC}"
fi

# Check and install ffmpeg
if ! check_command "ffmpeg"; then
    echo -e "${RED}❌ ffmpeg not found. Installing...${NC}"
    install_ffmpeg
else
    echo -e "${GREEN}✅ ffmpeg is available${NC}"
fi

echo
echo -e "${GREEN}✅ All system requirements are ready!${NC}"
echo

# Create scenes directory if it doesn't exist
mkdir -p scenes

echo -e "${BLUE}Step 2: Setting up Manim (this will take 2-5 minutes)...${NC}"
echo

# Setup virtual environment
env_name="manim-firsttime-env"
if [ ! -d "$env_name" ]; then
    echo -e "${YELLOW}Creating virtual environment...${NC}"
    python3 -m venv "$env_name"
fi

echo -e "${YELLOW}Activating virtual environment...${NC}"
source "$env_name/bin/activate"

echo -e "${YELLOW}Upgrading pip...${NC}"
pip install --upgrade pip

echo -e "${YELLOW}Installing Manim (this may take a few minutes)...${NC}"
pip install manim

echo
echo -e "${GREEN}✅ Manim installation complete!${NC}"
echo

echo -e "${BLUE}Step 3: Creating your first animation...${NC}"
echo

# Create a very simple demo scene
scene_file="scenes/first_demo.py"
if [ ! -f "$scene_file" ]; then
    echo -e "${YELLOW}Creating your first animation scene...${NC}"
    
    cat > "$scene_file" << 'EOL'
from manim import *

class FirstDemo(Scene):
    def construct(self):
        # Create a simple circle
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        
        # Create some text
        text = Text("Hello Manim!", color=WHITE)
        text.next_to(circle, UP)
        
        # Create a square
        square = Square()
        square.set_fill(RED, opacity=0.5)
        square.next_to(circle, RIGHT)
        
        # Animate everything
        self.play(Create(circle))
        self.play(Write(text))
        self.play(Create(square))
        
        # Wait a moment to see the result
        self.wait(2)
        
        # Fade everything out
        self.play(FadeOut(VGroup(circle, text, square)))
        self.wait(1)
EOL
    echo -e "${GREEN}✅ Animation scene created!${NC}"
fi

echo -e "${BLUE}Step 4: Running your first animation...${NC}"
echo
echo -e "${YELLOW}This will open a preview window. Close it when you're done!${NC}"
echo

# Run the animation
manim scenes/first_demo.py FirstDemo -pql

echo
echo -e "${GREEN}🎉 Congratulations! You've created your first Manim animation!${NC}"
echo
echo -e "${BLUE}What's next?${NC}"
echo -e "${GREEN}• Your animation file is at: scenes/first_demo.py${NC}"
echo -e "${GREEN}• Edit this file to create your own animations${NC}"
echo -e "${GREEN}• Run it again with: manim scenes/first_demo.py FirstDemo -pql${NC}"
echo -e "${GREEN}• Check out the Manim documentation for more examples${NC}"
echo

# Cleanup
safe_deactivate

echo -e "${GREEN}Setup complete! Happy animating! 🎬${NC}" 