# 🎬 Manim for Math Teachers

Interactive animation guide and turnkey solutions for creating mathematical visualizations using Manim.

## 🚀 Overview

This project provides comprehensive tools and documentation for math teachers to create engaging educational animations using Manim. Whether you're new to programming or an experienced educator, our turnkey solutions make it easy to bring mathematical concepts to life.

## ✨ Features

- **📖 Comprehensive Prompting Guide**: Master AI-assisted animation creation
- **⚙️ Automated Setup Scripts**: One-click installation and configuration
- **🎨 Example Scenes**: Ready-to-use animations for various math topics
- **📚 Best Practices**: Proven techniques for effective educational content
- **🎥 Video Examples**: Sample animations demonstrating key concepts

## 🎯 Perfect For

- Visualizing mathematical concepts
- Creating step-by-step proofs
- Demonstrating geometric transformations
- Showing real-time mathematical simulations
- Classroom presentations and lectures

## 🛠️ Quick Start

### Prerequisites
- Python 3.8+
- Git
- Basic command line knowledge

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rootlake/manim.git
   cd manim
   ```

2. **Run first-time setup**
   ```bash
   ./manim-FirstTime.sh
   ```

3. **Explore example scenes**
   ```bash
   ls scenes/
   ```

4. **Render your first animation**
   ```bash
   ./render.sh
   ```

## 📁 Project Structure

```
manim/
├── index.html                 # GitHub Pages main page
├── README.md                  # This file
├── manim-prompting-guide.md   # Comprehensive AI prompting guide
├── manim-FirstTime.sh         # First-time setup script
├── manim-Turnkey-Options.sh   # Advanced configuration options
├── render.sh                  # Animation rendering script
├── custom_config.yml          # Manim configuration
├── scenes/                    # Animation scene files
│   ├── demo_gl.py
│   ├── earth_scene.py
│   ├── enhanced_earth.py
│   └── textured_earth.py
├── videos/                    # Rendered animation outputs
│   ├── SimpleDemo.mp4
│   ├── SpinningEarth.mp4
│   └── TexturedSpinningEarth.mp4
├── downloads/                 # Assets and resources
└── manim-gl-src/             # Manim source code
```

## 🎬 Example Animations

### Simple Demo
Basic animation demonstrating fundamental Manim concepts.

### Spinning Earth
3D visualization of Earth rotation with realistic textures.

### Textured Earth
Enhanced Earth model with day/night cycle visualization.

## 📚 Documentation

### [Manim Prompting Guide](manim-prompting-guide.md)
Master the art of communicating with AI to create perfect Manim animations. Learn specific techniques for:
- Precise positioning and timing
- Visual effects and styling
- Mathematical content presentation
- Animation sequencing and flow

### Setup Scripts
- **`manim-FirstTime.sh`**: Complete first-time setup
- **`manim-Turnkey-Options.sh`**: Advanced configuration options
- **`render.sh`**: Quick animation rendering

## 🔧 Configuration

### Custom Configuration
Edit `custom_config.yml` to customize:
- Video quality and format
- Frame rate and resolution
- Output directory settings
- Rendering preferences

### Environment Setup
The setup scripts handle:
- Python environment creation
- Manim installation
- Dependencies management
- System-specific configurations

## 🎨 Creating Your Own Animations

1. **Study the examples** in the `scenes/` directory
2. **Read the prompting guide** for best practices
3. **Modify existing scenes** to fit your needs
4. **Use AI assistance** with the techniques from the guide
5. **Render and test** your animations

## 🚀 Advanced Usage

### Custom Scenes
Create new animation files in the `scenes/` directory:

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # Your animation code here
        circle = Circle()
        self.play(Create(circle))
        self.wait(2)
```

### Rendering Options
```bash
# Render specific scene
python -m manim scenes/my_scene.py MyScene

# High quality render
python -m manim scenes/my_scene.py MyScene -qh

# Preview mode
python -m manim scenes/my_scene.py MyScene -p
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Manim Community](https://github.com/ManimCommunity/manim) for the amazing animation library
- Math teachers worldwide for inspiration and feedback
- The open-source community for continuous improvements

## 📞 Support

If you encounter any issues or have questions:
1. Check the [prompting guide](manim-prompting-guide.md)
2. Review the example scenes
3. Open an issue on GitHub

---

**Made with ❤️ for math educators everywhere**

*Empowering teachers to create engaging mathematical visualizations* 