import pytest

from manim import *
from manim.opengl import *
from manim.renderer.opengl_renderer import OpenGLRenderer
from tests.test_graphical_units.testing.frames_comparison import frames_comparison

__module_test__ = "opengl"


@pytest.mark.xfail(
    reason="OpenGL is really hard to test. It will be tested when the design is largely improved. This test has an error for a reason that I can't understand/s"
)
@frames_comparison(use_opengl_renderer=True)
def test_Circle(scene):
    circle = OpenGLCircle().set_color(RED)
    scene.add(circle)
    scene.wait()

@frames_comparison(renderer_class=OpenGLRenderer, renderer="opengl", opengl_samples=4)
def test_opengl_samples(scene):
    sphere = OpenGLSphere()
    scene.add(sphere)
    scene.wait()