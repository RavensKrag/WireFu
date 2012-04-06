===== How to Play =====

Controls:
	Move Left:		Left Arrow
	Move Right:		Right Arrow
	Jump:			Spacebar

Run and jump your way to the the yellow platform.  Jump onto the zipline and 
your character will automatically grab onto it.  This will will help you cross 
gaps that are too long to be crossed with the jump.  Simply press the jump
key to let go of the zipline.

Note that the player must stand on the yellow platform for half a second
before the timer will stop, signaling the end of the level.  Thus, be
mindful of the gap behind the yellow platform.
==============================

===== OS Deployment Notes =====
The game only works on Linux and 32 bit Windows.  For 64 bit versions of
windows, only 32 bit python is supported.

update
==========

===== Code Structure =====
Most of the packages should be fairly self explanatory, based on their names.
An attempt to provide insight into the reasoning behind the division of
different packages will be given below.

User interface objects are contained within the user_interface package.

Objects which populate the game world are under the gameobjects directory.
Game objects are divided into two types.  Static objects (which do not move)
and nonstatic objects (which do move).

Various other systems, such as the input manager, and the collision handlers
for the physics library are present under the main directory.  Methods which
provide access to commonly used properties are housed in the Physics package,
which takes advantage of python's multiple inheritance to add these convenient 
methods to the gameobjects.  The separation is to keep the physics code
away from the main game logic.  In much the same way, the collision handlers
are given their own file.

They are much too verbose to be mixed into the files they pertain to.  Also, it
is not clear whether it would be better to associate a collision handler for
collisions between the player and the environment in the Player class or one of 
the environment object classes.

Animation is currently a filler package until art assets can be generated.
At that time, the animation package will house the animations for all of
the various game objects.

The pymunk directory houses the pymunk libraries, which are bindings for the
chipmunk rigid body physics library.  Currently, the directory houses 32 bit
Windows and Linux binaries, as well as a 64 bit Linux binary.
==============================




The basic design of the game remains the same as in the pitch document.  
However, the enemies have not yet been implemented, just the level structure.
The enemies will be present in the full prototype.
