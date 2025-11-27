# Contributing to Shadow Survivor

Thank you for your interest in contributing to Shadow Survivor! We welcome contributions from the community and appreciate your help in making this project better.

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project, you agree to abide by its terms.

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps which reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why**
* **Include screenshots and animated GIFs if possible**
* **Include your environment details** (Python version, OS, etc.)

### 💡 Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior and expected behavior**
* **Explain why this enhancement would be useful**

### 🔧 Pull Requests

* Fill in the required template
* Follow the Python and project styleguides
* End all files with a newline
* Avoid platform-dependent code

## Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/your-username/Shadow-survivor.git
   cd Shadow-survivor
   ```

2. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Set up your development environment**
   ```bash
   pip install pygame
   ```

4. **Make your changes**
   - Write clear, descriptive commit messages
   - Test your changes thoroughly
   - Ensure the game runs without errors

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Provide a clear description of the changes
   - Reference any related issues

## Styleguides

### Python Style

* Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) conventions
* Use descriptive variable and function names
* Add comments for complex logic
* Maximum line length: 100 characters (soft limit)

### Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

Example:
```
Add new enemy type: Dark Knight

- Implement Dark Knight class extending Enemy
- Balance stats for mid-wave difficulty
- Add visual sprite and animations
- Fixes #123
```

### Documentation

* Update README.md if you add or change features
* Add docstrings to new functions and classes
* Use clear, simple language
* Keep documentation up-to-date with code changes

## Types of Contributions

### Bug Fixes
* Fix game crashes or unexpected behaviors
* Improve collision detection accuracy
* Optimize performance

### New Features
* New enemy types or boss battles
* Additional upgrade options
* UI improvements
* Game mechanics enhancements

### Documentation
* Improve existing documentation
* Add code examples
* Create tutorials or guides
* Fix typos and clarify instructions

### Code Quality
* Refactor code for better readability
* Improve performance
* Reduce code duplication
* Add error handling

## Issue Labels

* `bug` - Something isn't working
* `enhancement` - New feature or request
* `documentation` - Improvements or additions to documentation
* `good first issue` - Good for newcomers
* `help wanted` - Extra attention is needed
* `question` - Further information is requested

## Review Process

1. A maintainer will review your pull request
2. Changes may be requested
3. Once approved, your PR will be merged
4. You'll be credited as a contributor

## Additional Notes

### Project Structure
```
ShadowSurvivor.py          # Main game file with all classes and logic
player.png                # Player sprite image
boss.png                  # Boss sprite image
ShadowSurvivor.spec       # PyInstaller configuration for building executables
```

### Key Classes to Know

* **Game**: Main game loop and state management
* **Player**: Player character with stats and abilities
* **Enemy**: Enemy entities with AI
* **Boss**: Special boss enemy type
* **Projectile**: Player projectiles/attacks
* **Particle**: Visual effect particles
* **Upgrade**: Player enhancement system

## Recognition

Contributors will be recognized in:
* The project's README.md
* GitHub's contributor page
* Commit history

## Questions?

Feel free to open an issue with the `question` label or reach out to the maintainers.

---

**Thank you for contributing to Shadow Survivor! 🎮**
