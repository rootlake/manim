from manimlib import *
import numpy as np

class EnhancedSpinningEarth(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }

    def construct(self):
        # Set black background
        self.camera.background_color = BLACK
        
        # Create realistic starry background
        # TODO: Replace with constellation graphics later
        stars = VGroup()
        
        # Create different sizes of stars for realism
        for _ in range(150):
            # Main stars
            star = Dot(radius=np.random.uniform(0.005, 0.02))
            star.set_color(WHITE)
            # Distribute stars in a sphere around the scene
            phi = np.random.uniform(0, 2 * np.pi)
            theta = np.random.uniform(0, np.pi)
            r = np.random.uniform(8, 15)
            x = r * np.sin(theta) * np.cos(phi)
            y = r * np.sin(theta) * np.sin(phi)
            z = r * np.cos(theta)
            star.move_to([x, y, z])
            star.set_opacity(np.random.uniform(0.4, 1.0))
            stars.add(star)
        
        # Add some brighter "major" stars
        for _ in range(20):
            bright_star = Dot(radius=np.random.uniform(0.02, 0.04))
            bright_star.set_color(WHITE)
            phi = np.random.uniform(0, 2 * np.pi)
            theta = np.random.uniform(0, np.pi)
            r = np.random.uniform(10, 15)
            x = r * np.sin(theta) * np.cos(phi)
            y = r * np.sin(theta) * np.sin(phi)
            z = r * np.cos(theta)
            bright_star.move_to([x, y, z])
            bright_star.set_opacity(1.0)
            stars.add(bright_star)
        
        # Add stars to scene
        self.add(stars)

        # Create sphere for Earth - perfectly centered
        sphere = Sphere(radius=2.5, resolution=(40, 40))  # Higher resolution for smoother texture
        
        # Earth textures - using local files
        day_texture = "downloads/earth_day.jpg"
        night_texture = "downloads/earth_night.jpg"

        # Create textured surface
        earth = TexturedSurface(sphere, day_texture, night_texture)
        earth.move_to(ORIGIN)
        
        # Set camera perspective for optimal Earth viewing
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=0 * DEGREES,    # No orbital rotation
            phi=70 * DEGREES,     # Slight tilt to see Earth nicely
        )

        # Add Earth to scene
        self.add(earth)
        
        # Realistic Earth rotation (counterclockwise when viewed from North Pole)
        # Real Earth: 360° in 24 hours = 15°/hour = 0.25°/minute
        # For visual effect, we'll speed this up significantly
        rotation_speed = -0.4  # Negative for counterclockwise, adjust for desired speed
        earth.add_updater(lambda m, dt: m.rotate(rotation_speed * dt, axis=UP))
        
        # Wait 3 seconds with just the spinning Earth and stars
        self.wait(3)
        
        # Create and animate gridlines appearing
        mesh = SurfaceMesh(earth)
        mesh.set_stroke(BLUE_B, 0.8, opacity=0.7)  # Slightly thicker, more visible
        
        self.play(
            ShowCreation(mesh, lag_ratio=0.01, run_time=2),
        )
        
        # Sync gridlines with Earth rotation
        mesh.add_updater(lambda m, dt: m.rotate(rotation_speed * dt, axis=UP))
        
        # Continue for total of 10 seconds (3 + 2 + 5 = 10)
        self.wait(5) 