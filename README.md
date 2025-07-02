# 🍄 Super Mario Python Game

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)

*A classic Super Mario-style platformer game built entirely in Python using Pygame!*

[Features](#-features) • [Installation](#-installation) • [Controls](#-controls) • [Gameplay](#-gameplay) • [Screenshots](#-screenshots) • [Contributing](#-contributing)

</div>

---

## 🎮 Features

### Core Gameplay
- **🏃‍♂️ Smooth Character Movement** - Responsive controls with realistic physics
- **🦘 Precise Jumping Mechanics** - Variable jump height and gravity system
- **🏗️ Multi-Level Platforming** - Two challenging levels with increasing difficulty
- **💰 Collectible System** - Coins scattered throughout levels for points
- **👾 Dynamic Enemies** - AI-controlled enemies with collision detection
- **🍄 Power-ups** - Mushrooms for extra lives and stars for bonus points

### Game Systems
- **❤️ Lives System** - Start with 3 lives, gain more through power-ups
- **🏆 Scoring System** - Points for coins (100), enemies (200), and power-ups (500-1000)
- **📊 Real-time UI** - Live display of score, lives, coins, and current level
- **🎯 Level Progression** - Complete objectives to advance to next level
- **🔄 Respawn System** - Smart respawning after taking damage or falling

### Technical Features
- **⚡ 60 FPS Gameplay** - Smooth, responsive gaming experience
- **🎨 Custom Graphics** - Hand-drawn game elements using Pygame primitives
- **🏗️ Modular Code Structure** - Clean, maintainable object-oriented design
- **🔧 Easy Customization** - Simple to modify levels, add features, or change mechanics

---

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Quick Start

1. **Clone or download the game files**
   ```bash
   # If using git
   git clone https://github.com/Fahad-Al-Maashani/Super_Mario_Clone_Minimalist.git
   cd super-mario-python
   
   # Or download the mario_game.py file directly
   ```

2. **Install Pygame**
   ```bash
   pip install pygame
   ```

3. **Run the game**
   ```bash
   python mario_game.py
   ```

### Alternative Installation (using virtual environment)
```bash
# Create virtual environment
python -m venv mario_env

# Activate virtual environment
# On Windows:
mario_env\Scripts\activate
# On macOS/Linux:
source mario_env/bin/activate

# Install Pygame
pip install pygame

# Run the game
python mario_game.py
```

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| ⬅️ **Left Arrow** or **A** | Move left |
| ➡️ **Right Arrow** or **D** | Move right |
| ⬆️ **Up Arrow**, **W**, or **Space** | Jump |
| **R** | Restart game (when game over) |
| **Q** | Quit game |

### Pro Tips
- Hold jump longer for higher jumps
- Time your jumps to land on enemies from above
- Collect all coins before reaching the end of each level
- Look for hidden power-ups on elevated platforms

---

## 🏁 Gameplay

### Objective
Navigate through challenging platformer levels, collect coins, defeat enemies, and reach the end of each stage!

### How to Win
1. **Collect all coins** in the level
2. **Reach the right side** of the screen
3. **Complete both levels** to achieve victory

### Game Elements

#### 🪙 Collectibles
- **Coins**: Worth 100 points each - collect them all!
- **Mushrooms**: Red power-ups that grant an extra life (+500 points)
- **Stars**: Yellow power-ups for massive bonus points (+1000 points)

#### 👾 Enemies
- **Black enemies**: Move back and forth on platforms
- **Defeat them**: Jump on top to eliminate and earn 200 points
- **Avoid contact**: Touching from the side costs you a life

#### 🏗️ Platforms
- **Brown platforms**: Standard solid ground
- **Multiple levels**: Navigate between different platform heights
- **Strategic placement**: Use platforms to avoid enemies and reach collectibles

### Scoring System
| Action | Points |
|--------|--------|
| Collect Coin | +100 |
| Defeat Enemy | +200 |
| Mushroom Power-up | +500 |
| Star Power-up | +1000 |

---

## 📸 Screenshots

```
🎮 Level 1 - Learning the Ropes
┌─────────────────────────────────────────────────────────┐
│  ☁️        ☁️        ☁️                               │
│                                                         │
│     🪙🪙🪙                    🍄                        │
│   ████████       🪙🪙                                   │
│              ████████    👾    🪙🪙🪙                   │
│                        ████████████                     │
│  🔴                                        ⭐           │
│██████████                            ████████████████  │
└─────────────────────────────────────────────────────────┘
```

```
🎮 Level 2 - Advanced Challenge
┌─────────────────────────────────────────────────────────┐
│  ☁️        ☁️        ☁️                               │
│                               🪙🪙  🍄                  │
│         🪙    🪙    🪙    ████████                      │
│       ████  ████  ████    👾                           │
│  🪙           👾           🪙                           │
│████      ████████      ████████                        │
│  🔴                                                     │
│██████              ██████            ████████████████  │
└─────────────────────────────────────────────────────────┘
```

---

## 🏗️ Code Structure

```
mario_game.py
├── Player Class      - Mario character with physics and controls
├── Platform Class    - Static platforms for level geometry  
├── Coin Class        - Collectible coins with collision detection
├── Enemy Class       - AI enemies with movement and combat
├── Powerup Class     - Special items (mushrooms, stars)
├── Game Class        - Main game loop and level management
└── Main Execution    - Game initialization and startup
```

### Key Components

- **Physics Engine**: Custom gravity and collision detection
- **Level System**: Procedural level generation with increasing difficulty
- **State Management**: Game states (playing, game over, victory)
- **Event Handling**: Keyboard input and game events
- **Rendering Pipeline**: Efficient drawing and UI updates

---

## 🎨 Customization

Want to modify the game? Here are some easy customization options:

### Add New Levels
```python
elif self.level == 3:
    # Add your platforms
    self.platforms.extend([
        Platform(x, y, width, height),
        # Add more platforms...
    ])
    
    # Add coins, enemies, powerups...
```

### Modify Game Physics
```python
# In Player class __init__
self.speed = 5          # Movement speed
self.jump_power = -15   # Jump strength
self.gravity = 0.8      # Gravity force
```

### Change Colors and Appearance
```python
# Modify color constants
RED = (255, 0, 0)      # Mario color
BROWN = (139, 69, 19)  # Platform color
YELLOW = (255, 255, 0) # Coin color
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help improve the game:

### Ways to Contribute
- 🐛 **Bug Reports**: Found a bug? Open an issue!
- 💡 **Feature Requests**: Have an idea? We'd love to hear it!
- 🎨 **Graphics**: Improve the visual design
- 🎵 **Sound**: Add sound effects and music
- 🏗️ **Code**: Submit pull requests with improvements

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

---

## 📋 Future Enhancements

### Planned Features
- 🎵 **Sound Effects**: Jump sounds, coin collection, background music
- 🎨 **Sprite Graphics**: Replace primitive shapes with detailed sprites
- 🏗️ **Level Editor**: In-game level creation tool
- 💾 **Save System**: Save progress and high scores
- 🎮 **Controller Support**: Gamepad/joystick compatibility
- 🌟 **Special Abilities**: Fire power, invincibility star effects
- 🏆 **Achievements**: Unlock system for completing challenges
- 📱 **Mobile Version**: Touch controls for mobile devices

### Advanced Features
- 🤖 **AI Improvements**: Smarter enemy behavior patterns
- 🌍 **World Map**: Visual level selection screen
- 👥 **Multiplayer**: Local co-op gameplay
- 🎯 **Boss Battles**: End-of-world boss encounters
- 🔄 **Procedural Generation**: Randomly generated levels
- 📊 **Statistics**: Detailed gameplay analytics

---

## 📝 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025 Super Mario Python Game

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 🙏 Acknowledgments

- **Nintendo** - For creating the original Super Mario Bros that inspired this project
- **Pygame Community** - For the excellent game development library
- **Python Software Foundation** - For the amazing Python programming language
- **Open Source Community** - For tools, libraries, and inspiration

---

## 📞 Support

Having trouble? We're here to help!

- 🐛 **Issues**: Report bugs on [GitHub Issues](https://github.com/Fahad-Al-Maashani/Super_Mario_Clone_Minimalist/issues))

---

<div align="center">

**⭐ Star this repository if you enjoyed the game! ⭐**

Made with ❤️ and lots of ☕ by passionate game developers

[🔝 Back to Top](#-super-mario-python-game)

</div>
