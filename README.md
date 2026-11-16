# Drone collab in Django

Full stack application in Django using DRF, templates and bootstrap.

## Tech stack

- Python 3
- Django
- Django REST Framework
- Pillow
- Database: PostgreSQL

## Project structure

- `drone_collab/`: project settings and root URLs
- `drone_management/`: Django app
- Tests: `drone_management/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `Drone` | `drone_management` | manufacturer, model, lattitude, longitude, batteryLevel, playloadCapacity, max_flight_time, max_speed, max_range, type |
| `Camera` | `drone_management` | type, resolution, lenses_type, drone |
| `Weapon` | `drone_management` | caliber, range |
| `AttackDrone` | `drone_management` | weapon |
| `Mission` | `drone_management` | name, objectives, start_time, end_time, area_to_cover, type, drones |
| `MissionDrones` | `drone_management` | drone, mission, role |

## URL routes

Declared in `urls.py`:

- `/blog/`
- `/drone-collab/`
- `/drone-missions/<int:id>`
- `/drones/ (router)`
- `/cameras/ (router)`
- `/weapons/ (router)`
- `/attack-drones/ (router)`
- `/missions/ (router)`
- `/mission-drones/ (router)`

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

`settings.py` is configured for PostgreSQL: create the database and use your own credentials before running `migrate`.

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
