<h1 align="center">
  <br>
  <a href="https://notaroomba.dev"><img src="https://raw.githubusercontent.com/notaroomba/simpleflightcontroller/main/assets/logo.png" alt="SFC" width="200"></a>
  <br>
  Simple Flight Controller
  <br>
</h1>

<h4 align="center">
A comprehensive guide on building a flight controller from scratch for rockets!
</h4>

<div align="center">

![KiCad](https://img.shields.io/badge/kicad-%2300578F.svg?style=for-the-badge&logo=kicad&logoColor=white)
![STM32](https://img.shields.io/badge/STM32-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white)

</div>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#guide">Guide</a> •
  <a href="#pcb">PCB</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

<img src="blender/render.png" alt="Flight Controller PCB" width="800"/>

## Key Features

- **STM32F722RET6 microcontroller** for high-performance control
- **ICM-45686 IMU** for precise motion tracking
- **BMP580 barometer** for altitude sensing
- **MicroSD card storage** for flight data logging
- **Dual servo outputs** for TVC or fin control
- **2-cell LiPo support** with integrated BQ25883 charger
- **USB-C connectivity** for programming and data transfer
- **Compact design** optimized for rocket applications

## Guide

Check out the comprehensive [GUIDE.md](GUIDE.md) that walks you through:

- Component selection and requirements
- Schematic design with detailed explanations
- Communication protocols (I2C, SPI, UART, USB)
- PCB layout and routing best practices
- Power management circuitry
- Manufacturing with JLCPCB

## PCB

Designed in KiCad with careful attention to signal integrity, power distribution, and compact layout suitable for rocket applications.

### Schematic

<img src="assets/kicad_final_schematic.png" alt="Schematic" width="800"/>

### PCB Layout

<img src="assets/pcb_final_complete.png" alt="PCB Layout" width="800"/>

## Credits

This project uses:

- [KiCad](https://www.kicad.org/)
- [STM32CubeMX](https://www.st.com/en/development-tools/stm32cubemx.html)
- [easyeda2kicad.py](https://github.com/uPesy/easyeda2kicad.py)
- [Hack Club Blueprint](https://blueprint.hackclub.com/)

## You may also like...

- [Trace](https://github.com/NotARoomba/Trace) – A comprehensive PCB ruler with reference footprints
- [Cyberboard](https://github.com/NotARoomba/Cyberboard) – A Raspberry Pi Pico-sized STM32 development board with Bluetooth
- [CyberCard](https://github.com/NotARoomba/CyberCard) – A Cyberpunk themed NFC hacker card
- [Niveles De Niveles](https://github.com/NotARoomba/NivelesDeNiveles) – Real-time flood alert app
- [Linea](https://github.com/NotARoomba/Linea) – An EMR tablet
- [Tamaki](https://github.com/NotARoomba/Tamaki) – A cute HackPad

## License

MIT

---

> [notaroomba.dev](https://notaroomba.dev) &nbsp;&middot;&nbsp;
> GitHub [@NotARoomba](https://github.com/NotARoomba) &nbsp;&middot;&nbsp;