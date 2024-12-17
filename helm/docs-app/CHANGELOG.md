# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Use `requiredDuringSchedulingIgnoredDuringExecution` for `podAntiAffinity`
- Add `PodDisruptionBudget` (PDB) for all deployments
- Add `RollingUpdate` strategy with `maxSurge: 1` and `maxUnavailable: 1`

### Changed

### Removed
