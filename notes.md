

Organization of the manim code base:

The fundmental unit of video production is the `Scene` (in `scene/scene.py`). You create your own scene by making a subclass of `Scene` and defining a `construct` method for that class. Your `construct` should make various animation-making function calls, which you can view by running
`python extract-scene.py yourscriptname.py YourClassName -pl`. 

Animations are produced by calling methods like `Write`, `GrowFromCenter`, and `Transform` on various `Mobject` types, such as `Point`, `Circle`, `Line`, or `TexMobject` (for text and math expressions). 

