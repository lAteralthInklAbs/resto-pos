# Legacy Code (Original Tkinter + MySQL)

This directory contains the original Restaurant POS built with Python Tkinter + MySQL (pymysql).
Preserved for reference. The reengineered version in the parent directory uses Flask + SQLite with MVC architecture, tests, and CI/CD.

## Original Flow
1. 3.cashier_pos.py - Cashier login (entry point)
2. PoSFile.py / 2.Cashier Main menu.py - Main menu
3. 1.Customer-infopage.py - Customer registration
4. 7.menu_interface.py - Food menu and ordering
5. 8.Payment page.py - Payment processing
6. RoC main.py - Reports

## Known Issues
- Hardcoded MySQL password
- No error handling
- No tests
- Monolithic scripts
