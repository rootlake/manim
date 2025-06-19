# Manim Prompting Guide: Best Practices for Teachers

## 🎯 Overview

This guide teaches you how to effectively communicate with AI assistants (like Cursor) to create high-quality Manim animations. Follow these principles to get the best results every time.

## 📋 Core Prompting Principles

### ✅ **DO: Be Specific and Structured**
- Specify exact positions using coordinates: "Place the circle at (2, 1)"
- Use precise measurements: "Create a square with side length 3 units"
- Define exact timing: "Animate over 2.5 seconds with smooth easing"
- Specify colors by name: "Use BLUE_A with 60% opacity"

### ✅ **DO: Use Clear Animation Language**
- Reference specific Manim animations: "Use Create() for drawing, Transform() for morphing"
- Specify animation rates: "Use rate_func=smooth for natural motion"
- Define animation sequences: "First Create(), then Wait(1), then FadeOut()"

### ✅ **DO: Include Technical Details**
- Specify scene class names: "Create a class called 'MyScene' that inherits from Scene"
- Define file structure: "Put everything in the construct() method"
- Mention import statements: "Import all from manim"

### ✅ **DO: Provide Context and Purpose**
- Explain the educational goal: "This animation demonstrates the relationship between..."
- Specify the target audience: "Suitable for high school students learning..."
- Define the visual style: "Use a clean, professional style with consistent colors"

### ❌ **AVOID: Ambiguous Positioning**
- Don't say "next to" or "near" - use specific coordinates or relative positioning
- Don't say "somewhere on the screen" - specify exact placement
- Don't say "arrange them nicely" - define the arrangement pattern

### ❌ **AVOID: Vague Timing**
- Don't say "animate it" - specify the animation type and duration
- Don't say "show it for a while" - specify exact wait times
- Don't say "make it smooth" - specify the rate function

### ❌ **AVOID: Generic Visual Descriptions**
- Don't say "make it colorful" - specify exact colors and opacity
- Don't say "make it big" - specify exact sizes or scaling factors
- Don't say "style it nicely" - specify fonts, colors, and visual effects

## 🎨 Visual Elements: Specific Specifications

### Colors and Styling
```markdown
✅ "Use BLUE_A for the circle, RED_B for the square, with 70% opacity"
✅ "Apply a gradient fill from BLUE to GREEN using set_fill()"
✅ "Use WHITE text with BLACK stroke for maximum contrast"
✅ "Set stroke_width to 3 for bold outlines"
```

### Shapes and Objects
```markdown
✅ "Create a Circle(radius=2) centered at (0, 0)"
✅ "Draw a Square(side_length=3) positioned at (4, 2)"
✅ "Make a Triangle() pointing upward, scaled by 1.5"
✅ "Create a RegularPolygon(n=6) for a hexagon"
```

### Text and Equations
```markdown
✅ "Display MathTex('\\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}') in white"
✅ "Show Text('Hello World', font_size=48, color=BLUE)"
✅ "Write 'Area = πr²' using MathTex positioned at (0, 3)"
✅ "Use MarkupText('<b>Bold</b> and <i>italic</i>') for rich text"
```

### Positioning and Layout
```markdown
✅ "Position the circle at (0, 0), square at (3, 0), triangle at (6, 0)"
✅ "Use VGroup(circle, square, triangle).arrange(RIGHT, buff=1)"
✅ "Place text above the circle using .next_to(circle, UP, buff=0.5)"
✅ "Center everything using .move_to(ORIGIN)"
```

## ⏱️ Animation Types: Precise Specifications

### Basic Animations
```markdown
✅ "Use Create(circle, run_time=2, rate_func=smooth)"
✅ "Apply FadeIn(square, shift=UP*0.5, run_time=1.5)"
✅ "Use Write(text, run_time=3) for letter-by-letter writing"
✅ "Apply ScaleInPlace(triangle, scale_factor=2, run_time=2)"
✅ "Use Rotate(hexagon, angle=TAU, run_time=3, rate_func=linear)"
```

### Complex Animations
```markdown
✅ "Transform circle into square over 2 seconds using Transform()"
✅ "Move along path using MoveAlongPath(obj, path, run_time=4)"
✅ "Animate color change using set_color() with ValueTracker"
✅ "Slide in from left using FadeIn(obj, shift=LEFT*3)"
✅ "Bounce using rate_func=there_and_back with elastic easing"
```

### Timing and Sequencing
```markdown
✅ "Play animations sequentially: self.play(Create(circle)), self.wait(1), self.play(Create(square))"
✅ "Animate simultaneously: self.play(Create(circle), Create(square))"
✅ "Use self.wait(2) after animation completes"
✅ "Loop with self.play(Rotate(obj, TAU, run_time=2, rate_func=linear))"
```

## 📐 Mathematical Content: Precise Specifications

### Equations and Formulas
```markdown
✅ "Display MathTex('x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}', font_size=36)"
✅ "Show step-by-step: MathTex('ax^2 + bx + c = 0') → MathTex('x^2 + \\frac{b}{a}x = -\\frac{c}{a}')"
✅ "Highlight parts using SurroundingRectangle() with different colors"
✅ "Use Brace() to label equation parts with Text()"
```

### Graphs and Coordinate Systems
```markdown
✅ "Create Axes(x_range=[-5, 5, 1], y_range=[-3, 3, 1], x_length=8, y_length=6)"
✅ "Plot function using ParametricFunction(lambda t: [t, t**2, 0], t_range=[-3, 3])"
✅ "Mark points using Dot(point=[1, 1, 0], color=RED, radius=0.1)"
✅ "Add grid using Axes.get_grid() with opacity=0.3"
```

### Geometric Constructions
```markdown
✅ "Draw perpendicular bisector using Line(start, end).set_color(YELLOW)"
✅ "Create angle bisector using Arc(radius=1, angle=PI/4)"
✅ "Show construction steps: Create(line), Create(circle), Create(intersection)"
✅ "Use DashedLine() for construction lines, SolidLine() for final results"
```

## 🎬 Advanced Example Scripts

### Example 1: Complex Mathematical Visualization
```markdown
Create a Manim scene called "QuadraticFormula" that demonstrates the quadratic formula derivation:

1. Start with title "Deriving the Quadratic Formula" at (0, 4) using Text()
2. Show the standard form: MathTex('ax^2 + bx + c = 0') at (0, 2.5)
3. Transform it step by step:
   - Divide by a: MathTex('x^2 + \\frac{b}{a}x + \\frac{c}{a} = 0')
   - Move constant: MathTex('x^2 + \\frac{b}{a}x = -\\frac{c}{a}')
   - Complete the square: MathTex('x^2 + \\frac{b}{a}x + (\\frac{b}{2a})^2 = -\\frac{c}{a} + (\\frac{b}{2a})^2')
   - Factor: MathTex('(x + \\frac{b}{2a})^2 = \\frac{b^2-4ac}{4a^2}')
   - Final formula: MathTex('x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}')

4. Use Transform() for each step with 2-second run_time
5. Highlight the discriminant b²-4ac in RED using SurroundingRectangle()
6. Show a specific example: x² + 5x + 6 = 0 → x = -2 or x = -3
7. Use VGroup() to organize all equations and animate them as a unit

Use WHITE text on BLACK background, with BLUE for the final formula.
```

### Example 2: Interactive Physics Simulation
```markdown
Create a Manim scene called "ProjectileMotion" that shows projectile motion with real-time analysis:

1. Set up coordinate system: Axes(x_range=[0, 10, 1], y_range=[0, 5, 1], x_length=10, y_length=5)
2. Create projectile as Dot(radius=0.1, color=RED) starting at (0, 0)
3. Define trajectory function: y = -0.1x² + 2x (parabolic path)
4. Animate projectile motion:
   - Use ValueTracker(t) to track time from 0 to 4 seconds
   - Update position using: x = t, y = -0.1t² + 2t
   - Use always_redraw() to update projectile position
5. Draw trajectory path using ParametricFunction() with DASHED stroke
6. Show velocity vectors at t=0, t=1, t=2, t=3:
   - Use Arrow() with different colors for each time
   - Label with Text() showing velocity components
7. Display real-time equations:
   - Position: MathTex('x = v_0 t', 'y = v_0 t - \\frac{1}{2}gt^2')
   - Velocity: MathTex('v_x = v_0', 'v_y = v_0 - gt')
8. Mark key points: maximum height, landing point
9. Show energy conservation: kinetic + potential = constant

Use smooth animations with rate_func=smooth and 60 FPS rendering.
```

### Example 3: Geometric Proof Animation
```markdown
Create a Manim scene called "PythagoreanProof" that demonstrates the Pythagorean theorem visually:

1. Start with title "Pythagorean Theorem: a² + b² = c²" at (0, 4)
2. Create a right triangle with sides a=3, b=4, c=5:
   - Use Polygon() with vertices at (0,0), (3,0), (3,4)
   - Label sides with Text(): "a=3", "b=4", "c=5"
3. Show area calculations:
   - Create squares on each side using Square() with appropriate sizes
   - Fill with different colors: BLUE for a², RED for b², GREEN for c²
   - Show area labels: "a² = 9", "b² = 16", "c² = 25"
4. Demonstrate the relationship:
   - Use Transform() to move the smaller squares into the larger square
   - Show that a² + b² = 9 + 16 = 25 = c²
5. Add visual proof elements:
   - Use DashedLine() to show how squares fit together
   - Animate the transformation with 3-second duration
   - Use rate_func=smooth for natural motion
6. Display the final equation: MathTex('3^2 + 4^2 = 5^2') → MathTex('9 + 16 = 25')
7. Add a checkmark or confirmation when the proof is complete

Use consistent colors throughout and clear, readable fonts.
```

### Example 4: Advanced Mathematical Function Visualization
```markdown
Create a Manim scene called "FunctionTransformation" that shows how function transformations work:

1. Set up coordinate system: Axes(x_range=[-4, 4, 1], y_range=[-3, 3, 1], x_length=8, y_length=6)
2. Start with base function: f(x) = x² (parabola)
   - Plot using ParametricFunction() with BLUE color
   - Label with MathTex('f(x) = x^2')
3. Show transformations step by step:
   a) Vertical stretch: f(x) = 2x²
      - Plot in RED, use Transform() to show the change
      - Label with MathTex('f(x) = 2x^2')
   b) Horizontal shift: f(x) = 2(x-1)²
      - Plot in GREEN, show the shift with arrows
      - Label with MathTex('f(x) = 2(x-1)^2')
   c) Vertical shift: f(x) = 2(x-1)² + 1
      - Plot in YELLOW, show final transformation
      - Label with MathTex('f(x) = 2(x-1)^2 + 1')
4. Use ValueTracker() to animate the transformation smoothly
5. Show the transformation matrix or equation:
   - Display MathTex('y = a(x-h)^2 + k') with highlighted parameters
   - Use SurroundingRectangle() to highlight a, h, k values
6. Add interactive elements:
   - Use NumberPlane() for grid reference
   - Mark key points: vertex, y-intercept, x-intercepts
   - Show domain and range with Text() labels

Use smooth animations with 2-second durations and clear color coding.
```

## 🔧 Technical Specifications

### Scene Setup
```markdown
✅ "Use config.background_color = BLACK"
✅ "Set config.frame_rate = 60"
✅ "Use config.pixel_height = 1080, config.pixel_width = 1920"
✅ "Import all from manim: from manim import *"
```

### File Organization
```markdown
✅ "Create class MyScene(Scene): with def construct(self): method"
✅ "Use proper indentation and organize code in logical sections"
✅ "Add comments explaining complex animations"
✅ "Use descriptive variable names: circle, square, title_text"
```

### Export Settings
```markdown
✅ "Render with: manim scene.py MyScene -pql"
✅ "Use -pql for preview quality, -pqh for high quality"
✅ "Add --save_last_frame for static images"
✅ "Use -s for skipping animations, -n for specific scene number"
```

## 🚀 Quick Copy-Paste Templates

### Template 1: Mathematical Function Analysis
```markdown
Create a Manim scene that analyzes a mathematical function with:
- Coordinate axes from -5 to 5 with grid lines
- Function plot using ParametricFunction() with smooth curve
- Key points marked with Dot() and labeled with Text()
- Derivative function plotted in different color
- Area under curve highlighted with fill
- Function equation displayed using MathTex()
- Animate the plotting process with Create() over 3 seconds
- Use consistent colors: BLUE for function, RED for derivative, GREEN for area
```

### Template 2: Geometric Construction
```markdown
Create a Manim scene that demonstrates a geometric construction with:
- Starting elements (points, lines, circles) in WHITE
- Construction steps using DashedLine() in YELLOW
- Final result using SolidLine() in BLUE
- Step-by-step animation showing each construction step
- Labels for all important points and measurements
- Proof or explanation using MathTex() and Text()
- Use Transform() to show how construction elements relate
- Animate each step with 2-second duration and smooth easing
```

### Template 3: Physics Concept Visualization
```markdown
Create a Manim scene that visualizes a physics concept with:
- Physical objects represented by appropriate shapes (Circle, Rectangle, etc.)
- Motion vectors using Arrow() with different colors for different forces
- Time evolution using ValueTracker() and always_redraw()
- Energy diagrams or graphs using Axes() and ParametricFunction()
- Equations of motion displayed using MathTex()
- Key moments highlighted with special effects (flash, color change)
- Use realistic timing and scaling for physical accuracy
- Include both visual and mathematical representations
```

## ⚠️ Specific Things to Avoid

### ❌ **AVOID: Imprecise Positioning**
- Don't say "next to" - use specific coordinates or .next_to() with buff parameter
- Don't say "somewhere on the left" - use exact x,y coordinates
- Don't say "arrange them" - specify the arrangement method (VGroup.arrange())

### ❌ **AVOID: Vague Animation Commands**
- Don't say "animate it" - specify Create(), Transform(), FadeIn(), etc.
- Don't say "make it move" - specify the path, direction, and timing
- Don't say "show it" - specify Write(), Create(), or FadeIn()

### ❌ **AVOID: Generic Styling**
- Don't say "make it pretty" - specify colors, fonts, sizes, opacity
- Don't say "style it" - specify stroke_width, fill_opacity, color values
- Don't say "format it nicely" - specify exact formatting parameters

### ❌ **AVOID: Ambiguous Timing**
- Don't say "for a while" - specify exact run_time values
- Don't say "smoothly" - specify rate_func (smooth, linear, ease_in_out)
- Don't say "gradually" - specify the exact animation progression

## 🎯 Pro Tips

1. **Start with Coordinates**: Always specify exact positions using (x, y) coordinates
2. **Use Manim Objects**: Reference specific classes like Circle(), Square(), Text(), MathTex()
3. **Specify Animation Types**: Use Create(), Transform(), FadeIn(), Write() explicitly
4. **Define Timing**: Always include run_time and rate_func parameters
5. **Use Color Constants**: Reference Manim colors like BLUE, RED, GREEN, WHITE
6. **Group Related Elements**: Use VGroup() for organizing multiple objects
7. **Test Incrementally**: Build complex animations step by step
8. **Use ValueTracker**: For dynamic, time-based animations

## 📚 Subject-Specific Examples

### Mathematics
- "Create a scene showing the area of a circle formula with visual proof using AnnularSector()"
- "Animate the process of completing the square for quadratic equations using Transform()"
- "Show the relationship between sine and cosine functions using ParametricFunction() on unit circle"

### Physics
- "Demonstrate projectile motion with velocity vectors using Arrow() and trajectory using ParametricFunction()"
- "Show wave interference patterns using ParametricFunction() with two point sources"
- "Animate a simple pendulum with energy conservation using ValueTracker() and always_redraw()"

### Chemistry
- "Create a molecular structure using Sphere() for atoms and Line() for bonds"
- "Show a chemical reaction with before/after states using Transform()"
- "Animate electron orbitals using ParametricFunction() with 3D coordinates"

### Biology
- "Show cell division process using Circle() and Transform() for splitting"
- "Create a food chain using Arrow() and Text() for energy flow"
- "Animate photosynthesis using Circle() for molecules and Line() for reactions"

---

**Remember**: The more specific and technical your prompt, the better the resulting code. Always specify positions, colors, timing, and animation types explicitly! 