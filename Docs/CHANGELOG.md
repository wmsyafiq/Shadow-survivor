# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project setup and structure
- Core gameplay mechanics (movement, combat, waves)
- Enemy types: Goblin, Orc, Imp, Troll, and Boss (Ogre King)
- Projectile system with piercing mechanics
- Level and upgrade system
- 15+ unique upgrades with different rarities
- Particle effects and visual feedback
- Score and kill tracking
- Camera system with smooth following
- HUD with real-time stats display
- Game states (menu, playing, paused, upgrade, game_over)
- Boss battles with phase system
- XP and pickup system

### Features
- Auto-targeting projectile system
- Wave-based enemy progression
- Dynamic difficulty scaling
- Multi-phase boss encounters
- Invulnerability frames on damage
- Health regeneration system
- Asset loading for player and boss sprites
- PyInstaller support for executable building

## [1.0.0] - 2024-11-27

### Added
- Initial release
- Full game implementation
- All core features and mechanics
- README with comprehensive documentation
- Contributing guidelines
- Code of Conduct
- Getting Started guide
- MIT License

---

## Semantic Versioning

This project uses semantic versioning:
- **MAJOR**: Breaking changes (e.g., 1.0.0 → 2.0.0)
- **MINOR**: New features (e.g., 1.0.0 → 1.1.0)
- **PATCH**: Bug fixes (e.g., 1.0.0 → 1.0.1)

## How to Use This Changelog

When making changes, please update this file by:

1. Adding your changes under the "Unreleased" section
2. Using one of these categories: **Added**, **Changed**, **Deprecated**, **Removed**, **Fixed**, **Security**
3. Being descriptive and clear about what changed
4. Including issue/PR references when applicable

Example:
```markdown
### Added
- New feature description (#123)

### Fixed
- Fixed crash when upgrading at max level (#124)

### Changed
- Improved enemy spawning algorithm for better balance
```

## Release Process

When creating a new release:
1. Move "Unreleased" section to a new version section with date
2. Update version number following semantic versioning
3. Tag the release in git with the version number
4. Create a GitHub release with the changelog
