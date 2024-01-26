import pathlib as Path

import json

#read data as python object and convert into a python project
path=Path('eq_data/eq_data_1_day_m1.geojson')
contents=path.read_text()
all_eq_data=json.loads(contents)

#create more readable version of data file.
path=Path('eq_data/eq_data_1_day_m1.geojson')
readable_contents = json.dumps(all_eq_data,indent=4)
path.write_text(readable_contents)

