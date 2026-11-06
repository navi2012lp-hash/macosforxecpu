# OpenCore Bootloader for Dell Latitude 3420 (Tiger Lake)

## Hardware
- Device: Dell Latitude 3420 laptop
- CPU: 11th Gen Intel Core i5 / Tiger Lake
- RAM: 32 GB
- Storage: M.2 SSD (internal)
- Boot target: USB installer for validation, then internal SSD for final install

## Status
This repo is a bootable OpenCore EFI payload for testing macOS on the Dell Latitude 3420. It is not a normal app repo and should not be treated like a standard software project.

## Current known boot issue
The main failure seen in the OpenCore logs is a hang at:
- `EXITBS:START`

This corresponds to the OpenCore boot-services transition stage, where the system is still loading the OS but is stuck before the system can continue booting.

## Fixes already applied
- Removed the invalid `DmgLoading` key from `Misc > Boot`
- Kept the valid `DmgLoading` value under `Misc > Security`
- Set `Booter > Quirks > DevirtualiseMmio` to `false`
- Kept `RebuildAppleMemoryMap`, `SyncRuntimePermissions`, and `ProvideCustomSlide` enabled
- Kept `OpenHfsPlus.efi` in the driver list for HFS+ support

## Current config notes
- The repo had contradictory notes about `DevirtualiseMmio`; the current config is intentionally set to `false`.
- The repo previously had a validation error from `DmgLoading` in the wrong OpenCore section.
- The theme load warning for OpenCanopy is cosmetic and not the primary boot blocker.

## Boot procedure
1. Boot the USB installer from the BIOS/UEFI boot menu.
2. Use verbose logging (`-v`) and keep the full OpenCore logs.
3. If the system hangs at `EXITBS:START`, capture the last 20-50 lines before the freeze.
4. Use the same USB installer volume name for clarity; do not rely on the default `(dmg)` label.

## Practical note
This is a hardware-specific OpenCore configuration. It requires a matching Dell Tiger Lake ACPI and kext setup. The repo is a work-in-progress and may need further hardware-specific tuning after the config validation issues are resolved.
