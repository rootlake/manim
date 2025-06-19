from manimlib import *
import numpy as np

class TexturedSpinningEarth(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }

    def construct(self):
        # Set black background
        self.camera.background_color = BLACK
        
        # Create starry background
        stars = VGroup()
        for _ in range(200):
            star = Dot(radius=0.01)
            star.set_color(WHITE)
            # Random positions in 3D space around the scene
            x = np.random.uniform(-10, 10)
            y = np.random.uniform(-6, 6)
            z = np.random.uniform(-10, 10)
            star.move_to([x, y, z])
            star.set_opacity(np.random.uniform(0.3, 1.0))
            stars.add(star)
        
        # Add stars to scene
        self.add(stars)

        # Create sphere for Earth - centered at origin
        sphere = Sphere(radius=2, resolution=(30, 30))
        
        # Earth textures - using local files
        day_texture = "downloads/earth_day.jpg"
        night_texture = "downloads/earth_night.jpg"

        # Create textured surface
        earth = TexturedSurface(sphere, day_texture, night_texture)
        # Center the Earth at origin
        earth.move_to(ORIGIN)
        
        # Set camera perspective for a nice view
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=0 * DEGREES,    # No theta rotation
            phi=75 * DEGREES,     # Slight tilt to see the sphere nicely
        )

        # Add Earth to scene
        self.add(earth)
        
        # Start Earth spinning immediately (counterclockwise like real Earth)
        # Earth rotates about 15 degrees per hour, so for visual effect we'll speed it up
        earth.add_updater(lambda m, dt: m.rotate(-0.3 * dt, axis=UP))  # Negative for counterclockwise
        
        # Wait 3 seconds with just the spinning Earth
        self.wait(3)
        
        # Create and animate gridlines appearing
        mesh = SurfaceMesh(earth)
        mesh.set_stroke(BLUE_B, 1, opacity=0.6)
        
        self.play(
            ShowCreation(mesh, lag_ratio=0.01, run_time=2),
        )
        
        # Continue spinning with gridlines for remaining time
        mesh.add_updater(lambda m, dt: m.rotate(-0.3 * dt, axis=UP))  # Same rotation as Earth
        
        # Wait for total of 10 seconds (3 + 2 + 5 = 10)
        self.wait(5) 