# Shadow Survivor - Getting Started Guide

Welcome to Shadow Survivor! This guide will help you get up and running quickly.

## Quick Start (2 minutes)

1. **Install Python** (if you haven't already)
   - Download from [python.org](https://www.python.org/downloads/)
   - Version 3.8 or higher required

2. **Clone the repository**
   ```bash
   git clone https://github.com/wmsyafiq/Shadow-survivor.git
   cd Shadow-survivor
   ```

3. **Install Pygame**
   ```bash
   pip install pygame
   ```

4. **Run the game**
   ```bash
   python ShadowSurvivor.py
   ```

## Basic Controls

| Key | Action |
|-----|--------|
| **Arrow Keys** or **WASD** | Move character |
| **Space** | Start game, select upgrade |
| **A/D** or **Left/Right** | Navigate upgrade options |
| **ESC** | Pause/Resume |

## Game Basics

### Main Menu
- Press **SPACE** to start the game

### During Gameplay
1. **Move** around to avoid enemies
2. **Projectiles** fire automatically at nearby enemies
3. **Defeat enemies** to gain XP and score
4. **Level up** by collecting enough XP
5. **Choose upgrades** when you level up
6. **Survive** as long as possible!

### Game Over
- View your final stats
- Press **SPACE** to play again

## Understanding the HUD

```
┌─────────────────────────────────────────────┐
│ HP: 100/100  Wave 1                 Score: 500 │
│ Level: 2     Enemies: 12            Kills: 25 │
│ [XP Progress Bar]                           │
└─────────────────────────────────────────────┘
```

- **HP**: Your current health / maximum health
- **Level**: Your current level
- **Wave**: Current enemy wave number
- **Enemies**: Number of active enemies on screen
- **Score**: Total XP earned
- **Kills**: Number of enemies defeated
- **XP Bar**: Progress towards next level

## Upgrade System

When you level up, choose one of three upgrades:

### Common Upgrades
- Shadow Strike - Increase damage
- Rapid Assault - Increase fire rate
- Sonic Shuriken - Increase projectile speed
- Iron Body - Increase max HP

### Rare Upgrades
- Shuriken Storm - Fire additional projectiles
- Blood Drain - Heal on kills
- Swift Wind - Increase movement speed

### Epic Upgrades
- Piercing Blade - Pierce through enemies
- Lightning Barrage - Massive fire rate increase

### Legendary Upgrades
- Full Restore - Fully heal

## Enemy Types

| Enemy | Description | Strategy |
|-------|-------------|----------|
| **Goblin** | Fast, weak | Kite and attack |
| **Orc** | Balanced | Standard combat |
| **Imp** | Very fast, weak | Keep distance |
| **Troll** | Slow, strong | Use cover/terrain |
| **Ogre King** | Boss enemy | Use hit-and-run tactics |

## Tips & Tricks

1. **Movement is Key**
   - Avoid clustering with enemies
   - Use the open space to your advantage
   - Keep moving to make enemy hits harder

2. **Upgrade Strategy**
   - Early game: Focus on damage and survival
   - Mid game: Balance between damage and utility
   - Late game: Prioritize DPS and pierce

3. **Optimal Strategies**
   - Kiting: Move in circles around enemies while attacking
   - Farming: Focus on hitting multiple enemies at once
   - Wave management: Learn spawn patterns

4. **Resource Management**
   - Pick up health drops when HP is low
   - Don't waste time on healing when safe
   - Focus on damage when enemies are far

## Troubleshooting

### Game won't start
- Make sure Python 3.8+ is installed
- Verify Pygame is installed: `pip install pygame`
- Check that you're in the correct directory

### Missing sprite images
- Ensure `player.png` and `boss.png` are in the game directory
- Images should be 50x50 and 200x200 pixels respectively

### Game is running slow
- Close other applications
- Try reducing graphics settings if available
- Check your Python version (3.8+ recommended)

### Crashes during gameplay
- Check the console for error messages
- Make sure all dependencies are installed
- Try restarting the game

## Advanced Configuration

Edit `ShadowSurvivor.py` to customize:

```python
# Display settings
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60

# Difficulty
ENEMY_SPAWN_RATE = 150  # Lower = faster spawn
WAVE_SIZE = 15          # Enemies per wave
```

## Building an Executable

Want to share with friends? Create a standalone executable:

```bash
pip install pyinstaller
pyinstaller ShadowSurvivor.spec
```

The executable will be in the `dist/` folder.

## Getting Help

- Check the [README.md](README.md) for detailed information
- Visit the [GitHub Issues](https://github.com/wmsyafiq/Shadow-survivor/issues)
- Read [CONTRIBUTING.md](CONTRIBUTING.md) to report bugs

## Next Steps

- Experiment with different upgrade strategies
- Try to beat your high score
- Customize the game with your own settings
- Join our community and contribute!

---

**Have fun and keep surviving! 🎮**
