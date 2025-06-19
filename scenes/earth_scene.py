from manimlib import *

class SpinningEarth(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }

    def construct(self):
        # Create title text
        title_text = Text("Spinning Earth with Gridlines")
        title_text.fix_in_frame()
        title_text.to_edge(UP)
        self.add(title_text)
        self.wait(0.1)

        # Create sphere for Earth
        sphere = Sphere(radius=3, resolution=(20, 20))
        sphere.set_color(BLUE_E)
        sphere.shift(IN)
        
        # Create mesh gridlines
        mesh = SurfaceMesh(sphere)
        mesh.set_stroke(WHITE, 1, opacity=0.7)

        # Set camera perspective
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )

        # Animate Earth appearance
        self.play(
            FadeIn(sphere),
            ShowCreation(mesh, lag_ratio=0.01, run_time=3),
        )
        
        # Rotate the Earth and mesh together
        self.play(
            Rotate(sphere, PI / 2), 
            Rotate(mesh, PI / 2),
            run_time=2
        )
        
        # Add continuous rotation to both
        sphere.add_updater(lambda m, dt: m.rotate(0.5 * dt, axis=UP))
        mesh.add_updater(lambda m, dt: m.rotate(0.5 * dt, axis=UP))
        
        # Add ambient camera rotation
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1 * dt))
        
        # Let it spin for a while
        self.wait(10) 