# OpenCore Bootloader for Dell Latitude 3420 (Tiger Lake)

## Hardware Specs
- Device: Dell Latitude 3420 Laptop
- Processor: 11th Gen Intel Core i5 (Tiger Lake, e.g., i5-1135G7)
- Memory: 32 GB RAM
- Storage: Single internal M.2 SSD slot

## Configuration
- OpenCore version: 1.0.8
- Bootloader: OpenCore 1.0.8
- Boot drive: USB (EFI/OC) for testing, internal SSD for permanent install
- macOS Version: 26 (Tahoe)

## Configuration Details
- Boot args: -v -allow3d -disablegfxfirmware
- SMBIOS: MacBookPro16,2
- DeviceProperties: Empty (no spoofing)
- Graphics: WhateverXe.kext (Tiger Lake Iris Xe translation)
- Kexts: Lilu, VirtualSMC, WhateverXe, AMFIPass, itlwm (disabled)
- ACPI: SSDT-PLUG, SSDT-AWAC, SSDT-EC-USBX, SSDT-PNLF, SSDT-RHUB

## Usage
1. Boot from USB with F12
2. Select "NO NAME (external)" to test
3. If successful, swap internal SSD and install macOS
4. Apply WhateverXe-Graphics.pkg post-install

## Notes
- Requires physical hardware boot - no VM/Docker testing possible
- Requires macOS 26+ BaseSystem.dmg for installer
- May need to adjust boot-args for specific hardware
''')
print("Created README.md")