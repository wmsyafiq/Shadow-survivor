# Shadow Survivor - Ninja Edition

A fast-paced, pixel-art inspired survivor-style game built with Python and Pygame. Battle waves of increasingly challenging enemies, level up, unlock powerful upgrades, and face mighty bosses in this thrilling arcade experience.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎮 Game Features

### Gameplay Mechanics
- **Wave-Based Combat**: Face progressively more challenging waves of enemies
- **Auto-Shooting System**: Automatically target and attack nearby enemies
- **Dynamic Enemy Types**: Encounter Goblins, Orcs, Imps, and Trolls with unique stats
- **Boss Battles**: Every 5th wave spawns a powerful Ogre King boss with multiple phases
- **Level Up System**: Gain XP from defeated enemies and unlock powerful upgrades

### Upgrade System
- **15+ Unique Upgrades**: Choose from various power-ups including:
  - Shuriken Storm - Fire additional projectiles
  - Shadow Strike - Increase damage output
  - Piercing Blade - Pierce through multiple enemies
  - Blood Drain - Heal on kills
  - Full Restore - Complete health recovery
  - Swift Wind - Movement speed boost
  - And many more!

### Visual Polish
- **Smooth Camera System**: Follows player movement seamlessly
- **Particle Effects**: Visual feedback for attacks, hits, and level-ups
- **Grid-Based World**: Infinite scrolling environment
- **Pixel Art Aesthetics**: Retro-style enemy and character designs
- **Dynamic HUD**: Real-time display of health, level, XP, wave, and score

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/wmsyafiq/Shadow-survivor.git
   cd Shadow-survivor
   ```

2. **Install dependencies**
   ```bash
   pip install pygame
   ```

3. **Ensure asset files are present**
   Make sure you have the following image files in the project directory:
   - `player.png` - Player character sprite (recommended 50x50 px)
   - `boss.png` - Boss character sprite (recommended 200x200 px)

### Running the Game

```bash
python ShadowSurvivor.py
```

## 🎯 How to Play

### Controls
- **Arrow Keys** or **WASD**: Move your character
- **Space**: Start game / Select upgrade / Confirm actions
- **A/D or Left/Right Arrow**: Navigate upgrade options
- **ESC**: Pause/Resume game

### Game Objective
Survive as long as possible and eliminate as many enemies as you can. Each defeated enemy grants experience points that contribute to leveling up. Upon leveling up, choose one of three available upgrades to enhance your abilities.

### Progression
1. **Waves**: Each wave contains 15+ enemies (increases with progression)
2. **Leveling**: Collect XP drops from defeated enemies
3. **Upgrades**: Select enhancements when you level up
4. **Scaling Difficulty**: Enemies become stronger and spawn faster with each wave
5. **Boss Fights**: Every 5th wave, face the ultimate challenge!

## 📊 Game Statistics

### Enemy Types
| Enemy | Speed | HP | XP | Difficulty |
|-------|-------|----|----|------------|
| Goblin | Fast | Low | Low | Easy |
| Orc | Medium | Medium | Medium | Normal |
| Imp | Very Fast | Very Low | Medium | Dangerous |
| Troll | Slow | High | High | Tough |

### Scaling
- Enemy strength increases by 3% per wave
- Spawn rate increases with wave progression
- Boss health scales with current wave (150 + wave * 75)

## 🛠️ Project Structure

```
Shadow-survivor/
├── ShadowSurvivor.py          # Main game file
├── ShadowSurvivor.spec        # PyInstaller configuration
├── player.png                 # Player sprite
├── boss.png                   # Boss sprite
├── README.md                  # This file
├── CONTRIBUTING.md            # Contribution guidelines
└── build/                     # Build artifacts (PyInstaller)
```

## 🏗️ Architecture Overview

### Core Classes

**Player**
- Manages player position, health, level, and upgrades
- Handles movement and projectile configuration
- Implements health regeneration and damage mechanics

**Enemy**
- Represents standard enemies with dynamic stats
- Scales difficulty based on current wave
- Supports multiple enemy types with unique characteristics

**Boss**
- Extends Enemy class with enhanced mechanics
- Implements phase system (gets faster as HP decreases)
- Features special boss-only visual effects

**Projectile**
- Handles projectile physics and movement
- Implements piercing mechanics
- Renders with trail effect

**Game**
- Main game loop and state management
- Handles collision detection
- Manages waves, upgrades, and game progression

**Camera**
- Implements viewport system following the player
- Enables infinite world exploration

## 🎨 Customization

### Modify Game Parameters
Edit constants at the top of `ShadowSurvivor.py`:
```python
SCREEN_WIDTH = 1000        # Window width
SCREEN_HEIGHT = 700        # Window height
FPS = 60                   # Target framerate
```

### Add Custom Upgrades
Extend the `get_upgrade_options()` method in the Game class:
```python
UpgradeOption("Custom Name", "Description", lambda p: custom_effect(p), "rarity")
```

### Adjust Enemy Properties
Modify the `types` list in the `Enemy.__init__()` method to change stats, speeds, and spawn rates.

## 📦 Building an Executable

### Using PyInstaller
```bash
pip install pyinstaller
pyinstaller ShadowSurvivor.spec
```

The executable will be created in the `dist/` folder.

## 🐛 Known Issues

- None currently reported

## 🔄 Future Enhancements

- [ ] Sound effects and background music
- [ ] Additional enemy types and bosses
- [ ] Power-up items in the game world
- [ ] Leaderboard system
- [ ] Multiple difficulty levels
- [ ] Mobile/touch controls support
- [ ] Achievements and statistics tracking
- [ ] Improved visual effects and animations

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**wmsyafiq**
- GitHub: [@wmsyafiq](https://github.com/wmsyafiq)

## 🙏 Acknowledgments

- Built with [Pygame](https://www.pygame.org/)
- Inspired by survivor-style arcade games
- Retro pixel art aesthetic

## 📧 Support

For issues, questions, or suggestions, please open an issue on the [GitHub repository](https://github.com/wmsyafiq/Shadow-survivor/issues).

---

**Happy Gaming! 🎮**
