> "yesterday only me and god could understand my code, today only god can"

# ITWC development kit

## Introduction
well well well, i'm a good developer that for sure (spoiler : no), so if even myself can't read some of my script you can't ! (i mean yes you can but it's complicated.)
And because i'm a crazy man with a crazy brain, my code is absolute garbadge ! so i will explain **every single itty bitty line of code** right here so everyone can understand and build magnificent thing with my tools ! 

i will mostly explain fundamental things like the structure of some node and what do you have to put in all the @export variable (i love @export you will see).

So have fun decrypting all of my intricated and spagettied script and good luck! (and sorry for the bad spelling i'm a frogeater so i don't know english very well)

## related information

so building a game is a complicated and long process so obviously i can't create everything from 0. Thus you can find right here all external tool and stuff required to work with ITWC.

- ITWC is a game created with [godot 4.4 .NET version](https://godotengine.org/releases/4.4/)

- [core code](https://github.com/The-Fourth-Wheel-Studio/ITWC) and ITWC dev kit

- ITWC use various godot addons to work listed down there
    - [ITWCdt](https://github.com/The-Fourth-Wheel-Studio/ITWC/tree/main/addons/ITWCdt) the plugin containing all random godot editor tool (obviously it can't work properly without the core code of the game)
    - [discord-rpc-godot](https://github.com/vaporvee/discord-rpc-godot) by vaporvee (currently not activated)




## Contents

### Component

sooo, godot is a powerfull game engine based on tree-like structure through node, i've try to use this potential by creating "component". Component are simply custom node with different behavior that you can ~~in theory~~ drag and drop on your scene and tada ! but because of various technical reason ~~(i'm a bad dev but don't tell this to Martin i want to keep my job)~~ this component system don't work great and is very hard to use, so here's a list of every single component and how they work.

### Node structure

The component system is great and all but if you don't know exaclty in witch order you have to put all your component you will have very difficult time with the red color of the godot's console. You can find here explanation for every component structure, mostly for camera and quest system.

### ITWCdata and game loading

because of various long thinking reason ~~(i wanted to flex)~~ i've created a custom file extension called .ITWCdata that is use to load game ressource and is very usefull for Mods

### Singleton and global class

ITWC have some singleton and global class that you can access anywhere in your code. It can be math utility, file system tool ect..

