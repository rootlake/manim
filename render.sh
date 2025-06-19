#!/bin/bash

# Simple script to render manim scenes to video with progress indicators
# Usage: ./render.sh scenes/scene_file.py SceneName

if [ $# -eq 0 ]; then
    echo "Usage: $0 <scene_file.py> <SceneName>"
    echo "Example: $0 scenes/earth_scene.py SpinningEarth"
    exit 1
fi

echo "Starting render of $2 from $1..."
echo "This may take a while for textured scenes..."

# Activate the virtual environment
source manim-gl-env/bin/activate

# Run manimgl with write flag and progress indicators
manimgl "$1" "$2" -w --show_animation_progress --leave_progress_bars --prerun

echo "✅ Video saved to videos/ directory" 