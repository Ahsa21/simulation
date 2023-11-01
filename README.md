## Description

The project creates a network of places, transitions, and resources, representing a miniature world.
The core components are transitions that act based on predetermined resources available via input channels.
Different types of Resources have different types of places and are manipulated by transitions. 

### Resource Dynamics

- **Workers**: Essential for production and consumption of products and food. Workers have a vitality that can fluctuate but never surpass 100%.
   If vitality reaches 0%, the worker dies. when all workers die, the simulation ends.
- **Food**: Varied in quality, produced in fields, and consumed by workers.
- **Products**: Manufactured in factories and consumed by workers.

### Place Functions

- **Barack**: A waiting room for workers.
- **Warehouse**: Stores food.
- **Inventory**: Stores products.

### Transition Functions

- **Factories**: Produce products but decrease a worker's vitality. Accidents might lead to worker fatalities.
- **Fields**: Produce food without affecting a worker's vitality but there are risks for accidents.
- **Dining_room**: Vitality restoration for workers but with varying effectiveness based on food quality. Poor quality can lead to reduced vitality.
- **Home**: Workers recover here, with actions that involve resting a worker or enabling two workers to marry and become three.

## Dependencies
...
This addition emphasizes the simulation's representation as a self-contained miniaturized world with its unique set of resources, places, and interactions.


## Dependencies

The libraries used in this project include:
- `deque` from `collections`
- `random`
- `sqlite3`
- `Workbook` and `load_workbook` from `openpyxl`
- `pyplot` from `matplotlib`

## Data Storage and Analysis

The project utilizes a database file to store resource data and generates an Excel file. The database and Excel files allow users to view, analyze, and visualize resource data via diagrams representing three different resource lines.

## Usage

To use the program:
1. Run `create_db.py` to generate the database file.
2. Execute `file.py` to run the simulation.

## Contribution and License

This project is open for everyone to use and contribute to.
